import sys
try:
    assert('Linux' in sys.platform),"This runs only on Linux"
except:
    print("This is windows")

try:
    with open("demo.log") as file:
        read_data=file.read()
except FileNotFoundError as ff:
    print(ff)