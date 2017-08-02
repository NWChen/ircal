import sys
from fake_serial import FakeSerial

def main():
    fs = FakeSerial(1) 
    return 0

if __name__ == '__main__':
    sys.exit(main())
