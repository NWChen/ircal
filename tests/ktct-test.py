#!/usr/bin/env python
import serial
import sys

sys.path.append('../ktview')
import ktview

PORT = 'loop://'
ser = serial.serial_for_url(PORT, timeout=1)
ktview.ktct_ask_temp(ser)

try:
    assert ktview.ktct_read(ser) == "TEMP\r\n"
except AssertionError:
    print "[ ] FAILED"
else:
    print "[x] PASSED"

ser.close()
