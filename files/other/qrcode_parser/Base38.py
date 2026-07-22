#!/usr/bin/env python3
#
#    Copyright (c) 2022 Project CHIP Authors
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http:#www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# TODO: Implement the decode method

CODES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z', '-', '.']
RADIX = len(CODES)
BASE38_CHARS_NEEDED_IN_CHUNK = [2, 4, 5]
MAX_BYTES_IN_CHUNK = 3

kBogus = 255
# map of base38 charater to numeric value
# subtract 45 from the charater, then index into this array, if possible
decodes = [
        36,     # '-', =45
        37,     # '.', =46
        kBogus, # '/', =47
        0,      # '0', =48
        1,      # '1', =49
        2,      # '2', =50
        3,      # '3', =51
        4,      # '4', =52
        5,      # '5', =53
        6,      # '6', =54
        7,      # '7', =55
        8,      # '8', =56
        9,      # '9', =57
        kBogus, # ':', =58
        kBogus, # ';', =59
        kBogus, # '<', =50
        kBogus, # '=', =61
        kBogus, # '>', =62
        kBogus, # '?', =63
        kBogus, # '@', =64
        10,     # 'A', =65
        11,     # 'B', =66
        12,     # 'C', =67
        13,     # 'D', =68
        14,     # 'E', =69
        15,     # 'F', =70
        16,     # 'G', =71
        17,     # 'H', =72
        18,     # 'I', =73
        19,     # 'J', =74
        20,     # 'K', =75
        21,     # 'L', =76
        22,     # 'M', =77
        23,     # 'N', =78
        24,     # 'O', =79
        25,     # 'P', =80
        26,     # 'Q', =81
        27,     # 'R', =82
        28,     # 'S', =83
        29,     # 'T', =84
        30,     # 'U', =85
        31,     # 'V', =86
        32,     # 'W', =87
        33,     # 'X', =88
        34,     # 'Y', =89
        35]     # 'Z', =90

def decodeChar(c:str) -> int:
    if c < '-' or c > 'Z':
        print("invalid integer value")
        return None
    v = decodes[ord(c) - ord('-')]
    if v == kBogus:
        print("invalid integer value")
        return None
    return v

def encode(bytes):
    total_bytes = len(bytes)
    qrcode = ''

    for i in range(0, total_bytes, MAX_BYTES_IN_CHUNK):
        if (i + MAX_BYTES_IN_CHUNK) > total_bytes:
            bytes_in_chunk = total_bytes - i
        else:
            bytes_in_chunk = MAX_BYTES_IN_CHUNK

        value = 0
        for j in range(i, i + bytes_in_chunk):
            value = value + (bytes[j] << (8 * (j - i)))

        base38_chars_needed = BASE38_CHARS_NEEDED_IN_CHUNK[bytes_in_chunk - 1]
        while base38_chars_needed > 0:
            qrcode += CODES[int(value % RADIX)]
            value = int(value / RADIX)
            base38_chars_needed -= 1

    return qrcode

def decode(qrcode:str) -> bytes:
    result = []
    base38CharactersNumber = len(qrcode)
    decodedBase38Characters = 0

    while base38CharactersNumber > 0:
        if base38CharactersNumber >= BASE38_CHARS_NEEDED_IN_CHUNK[2]:
            base38CharactersInChunk = BASE38_CHARS_NEEDED_IN_CHUNK[2]
            bytesInDecodedChunk     = 3
        elif base38CharactersNumber >= BASE38_CHARS_NEEDED_IN_CHUNK[1]:
            base38CharactersInChunk = BASE38_CHARS_NEEDED_IN_CHUNK[1]
            bytesInDecodedChunk     = 2
        elif base38CharactersNumber >= BASE38_CHARS_NEEDED_IN_CHUNK[0]:
            base38CharactersInChunk = BASE38_CHARS_NEEDED_IN_CHUNK[0]
            bytesInDecodedChunk     = 1
        else:
            print("invalid string length")
            return None
        
        value = 0
        for i in range(base38CharactersInChunk, 0, -1):
            index = decodedBase38Characters + i - 1
            v = decodeChar(qrcode[index])
            if v == None:
                return None
            
            value = value * RADIX +v

        decodedBase38Characters += base38CharactersInChunk
        base38CharactersNumber -= base38CharactersInChunk

        for i in range(bytesInDecodedChunk):
            result.append(value & 0xff)
            value >>= 8

        if value > 0:
            print("encoded value is too big to represent a correct chunk of size 1, 2 or 3 bytes")
            return None
        
    return result