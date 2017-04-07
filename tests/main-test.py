#!/usr/bin/env python
import serial
import string
import sys
import telnetlib
import unittest

sys.path.append('../ktview')
import ktview

class MockTelnet(object):

    def write(self, q):
        if "DA" in q:
            self._buf = filter(lambda c : c in string.digits + '.', q)

    def read_very_eager(self):
        return "T2=" + self._buf + "\r\n"

class TestKtview(unittest.TestCase):

    def setUp(self):
        self.ser = serial.serial_for_url('loop://', timeout=0)
        self.tn = MockTelnet()

    def tearDown(self):
        self.ser.close()

    def test_ktct(self):
        ktview.ktct_ask_temp(self.ser)
        self.assertEqual(ktview.ktct_read(self.ser), "TEMP\r\n")

    def test_bb(self):
        temp = 25
        ktview.bb_set(self.tn, temp)
        ktview.bb_get(self.tn)
        self.assertEqual(ktview.bb_read(self.tn), temp)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKtview)
    unittest.TextTestRunner(verbosity=2).run(suite)
