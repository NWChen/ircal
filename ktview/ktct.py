#!/usr/bin/env python
import sys
import serial
from random import randint

class Ktct(object):
    """ Encapsulates a KT/CT serial driver. The only functionality included is requesting absolute temperature. """

    def __init__(self, port=None, debug=False):
        """ A valid USB port is expected; the driver will terminate otherwise. """
        if debug:
            self.debug = True
        else:
            try:
                self.ser = serial.Serial(port, timeout=0)
            except serial.SerialException:
                self._die(port + " is not connected. Please try a different USB port.")
            if self.ser is None:
                self._die("Serial connection detected but failed. Please try a different USB port.")

    def _die(self, message):
        sys.exit(message)

    def read(self, numeric=False):
        """ Reads output from KT/CT output buffer. Returns the full string, or a number if requested. """
        if self.debug:
            return randint(0, 100)
        out = self.ser.readline()
        if len(out) < 1:
            return ""
        if numeric:
            out = float(filter(str.isdigit, out))
        return out

    def ask(self):
        """ Requests temperature from KT/CT. Since there can be significant latency between sending command and receiving temperature, this method does not retrieve any data. Instead, call ktct_read(). """
        if self.debug:
            return
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write("TEMP\r\n")
