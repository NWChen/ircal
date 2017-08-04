import sys
import test_fake_serial
import unittest
from fake_serial import FakeSerial

if __name__ == '__main__':
    try:
        all_tests = []
        all_tests.append(unittest.TestSuite([test_fake_serial.get_tests()]))
        
        for test in all_tests:
            unittest.TextTestRunner().run(test)
        sys.exit(0)
    except:
        sys.exit(1)
