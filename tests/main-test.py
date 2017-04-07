#!/usr/bin/env python
import serial
import sys
import unittest

sys.path.append('../ktview')
import ktview

class TestKtview(unittest.TestCase):

    def test_ktct(self):
        self.ser = serial.serial_for_url('loop://', timeout=1)
        ktview.ktct_ask_temp(self.ser)
        self.assertEqual(ktview.ktct_read(self.ser), "TEMP\r\n")

        

if __name__ == '__main__':
    unittest.main()
    ser.close()
