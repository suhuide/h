import serial
import struct
import time
import os
import zlib
import threading

# Partition part
# Assume MAX_PARTITION_COUNT is 15
MAX_PARTITION_COUNT = 15

# Define partition_entry strut
partition_entry_fmt = '8sHHIHHI'

# Define partition_table strut
partition_table_fmt = f'IHHHH4s{MAX_PARTITION_COUNT * struct.calcsize(partition_entry_fmt)}s4sI'

def remove_crc(data):
    result = bytearray()
    for i in range(0, len(data), 34):  # ÿ 34 �ֽڴ���һ��
        result.extend(data[i:i+32])  # ֻ����ǰ 32 �ֽ�
    return bytes(result)

def add_crc(data):
    result = bytearray()
    for i in range(0, len(data), 32):  # ÿ 32 �ֽڴ���һ��
        chunk = data[i:i+32]
        crc = calculate_crc(chunk)  # ���� CRC У��ֵ
        result.extend(chunk)
        result.extend(crc.to_bytes(2, byteorder='little'))  # ���� CRC У��ֵ
    return bytes(result)

def calculate_crc(data):
    crc = 0xFFFF
    for byte in data:
        for i in range(8):
            if (crc & 0x8000) != 0:
                crc <<= 1
                crc &= 0xFFFF
                crc ^= 0x1021
            else:
                crc <<= 1
                crc &= 0xFFFF
            if (byte & (1 << (i))) != 0:
                crc ^= 0x1021
    crc = (crc >> 8) | (crc << 8)
    return crc & 0xFFFF

def read_partition_table(data, offset, length):
    # ����������ȡ����������
    table_data = data[offset:offset+length]

    # ȥ�� CRC ����
    table_data = remove_crc(table_data)

    # ���� partition_table
    table = struct.unpack(partition_table_fmt, table_data)

    magic = hex(table[0])
    version = hex(table[1])
    table_size = hex(table[2])
    part_cnt = hex(table[3])
    part_entry_size = hex(table[4])
    reserved1 = table[5].hex()

    parts = []
    part_data = table[6]
    for i in range(MAX_PARTITION_COUNT):
        start = i * struct.calcsize(partition_entry_fmt)
        end = start + struct.calcsize(partition_entry_fmt)
        part = struct.unpack(partition_entry_fmt, part_data[start:end])
        parts.append({
            'name': part[0],
            'type': hex(part[1]),
            'flag': hex(part[2]),
            'offset': hex(part[3]),
            'seq': hex(part[4]),
            'reserve': hex(part[5]),
            'entry_offs': hex(part[6])
        })

    reserved2 = table[7].hex()
    table_crc = hex(table[8])

    result = {
        'magic': magic,
        'version': version,
        'table_size': table_size,
        'part_cnt': part_cnt,
        'part_entry_size': part_entry_size,
        'reserved1': reserved1,
        'parts': parts,
        'reserved2': reserved2,
        'table_crc': table_crc
    }

    return result

def write_partition_table(data, f_offset, table):
    # �޸�ָ���� seq ֵ
    for part in table['parts']:
        if part['name'] == b'fw1_boot':
            part['seq'] = hex(1)  # �޸� seq Ϊ 0x1
        if part['name'] == b'fw1_app\x00':
            part['seq'] = hex(1)  # �޸� seq Ϊ 0x1

    # ���´������
    magic = int(table['magic'], 16)
    version = int(table['version'], 16)
    table_size = int(table['table_size'], 16)
    part_cnt = int(table['part_cnt'], 16)
    part_entry_size = int(table['part_entry_size'], 16)
    reserved1 = bytes.fromhex(table['reserved1'])
    reserved2 = bytes.fromhex(table['reserved2'])
    table_crc = int(table['table_crc'], 16)

    part_data = bytearray()
    for part in table['parts']:
        name = part['name']
        type_ = int(part['type'], 16)
        flag = int(part['flag'], 16)
        offset = int(part['offset'], 16)
        seq = int(part['seq'], 16)
        reserve = int(part['reserve'], 16)
        entry_offs = int(part['entry_offs'], 16)
        part_data.extend(struct.pack(partition_entry_fmt, name, type_, flag, offset, seq, reserve, entry_offs))

    packed_data = struct.pack(partition_table_fmt, magic, version, table_size, part_cnt, part_entry_size, reserved1, part_data, reserved2, table_crc)

    # ���� CRC ����
    packed_data_with_crc = add_crc(packed_data)
    
    # ���޸ĺ������д�뵽ԭʼ������
    data = bytearray(data)
    
    data[f_offset:f_offset+len(packed_data_with_crc)] = packed_data_with_crc

    return bytes(data)

def fileOverwrite(file_path):
    offset = 0x00000cc0  # ָ��ƫ�Ƶ�ַ
    length = 408  # ���� CRC ���ݺ���ܳ���
    print(f"{file_path} Overwrite!!")

    # ��ȡԭʼ�ļ�����
    with open(file_path, 'rb') as f:
        data = f.read()

    # ��ȡ������������
    partition_table = read_partition_table(data, offset, length)

    # �޸Ĳ�д��ԭ�ļ�
    modified_data = write_partition_table(data, offset, partition_table)

    # д�뵽�µ��ļ�
    with open(file_path, 'wb') as f:
        f.write(modified_data)

# Partition part

def calculate_crc32(file_path):
    try:
        with open(file_path, 'rb') as file:
            crc = 0
            while True:
                data = file.read(4096)
                if not data:
                    break
                crc = zlib.crc32(data, crc)
            final_crc = crc & 0xFFFFFFFF
            return final_crc
    except FileNotFoundError:
        print(f"File {file_path} not found!!")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_bin_file(file_path, chunk_size):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def crc8(data, poly=0x07, seed=0x00):
    crc = seed
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
        crc &= 0xFF
    return crc

def crc32(data, seed=0x00000000):
    crc = zlib.crc32(data, seed) & 0xFFFFFFFF
    return crc

def create_tlv_packet(type_value, address, data):
    # Length field is the sum of 4 bytes for address + the length of data  +  4byte crc  +  8byte header
    total_length = 4 + len(data)  + 4 + 8
    length_field = struct.pack('<H', total_length)
    head_post = 0x01E7
    #crc32 = 0xFFFFFFFF
    # TLV packet: 4 bytes Type, 6 bytes Length (2 bytes data length + 4 bytes address), data, crc
    #tlv_packet = struct.pack('>I', type_value) + length_field + struct.pack('>H', head_post) + struct.pack('<I', address) + data + struct.pack('<I', crc32)

    data_part = struct.pack('<I', address) + data

    # 计算 CRC8
    crc8_value = crc8(data_part)
    head_post += crc8_value  # 替换 E7 为计算的 CRC8 值
    head_post_field = struct.pack('>H', head_post)
    print(f"{head_post_field}")


    tlv_packet = struct.pack('>I', type_value) + length_field + head_post_field + data_part

    # 计算 CRC32
    crc32_value = crc32(tlv_packet)
    print(f"{crc32_value}")
    crc32_field = struct.pack('<I', crc32_value)

    # 最终数据包
    final_packet = tlv_packet + crc32_field



    return final_packet

def send_factory_cmd(ser):
    f_d = '9E01FA1E0D0001B7018F2DF7F4'
    #f_packet = bytes.fromhex(f_d)
    data_without_crc8 = bytes.fromhex(f_d[:14])
    crc8_value = crc8(data_without_crc8)
    crc8_hex = f"{crc8_value:02X}"
    data_with_crc8_hex = f_d[:14] + crc8_hex + f_d[16:]
    data_with_crc8 = bytes.fromhex(data_with_crc8_hex)

    crc32_value = crc32(data_with_crc8[:-4])
    crc32_bytes = crc32_value.to_bytes(4, byteorder='little')
    crc32_hex = crc32_bytes.hex().upper()
    print(f"{crc32_hex}")
    data_with_crc = data_with_crc8_hex[:-8] + crc32_hex
    print(f"{data_with_crc}")
    f_packet = bytes.fromhex(data_with_crc)
    print(f"{f_packet}")
    ser.write(f_packet)
    print(f"Enter Factory Mode!!!")
    time.sleep(0.1)

    f_d = '9E01FAA00C0001B78F2DF7F4'

    data_without_crc8 = bytes.fromhex(f_d[:14])
    crc8_value = crc8(data_without_crc8)
    crc8_hex = f"{crc8_value:02X}"
    data_with_crc8_hex = f_d[:14] + crc8_hex + f_d[16:]
    data_with_crc8 = bytes.fromhex(data_with_crc8_hex)

    crc32_value = crc32(data_with_crc8[:-4])
    crc32_bytes = crc32_value.to_bytes(4, byteorder='little')
    crc32_hex = crc32_bytes.hex().upper()
    print(f"{crc32_hex}")
    data_with_crc = data_with_crc8_hex[:-8] + crc32_hex
    print(f"{data_with_crc}")
    f_packet = bytes.fromhex(data_with_crc)
    print(f"{f_packet}")
    ser.write(f_packet)
    print(f"Enter Factory Mode!!!")
    time.sleep(0.1)

def send_get_partition_cmd(ser):
    f_d = '9E01FAA10C0001E7FFFFFFFF'

    data_without_crc8 = bytes.fromhex(f_d[:14])
    crc8_value = crc8(data_without_crc8)
    crc8_hex = f"{crc8_value:02X}"
    data_with_crc8_hex = f_d[:14] + crc8_hex + f_d[16:]
    data_with_crc8 = bytes.fromhex(data_with_crc8_hex)

    crc32_value = crc32(data_with_crc8[:-4])
    crc32_bytes = crc32_value.to_bytes(4, byteorder='little')
    crc32_hex = crc32_bytes.hex().upper()
    print(f"{crc32_hex}")
    data_with_crc = data_with_crc8_hex[:-8] + crc32_hex
    print(f"{data_with_crc}")
    f_packet = bytes.fromhex(data_with_crc)

    ser.write(f_packet)
    print(f"Get partition!!!")
    time.sleep(0.1)

def send_get_version_cmd(ser):
    f_d = '9E01FAA50C0001E7FFFFFFFF'

    data_without_crc8 = bytes.fromhex(f_d[:14])
    crc8_value = crc8(data_without_crc8)
    crc8_hex = f"{crc8_value:02X}"
    data_with_crc8_hex = f_d[:14] + crc8_hex + f_d[16:]
    data_with_crc8 = bytes.fromhex(data_with_crc8_hex)

    crc32_value = crc32(data_with_crc8[:-4])
    crc32_bytes = crc32_value.to_bytes(4, byteorder='little')
    crc32_hex = crc32_bytes.hex().upper()
    print(f"{crc32_hex}")
    data_with_crc = data_with_crc8_hex[:-8] + crc32_hex
    print(f"{data_with_crc}")
    f_packet = bytes.fromhex(data_with_crc)

    ser.write(f_packet)
    print(f"Get version!!!")
    time.sleep(0.1)

def send_erase_cmd(ser, type_value, erase_size, address):
    print(f"Erase {erase_size} bytes start from {hex(address)} !!!")
    # Length field is the sum of 4 bytes for address + the length of data  +  4byte crc  +  8byte header
    
    total_length = 0x14 #4 + len(data)  + 4 + 8
    length_field = struct.pack('<H', total_length)
    head_post = 0x01E7

    data_part = struct.pack('<I', address) + struct.pack('<I', erase_size)

    # 计算 CRC8
    crc8_value = crc8(data_part)
    head_post += crc8_value  # 替换 E7 为计算的 CRC8 值
    head_post_field = struct.pack('>H', head_post)
    print(f"{head_post_field}")


    tlv_packet = struct.pack('>I', type_value) + length_field + head_post_field + data_part

    # 计算 CRC32
    crc32_value = crc32(tlv_packet)
    print(f"{crc32_value}")
    crc32_field = struct.pack('<I', crc32_value)

    # 最终数据包
    final_packet = tlv_packet + crc32_field
    
    ser.write(final_packet)
    print(f"{final_packet}")
    time.sleep(0.5)

def send_verify_cmd(ser, type_value, length, address, crc):
    print(f"Verify {length} bytes start from {hex(address)} !!!")
    # Length field is the sum of 4 bytes for address + the length of data  +  4byte crc  +  8byte header
    total_length = 0x18  # 4 + len(data) + 4 + 8
    length_field = struct.pack('<H', total_length)
    head_post = 0x01E7

    data_part =  struct.pack('<I', address) + struct.pack('<I', length) + struct.pack('<I', crc)

    # 计算 CRC8
    crc8_value = crc8(data_part)
    head_post += crc8_value  # 替换 E7 为计算的 CRC8 值
    head_post_field = struct.pack('>H', head_post)
    print(f"{head_post_field}")


    tlv_packet = struct.pack('>I', type_value) + length_field + head_post_field + data_part

    # 计算 CRC32
    crc32_value = crc32(tlv_packet)
    print(f"{crc32_value}")
    crc32_field = struct.pack('<I', crc32_value)

    # 最终数据包
    final_packet = tlv_packet + crc32_field
    
    ser.write(final_packet)
    print(f"{final_packet}")
    time.sleep(0.5)

def send_reset_cmd(ser):
    f_d = '9E01FAA60C0001E7FFFFFFFF'

    data_without_crc8 = bytes.fromhex(f_d[:14])
    crc8_value = crc8(data_without_crc8)
    crc8_hex = f"{crc8_value:02X}"
    data_with_crc8_hex = f_d[:14] + crc8_hex + f_d[16:]
    data_with_crc8 = bytes.fromhex(data_with_crc8_hex)

    crc32_value = crc32(data_with_crc8[:-4])
    crc32_bytes = crc32_value.to_bytes(4, byteorder='little')
    crc32_hex = crc32_bytes.hex().upper()
    print(f"{crc32_hex}")
    data_with_crc = data_with_crc8_hex[:-8] + crc32_hex
    print(f"{data_with_crc}")
    f_packet = bytes.fromhex(data_with_crc)

    #ser.write(f_packet)
    print(f"System reboot!!!")
    time.sleep(0.1)

def send_tlv_packets(ser, type_value, chunk_size, start_address, file_path):
    address = start_address

    for chunk in read_bin_file(file_path, chunk_size):
        tlv_packet = create_tlv_packet(type_value, address, chunk)
        #h_d = '9E01FAA2500001E70096030000112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeffff2D5DAC49'
        #tlv_packet = bytes.fromhex(h_d)
        ser.write(tlv_packet)
        #print(f"Sent {tlv_packet} packet with address {hex(address)} and {len(chunk)} bytes of data.")
        #print(f"{tlv_packet}")
        time.sleep(0.1)
        #break
        address += chunk_size  # Increment address by chunk size

def uart_receive_thread(ser, receive_callback):
    while True:
        try:
            data = ser.read(ser.in_waiting or 1)
            if data:
                receive_callback(data)
        except Exception as e:
            print(f"UART receive error: {e}")

def handle_received_data(data):
    print(f"data: {data.hex()}")
    if data.startswith(b'\x9E\x01\xFA'):
        print("Received a factory command!")

def main():
    # COM port configuration
    com_port = 'COM3'  # Change to your COM port
    baud_rate = 115200  # Change as needed

    # File path and address configuration
    mbrec_file_path = 'mbrec.bin'  # Path to your bin file
    mbrec_start_address = 0x00001000
    app_file_path = 'app.bin'  # Path to your bin file
    app_start_address = 0x0003B800 #0x00039600
    chunk_size = 128
    
    # Open the serial port
    ser = serial.Serial(com_port, baud_rate, timeout=1)
    try:
        # Start UART receive thread
        receive_thread = threading.Thread(target=uart_receive_thread, args=(ser, handle_received_data))
        receive_thread.daemon = True  # Configure as daemon thread
        receive_thread.start()

        # 0 File name and size
        fileOverwrite(mbrec_file_path)

        print(f"Step 0, file name and size!!!")
        mbrec_file_name = os.path.basename(mbrec_file_path)
        mbrec_file_size = os.path.getsize(mbrec_file_path)
        mbrec_file_crc = calculate_crc32(mbrec_file_path)
        print(f"mbrec File name: {mbrec_file_name}")
        print(f"mbrec File size: {mbrec_file_size}--{hex(mbrec_file_size)}")
        print(f"mbrec File crc: {mbrec_file_crc}--{hex(mbrec_file_crc)}")
        print(f"mbrec Start address: {mbrec_start_address}--{hex(mbrec_start_address)}")

        app_file_name = os.path.basename(app_file_path)
        app_file_size = os.path.getsize(app_file_path)
        app_file_crc = calculate_crc32(app_file_path)
        print(f"app File name: {app_file_name}")
        print(f"app File size: {app_file_size}--{hex(app_file_size)}")
        print(f"app File crc: {app_file_crc}--{hex(app_file_crc)}")
        print(f"app Start address: {app_start_address}--{hex(app_start_address)}")

        # 1 First enter factory mode
        print(f"Step 1, enter test mode!!!")
        send_factory_cmd(ser)
        send_get_version_cmd(ser)
        send_get_partition_cmd(ser)

        # 2 Erase target app area
        print(f"Step 2, erase target app area!!!")
        send_erase_cmd(ser, 0x9E01FAA4, app_file_size, app_start_address)

        # 3 Send app TLV packets
        print(f"Step 3, send app!!!")
        send_tlv_packets(ser, 0x9E01FAA2, chunk_size, app_start_address, app_file_path)
        time.sleep(0.5)

        # 4 Verify app
        print(f"Step 4, verify app!!!")
        send_verify_cmd(ser, 0x9E01FAA3, app_file_size, app_start_address, app_file_crc)
        time.sleep(0.5)

        # 5 Erase target mbrec area
        print(f"Step 5, erase target mbrec area!!!")
        send_erase_cmd(ser, 0x9E01FAA4, mbrec_file_size, mbrec_start_address)

        # 6 Send mbrec TLV packets
        print(f"Step 6, send mbrec!!!")
        send_tlv_packets(ser, 0x9E01FAA2, chunk_size, mbrec_start_address, mbrec_file_path)
        time.sleep(0.5)

        # 7 Verify mbrec
        print(f"Step 7, verify mbrec!!!")
        send_verify_cmd(ser, 0x9E01FAA3, mbrec_file_size, mbrec_start_address, mbrec_file_crc)

        # 8 Erase current bootloader
        print(f"Step 8, Erase current bootloader!!!")
        mbrec_start_address = 0x00000000
        #send_erase_cmd(ser, 0x9E01FAA4, mbrec_file_size, mbrec_start_address)

        # 9 Reset/reboot
        print(f"Step 9, Reboot!!!")
        #send_reset_cmd(ser)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial port
        receive_thread.stop()
        ser.close()

if __name__ == "__main__":
    main()