## Read
```c
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000
```
## Parse
```c
commander nvm3 parse nvm3.s37
Parsing file nvm3.s37...
Found NVM3 range: 0x08174000 - 0x0817E000
Using 4096 B as maximum object size, based on given size of NVM3 area.
All NVM3 objects:
    KEY -       TYPE -     SIZE - DATA
0x0ef00 -       Data -     32 B - 34 65 66 34 30 65 39 37 (+ 24 more bytes)
0x0f00b -       Data -      0 B -
0x0f00c -       Data -      0 B -
0x0f00f -       Data -     10 B - 02 90 01 00 01 01 86 00 (+ 2 more bytes)
0x0f0a0 -       Data -     27 B - EF AB 06 00 00 00 01 01 (+ 19 more bytes)
0x4002c -       Data -      6 B - D0 AF 92 21 6C DA
0x40038 -       Data -     32 B - FF FF FF FF FF FF FF FF (+ 24 more bytes)
0x4003c -       Data -      1 B - 01
0x4003f -       Data -      4 B - 04 00 00 00
0x43fff -       Data -     12 B - 00 00 00 00 0D 00 00 00 (+ 4 more bytes)
0x86d1a -       Data -     84 B - 10 5D 17 5E 00 00 00 00 (+ 76 more bytes)
0x86d6d -       Data -     68 B - 10 5D 17 5E 00 00 00 00 (+ 60 more bytes)
0x87200 -       Data -     16 B - 39 41 39 43 45 44 38 42 (+ 8 more bytes)
0x87204 -       Data -     10 B - 32 30 32 36 2D 30 31 2D (+ 2 more bytes)
0x87205 -       Data -     11 B - D0 A4 A8 90 41 E0 83 9E (+ 3 more bytes)
0x87207 -       Data -      2 B - 1F 04
0x87208 -       Data -      4 B - E8 03 00 00
0x87209 -       Data -     24 B - 61 43 73 49 39 56 73 33 (+ 16 more bytes)
0x8720a -       Data -    132 B - 55 34 44 67 32 76 73 79 (+ 124 more bytes)
0x8720b -       Data -      2 B - 15 32
0x8720c -       Data -      2 B - 9A 14
0x8720d -       Data -      4 B - 41 2D 4F 4B
0x8720e -       Data -     18 B - 43 75 72 74 61 69 6E 20 (+ 10 more bytes)
0x8720f -       Data -      4 B - 56 31 2E 30
0x87210 -       Data -     15 B - 6C 61 62 65 6C 20 48 4D (+ 7 more bytes)
0x87211 -       Data -     21 B - 68 74 74 70 73 3A 2F 2F (+ 13 more bytes)
0x87212 -       Data -      9 B - 50 4E 20 4D 54 32 34 30 (+ 1 more bytes)
0x87218 -       Data -      2 B - 01 00
0x8721f -       Data -     32 B - 62 37 65 33 36 36 63 39 (+ 24 more bytes)
0x87220 -       Data -      4 B - 02 00 00 00
0x87221 -       Data -      4 B - 00 E0 17 08
0x87222 -       Data -      4 B - 00 00 00 00
0x87223 -       Data -      4 B - E1 01 00 00
0x87224 -       Data -      4 B - 00 02 00 00
0x87225 -       Data -      4 B - D6 01 00 00
0x87226 -       Data -      4 B - 00 04 00 00
0x87227 -       Data -      4 B - F4 00 00 00
0x87309 -       Data -      4 B - 00 00 00 00
0x8730a -       Data -      2 B - 58 58
0x87318 -       Data -     16 B - 33 36 31 37 37 32 32 41 (+ 8 more bytes)
0x87320 -       Data -      6 B - 00 00 00 00 00 00
0x87321 -       Data -      4 B - 13 00 00 00
0x87403 -       Data -      4 B - 05 00 00 00
0x87500 -       Data -    800 B - C2 26 30 34 E8 99 7C 0A (+ 792 more bytes)
0x87501 -       Data -      7 B - 67 2F 73 75 6D 0F 00
0x87502 -       Data -     14 B - 67 2F 6C 6B 67 74 15 26 (+ 6 more bytes)
0x87503 -       Data -      9 B - 67 2F 67 63 63 58 C1 A4 (+ 1 more bytes)
0x87504 -       Data -      9 B - 67 2F 67 64 63 94 6B 47 (+ 1 more bytes)
0x87505 -       Data -     15 B - 67 2F 69 6D 2F 65 63 00 (+ 7 more bytes)
0x87506 -       Data -     10 B - 67 2F 61 2F 33 2F 38 2F (+ 2 more bytes)
0x87507 -       Data -     10 B - 67 2F 61 2F 34 2F 38 2F (+ 2 more bytes)
0x87508 -       Data -     16 B - 67 2F 61 2F 30 2F 32 62 (+ 8 more bytes)
0x87509 -       Data -     12 B - 67 2F 61 2F 31 2F 31 30 (+ 4 more bytes)
0x8750a -       Data -     12 B - 67 2F 61 2F 32 2F 31 30 (+ 4 more bytes)

NVM3 erase count: 2

DONE
```