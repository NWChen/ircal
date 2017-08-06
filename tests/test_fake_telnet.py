import unittest
import threading
import sys
import fake_telnet
import time
from telnetlib import Telnet

class FakeTelnetTestCase(unittest.TestCase):

    def setUp(self):
        addr, port = 'localhost', 9999
        self.t = threading.Thread(target=fake_telnet.start)
        self.t.start()
        self.tn = Telnet(addr, port)
        time.sleep(0.5)
        self.tn.read_very_eager()

    def tearDown(self):
        self.tn.close()

    def test_initialization(self):
        self.tn.write('M2\r\n')
        time.sleep(0.2)
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')
        time.sleep(0.2)
        self.tn.write('M1\r\n')
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')

    def test_temp_change(self):
        self.tn.write('DA32.0\r\n')
        self.tn.write('M1\r\n')
        time.sleep(0.2)
        self.assertEqual(self.tn.read_very_eager(), '32.0\r\n')

def get_tests():
    tests = ['test_initialization', 'test_temp_change']
    return unittest.TestSuite(map(FakeTelnetTestCase, tests))

if __name__ == '__main__':
    sys.exit(unittest.main())
