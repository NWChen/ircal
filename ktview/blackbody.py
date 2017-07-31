#!/usr/bin/env python
import sys
import string
from random import randint

class Blackbody(object):
    """ Encapsulates a blackbody radiation emitter. """

    def __init__(self, debug=False, timeout=2):
        """ Creates a Blackbody object. Assumes the device is already connected. """
        if debug:
            self.debug = True
        else:
            try:
                ip_addr, port = "192.168.200.161", "7788"
                self.tn = telnetlib.Telnet(ip_addr, port, timeout)
            except Exception:
                self._die("IP  or port not recognized. Please check your connection and try again.")

    def _die(self, message):
        sys.exit(message)

    def read(self, numeric=False):
        """ Reads the output buffer of the blackbody. """
        if self.debug:
            return randint(0, 100)
        response = self.tn.read_very_eager()
        out = ""
        if len(response) >= 1:
            field = "T2="
            i = response.index(field) + len(field)
            response = response[i:response.index("\n", i)]
            out = filter(lambda c: c in string.digits + '.', response)
        if numeric:
            out = float(out)
        return out

    def set(self, setpoint):
        """ Sets an absolute setpoint for the blackbody to reach. You must wait for the controller to saturate before assuming this setpoint has actually been reached.  """
        if self.debug:
            return
        self.tn.write("DA%f\r\n" % setpoint)

    def get(self):
        """ Gets the current absolute temperature of the blackbody. You must call read() after this to retrieve the value. """
        if self.debug:
            return
        self.tn.write("M2\r\n")
