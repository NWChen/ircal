import unittest
import sys
import time
import threading
from subprocess import call
from telnetlib import Telnet

class NonBlockingDaemon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        threading.Thread(target=self._begin_server).start()
        self.shutdown = False

    def _begin_server(self):
        proc = call(["python", "fake_telnet.py"])
        while not self.shutdown:
            pass
        proc.terminate()
        sys.exit(0)

class FakeTelnetTestCase(unittest.TestCase):

    def setUp(self):
        self.nbd = NonBlockingDaemon()
        time.sleep(1)
        self.tn = Telnet() 
        try:
            self.tn = Telnet('localhost', 9999)
            time.sleep(1)
            self.tn.read_very_eager() 
        except Exception as e:
            print 'unreasonable connection attempt'
            print e

    def tearDown(self):
        self.tn.close()
        self.nbd.shutdown = True

    def test_initialization(self):
        self.tn.write('M2\r\n')
        time.sleep(1)
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')
        time.sleep(1)
        self.tn.write('M1\r\n')
        time.sleep(1)
        self.assertEqual(self.tn.read_very_eager(), '25.0\r\n')

    #def test_temp_change(self):
    #    self.tn.write('DA32.0\r\n')
    #    self.tn.write('M1\r\n')
    #    time.sleep(1)
    #    self.assertEqual(self.tn.read_very_eager(), '32.0\r\n')

def get_tests():
    tests = ['test_initialization']#, 'test_temp_change']
    return unittest.TestSuite(map(FakeTelnetTestCase, tests))

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
