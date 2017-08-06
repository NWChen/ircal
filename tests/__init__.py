import sys
import test_fake_serial
import test_fake_telnet
import unittest

if __name__ == '__main__':
    try:
        all_tests = []
        all_tests.extend(unittest.TestSuite([test_fake_serial.get_tests()]))
        all_tests.extend(unittest.TestSuite([test_fake_telnet.get_tests()]))
        
        for test in all_tests:
            unittest.TextTestRunner().run(test)
        sys.exit(0)
    except Exception:
        sys.exit(1)
