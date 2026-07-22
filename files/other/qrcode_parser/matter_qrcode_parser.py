#!/usr/bin/env python3
import argparse
import enum
from bitarray import bitarray
from stdnum.verhoeff import calc_check_digit
import Base38

# See section 5.1.4.1 Manual Pairing Code in the Matter specification v1.0
MANUAL_DISCRIMINATOR_LEN = 4
PINCODE_LEN = 27

MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_LEN = 2
MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_POS = 0
MANUAL_CHUNK1_VID_PID_PRESENT_BIT_POS = MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_POS + MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_LEN
MANUAL_CHUNK1_LEN = 1

MANUAL_CHUNK2_DISCRIMINATOR_LSBITS_LEN = 2
MANUAL_CHUNK2_PINCODE_LSBITS_LEN = 14
MANUAL_CHUNK2_PINCODE_LSBITS_POS = 0
MANUAL_CHUNK2_DISCRIMINATOR_LSBITS_POS = MANUAL_CHUNK2_PINCODE_LSBITS_POS + MANUAL_CHUNK2_PINCODE_LSBITS_LEN
MANUAL_CHUNK2_LEN = 5

MANUAL_CHUNK3_PINCODE_MSBITS_LEN = 13
MANUAL_CHUNK3_PINCODE_MSBITS_POS = 0
MANUAL_CHUNK3_LEN = 4

MANUAL_VID_LEN = 5
MANUAL_PID_LEN = 5

# See section 5.1.3. QR Code in the Matter specification v1.0
QRCODE_VERSION_LEN = 3
QRCODE_DISCRIMINATOR_LEN = 12
QRCODE_VID_LEN = 16
QRCODE_PID_LEN = 16
QRCODE_COMMISSIONING_FLOW_LEN = 2
QRCODE_DISCOVERY_CAP_BITMASK_LEN = 8
QRCODE_PADDING_LEN = 4
QRCODE_VERSION = 0
QRCODE_PADDING = 0

INVALID_PASSCODES = [00000000, 11111111, 22222222, 33333333, 44444444, 55555555,
                     66666666, 77777777, 88888888, 99999999, 12345678, 87654321]


class CommissioningFlow(enum.IntEnum):
    Standard = 0,
    UserIntent = 1,
    Custom = 2


class SetupPayloadGenerator:
    def __init__(self, discriminator, pincode, rendezvous=4, flow=CommissioningFlow.Standard, vid=0, pid=0):
        self.long_discriminator = discriminator
        self.short_discriminator = discriminator >> 8
        self.pincode = pincode
        self.rendezvous = rendezvous
        self.flow = flow
        self.vid = vid
        self.pid = pid

    def manual_chunk1(self):
        discriminator_shift = (MANUAL_DISCRIMINATOR_LEN - MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_LEN)
        discriminator_mask = (1 << MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_LEN) - 1
        discriminator_chunk = (self.short_discriminator >> discriminator_shift) & discriminator_mask
        vid_pid_present_flag = 0 if self.flow == CommissioningFlow.Standard else 1
        return (discriminator_chunk << MANUAL_CHUNK1_DISCRIMINATOR_MSBITS_POS) | (vid_pid_present_flag << MANUAL_CHUNK1_VID_PID_PRESENT_BIT_POS)

    def manual_chunk2(self):
        discriminator_mask = (1 << MANUAL_CHUNK2_DISCRIMINATOR_LSBITS_LEN) - 1
        pincode_mask = (1 << MANUAL_CHUNK2_PINCODE_LSBITS_LEN) - 1
        discriminator_chunk = self.short_discriminator & discriminator_mask
        return ((self.pincode & pincode_mask) << MANUAL_CHUNK2_PINCODE_LSBITS_POS) | (discriminator_chunk << MANUAL_CHUNK2_DISCRIMINATOR_LSBITS_POS)

    def manual_chunk3(self):
        pincode_shift = PINCODE_LEN - MANUAL_CHUNK3_PINCODE_MSBITS_LEN
        pincode_mask = (1 << MANUAL_CHUNK3_PINCODE_MSBITS_LEN) - 1
        return ((self.pincode >> pincode_shift) & pincode_mask) << MANUAL_CHUNK3_PINCODE_MSBITS_POS

    def generate_manualcode(self):
        payload = str(self.manual_chunk1()).zfill(MANUAL_CHUNK1_LEN)
        payload += str(self.manual_chunk2()).zfill(MANUAL_CHUNK2_LEN)
        payload += str(self.manual_chunk3()).zfill(MANUAL_CHUNK3_LEN)

        if self.flow != CommissioningFlow.Standard:
            payload += str(self.vid).zfill(MANUAL_VID_LEN)
            payload += str(self.pid).zfill(MANUAL_PID_LEN)

        payload += calc_check_digit(payload)
        return payload

class SetupPayloadParser:
    def __init__(self) -> None:
        self.version = 0
        self.long_discriminator = None
        self.short_discriminator = None
        self.pincode = 0
        self.rendezvous = 0
        self.flow = 0
        self.vid = 0
        self.pid = 0

    def __str__(self) -> str:
        '''
        Version:             0
        VendorID:            65521
        ProductID:           32773
        Custom flow:         0    (STANDARD)
        Discovery Bitmask:   0x02 (BLE)
        Long discriminator:  3840   (0xf00)
        Passcode:            20202021
        '''
        custom_flow_str = '???'
        if self.flow == CommissioningFlow.Standard:
            custom_flow_str = 'STANDARD'
        elif self.flow == CommissioningFlow.UserIntent:
            custom_flow_str = 'USER ACTION REQUIRED'
        elif self.flow == CommissioningFlow.Custom:
            custom_flow_str = 'CUSTOM'

        rendezvous_bitmap_str = ''
        if self.rendezvous == 0:
            rendezvous_bitmap_str = 'NONE'
        if self.rendezvous & 0x01:
            rendezvous_bitmap_str += 'Soft-AP'
        if self.rendezvous & 0x02:
            if len(rendezvous_bitmap_str) > 0:
                rendezvous_bitmap_str += ', '
            rendezvous_bitmap_str += 'BLE'
        if self.rendezvous & 0x04:
            if len(rendezvous_bitmap_str) > 0:
                rendezvous_bitmap_str += ', '
            rendezvous_bitmap_str += 'On IP network'
        if self.rendezvous & 0x10:
            if len(rendezvous_bitmap_str) > 0:
                rendezvous_bitmap_str += ', '
            rendezvous_bitmap_str += 'NFC'


        text =  "Version:             {}\n".format(self.version)
        text += "VendorID:            {} (0x{:X})\n".format(self.vid, self.vid)
        text += "ProductID:           {} (0x{:X})\n".format(self.pid, self.pid)
        text += "Custom flow:         {}    ({})\n".format(self.flow, custom_flow_str)
        text += "Discovery Bitmask:   0x{:X}    ({})\n".format(self.rendezvous, rendezvous_bitmap_str)
        if self.long_discriminator != None:
            text += "Long discriminator:  {}   (0x{:X})\n".format(self.long_discriminator, self.long_discriminator)
        elif self.short_discriminator != None:
            text += "Short discriminator: {}   (0x{:X})\n".format(self.short_discriminator, self.short_discriminator)
        text += "Passcode:            {}\n".format(self.pincode)
    
        setuppayload = SetupPayloadGenerator(self.long_discriminator, self.pincode, self.rendezvous,
                                         CommissioningFlow(self.flow), self.vid, self.pid)
        manualcode = setuppayload.generate_manualcode()
        text += "ManualCode:          {}\n".format(self.manualcode_to_434_format(manualcode))

        return text
        
    @staticmethod
    def manualcode_to_434_format(manualcode:str) -> str:
        if len(manualcode) == 11:
            return manualcode[0:4] + '-' + manualcode[4:7] + '-' + manualcode[7:]
        elif len(manualcode) == 21:
            return manualcode[0:4] + '-' + manualcode[4:7] + '-' + manualcode[7:11] + '\n' + manualcode[11:15] + '-' + manualcode[15:18] + '-' + manualcode[18:20]  + '-' + manualcode[20:] 
        else:
            return None
            
    
    def bitstr_to_int(self, bits:str) -> int:
        ba = bitarray(bits.zfill(32))
        ba_bytes = ba.tobytes()
        result = int.from_bytes(ba_bytes, "big")
        return result


    def parse_qrcode(self, qrcode:str) -> bool:
        if qrcode.startswith('MT:') == False:
            return False
        
        # strip "MT:" prefix
        qrcode = qrcode[3:]

        bytes = Base38.decode(qrcode)
        if bytes == None:
            return False

        bytes.reverse()
        qrcode_bit_string = ''
        for i in bytes:
            qrcode_bit_string += format(i, '08b')
        
        #print(qrcode_bit_string)
        offset = len(qrcode_bit_string)

        bits_version = qrcode_bit_string[offset-QRCODE_VERSION_LEN:offset]
        self.version = self.bitstr_to_int(bits_version)
        offset -= QRCODE_VERSION_LEN
        if self.version != QRCODE_VERSION:
            print("qrcode version error")
            return False
        
        bits_vid = qrcode_bit_string[offset-QRCODE_VID_LEN:offset]
        self.vid = self.bitstr_to_int(bits_vid)
        offset -= QRCODE_VID_LEN
        
        bits_pid = qrcode_bit_string[offset-QRCODE_PID_LEN:offset]
        self.pid = self.bitstr_to_int(bits_pid)
        offset -= QRCODE_PID_LEN
        
        bits_comm_flow = qrcode_bit_string[offset-QRCODE_COMMISSIONING_FLOW_LEN:offset]
        self.flow = self.bitstr_to_int(bits_comm_flow)
        offset -= QRCODE_COMMISSIONING_FLOW_LEN
        
        bits_rendezvous = qrcode_bit_string[offset-QRCODE_DISCOVERY_CAP_BITMASK_LEN:offset]
        self.rendezvous = self.bitstr_to_int(bits_rendezvous)
        offset -= QRCODE_DISCOVERY_CAP_BITMASK_LEN
        
        bits_discrimator = qrcode_bit_string[offset-QRCODE_DISCRIMINATOR_LEN:offset]
        self.long_discriminator = self.bitstr_to_int(bits_discrimator)
        offset -= QRCODE_DISCRIMINATOR_LEN
        
        bits_pincode = qrcode_bit_string[offset-PINCODE_LEN:offset]
        self.pincode = self.bitstr_to_int(bits_pincode)
        offset -= PINCODE_LEN
        
        bits_padding = qrcode_bit_string[offset-QRCODE_PADDING_LEN:offset]
        self.padding = self.bitstr_to_int(bits_padding)
        offset -= QRCODE_PADDING_LEN
        if self.padding != QRCODE_PADDING:
            print("qrcode padding error")
            return False

        return validate_args(self.vid, self.pid, self.long_discriminator, self.pincode, self.rendezvous)


def validate_args(vendor_id:int, product_id:int, discriminator:int, passcode:int, discovery_cap_bitmask:int):
    def check_int_range(value, min_value, max_value, name):
        if value and ((value < min_value) or (value > max_value)):
            print('{} is out of range, should be in range from {} to {}'.format(name, min_value, max_value))
            return False
        return True

    if ((passcode < 0x0000001 or passcode > 0x5F5E0FE) or (passcode in INVALID_PASSCODES)):
        print('Invalid passcode:' + str(passcode))
        return False

    if not check_int_range(discriminator, 0x0000, 0x0FFF, 'Discriminator'):
        return False
    if not check_int_range(product_id, 0x0000, 0xFFFF, 'Product id'):
        return False
    if not check_int_range(vendor_id, 0x0000, 0xFFFF, 'Vendor id'):
        return False
    if not check_int_range(discovery_cap_bitmask, 0x0001, 0x00FF, 'Discovery Capability Mask'):
        return False
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Matter QRCode Parser')
    parser.add_argument('--qrcode', type=str, required=True,
                              help='The matter qrcode for pairing, start with MT:')
    args = parser.parse_args()
    
    dec = SetupPayloadParser()
    dec.parse_qrcode(args.qrcode)
    print(dec)

