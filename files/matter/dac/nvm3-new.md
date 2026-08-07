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
0x0ef00 -       Data -     32 B - 31 37 34 36 31 66 34 65 (+ 24 more bytes)
0x0f00f -       Data -     10 B - 02 90 01 00 01 01 86 00 (+ 2 more bytes)
0x0f0a0 -       Data -     27 B - EF AB 06 00 00 00 01 01 (+ 19 more bytes)
0x20100 -       Data -    107 B - 0E 08 00 00 66 87 99 D3 (+ 99 more bytes)
0x20300 -       Data -     38 B - 02 04 09 B8 11 00 00 00 (+ 30 more bytes)
0x20400 -       Data -     10 B - 46 82 F0 28 1B D4 78 91 (+ 2 more bytes)
0x20700 -       Data -     32 B - F7 92 74 CC 4A 2B 83 78 (+ 24 more bytes)
0x4003f -       Data -      4 B - 04 00 00 00
0x86d1a -       Data -     84 B - 10 5D 17 5E 00 00 00 00 (+ 76 more bytes)
0x86d28 -       Data -     84 B - 10 5D 17 5E 00 00 00 00 (+ 76 more bytes)
0x86d2a -       Data -     84 B - 10 5D 17 5E 00 00 00 00 (+ 76 more bytes)
0x86d41 -       Data -     84 B - 10 5D 17 5E 00 00 00 00 (+ 76 more bytes)
0x86d58 -       Data -     68 B - 10 5D 17 5E 00 00 00 00 (+ 60 more bytes)
0x86d6d -       Data -     68 B - 10 5D 17 5E 00 00 00 00 (+ 60 more bytes)
0x86d77 -       Data -     68 B - 10 5D 17 5E 00 00 00 00 (+ 60 more bytes)
0x87200 -       Data -     16 B - 30 43 31 37 37 37 44 36 (+ 8 more bytes)
0x87204 -       Data -     10 B - 32 30 32 36 2D 30 33 2D (+ 2 more bytes)
0x87205 -       Data -     11 B - D0 A4 A8 90 41 80 EB DA (+ 3 more bytes)
0x87207 -       Data -      2 B - 5C 07
0x87208 -       Data -      4 B - E8 03 00 00
0x87209 -       Data -     24 B - 6E 6F 46 41 61 48 5A 46 (+ 16 more bytes)
0x8720a -       Data -    132 B - 48 36 61 77 5A 79 36 6A (+ 124 more bytes)
0x8720b -       Data -      2 B - 15 32
0x8720c -       Data -      2 B - 9A 14
0x8720d -       Data -      4 B - 41 2D 4F 4B
0x8720e -       Data -     18 B - 43 75 72 74 61 69 6E 20 (+ 10 more bytes)
0x8720f -       Data -      4 B - 56 31 2E 30
0x87211 -       Data -     21 B - 68 74 74 70 73 3A 2F 2F (+ 13 more bytes)
0x87218 -       Data -      2 B - 01 00
0x8721f -       Data -     32 B - 65 37 37 61 34 37 62 62 (+ 24 more bytes)
0x87220 -       Data -      4 B - 02 00 00 00
0x87221 -       Data -      4 B - 00 E0 17 08
0x87222 -       Data -      4 B - 00 10 00 00
0x87223 -       Data -      4 B - E0 01 00 00
0x87224 -       Data -      4 B - 00 12 00 00
0x87225 -       Data -      4 B - D6 01 00 00
0x87226 -       Data -      4 B - 00 14 00 00
0x87227 -       Data -      4 B - F5 00 00 00
0x87309 -       Data -      4 B - 00 00 00 00
0x8730a -       Data -      2 B - 43 4E
0x87318 -       Data -     16 B - 33 34 39 33 46 31 32 43 (+ 8 more bytes)
0x87320 -       Data -      6 B - 01 02 00 00 00 00
0x87321 -       Data -      4 B - 05 00 00 00
0x87403 -       Data -      4 B - 05 00 00 00
0x87500 -       Data -    800 B - C2 26 30 34 E8 99 7C 0A (+ 792 more bytes)
0x87501 -       Data -      7 B - 67 2F 73 75 6D 0F 00
0x87502 -       Data -     14 B - 67 2F 6C 6B 67 74 15 26 (+ 6 more bytes)
0x87503 -       Data -      9 B - 67 2F 67 63 63 CF 5E 33 (+ 1 more bytes)
0x87504 -       Data -      9 B - 67 2F 67 64 63 1F E0 A6 (+ 1 more bytes)
0x87505 -       Data -     15 B - 67 2F 69 6D 2F 65 63 00 (+ 7 more bytes)
0x87506 -       Data -     10 B - 67 2F 61 2F 33 2F 38 2F (+ 2 more bytes)
0x87507 -       Data -     10 B - 67 2F 61 2F 34 2F 38 2F (+ 2 more bytes)
0x87508 -       Data -     16 B - 67 2F 61 2F 30 2F 32 62 (+ 8 more bytes)
0x87509 -       Data -     12 B - 67 2F 61 2F 31 2F 31 30 (+ 4 more bytes)
0x8750a -       Data -     12 B - 67 2F 61 2F 32 2F 31 30 (+ 4 more bytes)
0x8750b -       Data -    104 B - 66 2F 31 2F 6B 2F 30 15 (+ 96 more bytes)
0x8750c -       Data -     13 B - 67 2F 67 66 6C 15 24 01 (+ 5 more bytes)
0x8750d -       Data -     28 B - 66 2F 31 2F 67 15 24 01 (+ 20 more bytes)
0x8750e -       Data -     37 B - 66 2F 31 2F 61 63 2F 30 (+ 29 more bytes)
0x8750f -       Data -     32 B - 66 2F 31 2F 61 63 2F 30 (+ 24 more bytes)
0x87510 -       Data -     93 B - 66 2F 31 2F 73 2F 30 30 (+ 85 more bytes)
0x87511 -       Data -     39 B - 67 2F 73 2F 32 79 50 54 (+ 31 more bytes)
0x87512 -       Data -     44 B - 67 2F 73 72 69 16 15 24 (+ 36 more bytes)
0x87514 -       Data -     23 B - 66 2F 31 2F 6D 15 25 00 (+ 15 more bytes)
0x87515 -       Data -    258 B - 66 2F 31 2F 6E 15 30 01 (+ 250 more bytes)
0x87516 -       Data -    251 B - 66 2F 31 2F 72 15 30 01 (+ 243 more bytes)
0x87517 -       Data -     18 B - 67 2F 66 69 64 78 15 24 (+ 10 more bytes)
0x87518 -       Data -    104 B - 66 2F 32 2F 6B 2F 30 15 (+ 96 more bytes)
0x87519 -       Data -     28 B - 66 2F 32 2F 67 15 24 01 (+ 20 more bytes)
0x8751a -       Data -     32 B - 66 2F 32 2F 61 63 2F 30 (+ 24 more bytes)
0x8751b -       Data -     93 B - 66 2F 32 2F 73 2F 35 38 (+ 85 more bytes)
0x8751c -       Data -     43 B - 67 2F 73 2F 4F 5A 44 2B (+ 35 more bytes)
0x8751d -       Data -     93 B - 66 2F 31 2F 73 2F 30 30 (+ 85 more bytes)
0x8751e -       Data -     14 B - 66 2F 32 2F 6D 15 25 00 (+ 6 more bytes)
0x8751f -       Data -    262 B - 66 2F 32 2F 6E 15 30 01 (+ 254 more bytes)
0x87520 -       Data -    259 B - 66 2F 32 2F 72 15 30 01 (+ 251 more bytes)
0x87521 -       Data -     39 B - 67 2F 73 2F 36 56 51 57 (+ 31 more bytes)
0x87522 -       Data -     79 B - 67 2F 73 75 2F 31 15 26 (+ 71 more bytes)
0x87523 -       Data -     22 B - 67 2F 6F 2F 64 70 16 15 (+ 14 more bytes)

NVM3 erase count: 1

DONE
```