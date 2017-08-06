import unittest
import threading
import sys
import fake_telnet
import time
from telnetlib import Telnet

t = threading.Thread(target=fake_telnet.start)

class FakeTelnetTestCase(unittest.TestCase):

    def setUp(self):
        self.tn = Telnet() 
        try:
            global t
            t.start()
            self.tn = Telnet('localhost', 9999)
            time.sleep(1)
            self.tn.read_very_eager() 
        except Exception:
            pass
        time.sleep(1)

    def tearDown(self):
        self.tn.close()

    def test_initialization(self):
        self.tn.write('M2\r\n')
        time.sleep(1)
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')
        time.sleep(1)
        self.tn.write('M1\r\n')
        time.sleep(1)
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')

    '''
    def test_temp_change(self):
        self.tn.write('DA32.0\r\n')
        self.tn.write('M1\r\n')
        time.sleep(1)
        self.assertEqual(self.tn.read_very_eager(), '32.0\r\n')
    '''

def get_tests():
    tests = ['test_initialization']#, 'test_temp_change']
    return unittest.TestSuite(map(FakeTelnetTestCase, tests))

if __name__ == '__main__':
    sys.exit(unittest.main())
