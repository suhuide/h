PS C:\Users\huide\Desktop\qrcode_parser> python.exe .\matter_qrcode_parser.py MT:K2CA0YDG158HO34RB10
Traceback (most recent call last):
  File "C:\Users\huide\Desktop\qrcode_parser\matter_qrcode_parser.py", line 4, in <module>
    from bitarray import bitarray
ModuleNotFoundError: No module named 'bitarray'
PS C:\Users\huide\Desktop\qrcode_parser> python.exe -m pip install bitarray
Collecting bitarray
  Downloading bitarray-3.9.0-cp310-cp310-win_amd64.whl.metadata (36 kB)
Downloading bitarray-3.9.0-cp310-cp310-win_amd64.whl (152 kB)
Installing collected packages: bitarray
Successfully installed bitarray-3.9.0

[notice] A new release of pip is available: 26.1.1 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
PS C:\Users\huide\Desktop\qrcode_parser> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\siliconlabs\simplicitystudio\v5\developer\adapter_packs\python\lib\site-packages (26.1.1)
Collecting pip
  Downloading pip-26.1.2-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.1.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 9.0 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 26.1.1
    Uninstalling pip-26.1.1:
      Successfully uninstalled pip-26.1.1
  WARNING: The scripts pip.exe, pip3.10.exe and pip3.exe are installed in 'C:\SiliconLabs\SimplicityStudio\v5\developer\adapter_packs\python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-26.1.2
PS C:\Users\huide\Desktop\qrcode_parser> python.exe .\matter_qrcode_parser.py MT:K2CA0YDG158HO34RB10
Traceback (most recent call last):
  File "C:\Users\huide\Desktop\qrcode_parser\matter_qrcode_parser.py", line 5, in <module>
    from stdnum.verhoeff import calc_check_digit
ModuleNotFoundError: No module named 'stdnum'
PS C:\Users\huide\Desktop\qrcode_parser> python.exe -m pip install stdnum
ERROR: Could not find a version that satisfies the requirement stdnum (from versions: none)
ERROR: No matching distribution found for stdnum
PS C:\Users\huide\Desktop\qrcode_parser> python.exe -m pip install python-stdnum
Collecting python-stdnum
  Downloading python_stdnum-2.2-py3-none-any.whl.metadata (19 kB)
Downloading python_stdnum-2.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 1.5 MB/s  0:00:00
Installing collected packages: python-stdnum
Successfully installed python-stdnum-2.2
PS C:\Users\huide\Desktop\qrcode_parser> python.exe .\matter_qrcode_parser.py MT:K2CA0YDG158HO34RB10
usage: matter_qrcode_parser.py [-h] --qrcode QRCODE
matter_qrcode_parser.py: error: the following arguments are required: --qrcode
PS C:\Users\huide\Desktop\qrcode_parser> python.exe .\matter_qrcode_parser.py --qrcode MT:K2CA0YDG158HO34RB10
Version:             0
VendorID:            5232 (0x1470)
ProductID:           65281 (0xFF01)
Custom flow:         0    (STANDARD)
Discovery Bitmask:   0x2    (BLE)
Long discriminator:  2485   (0x9B5)
Passcode:            61915432
ManualCode:          2166-803-7798