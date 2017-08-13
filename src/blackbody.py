import re
from telnetlib import Telnet

class Blackbody():
    """A wrapper and Python interface for a blackbody emitter over telnet."""

    def __init__(self, addr="192.168.200.161", port=7788, timeout=1):
        """Establish a telnet connection to a blackbody source.
            :param addr: IP address of the blackbody.
            :param port: Port over which to talk to the blackbody.
            :type addr: String
            :type port: int
        """
        self.setpoint = 0.0
        try:
            self.tn = Telnet(addr, port, timeout)
        except Exception, e:
            print 'Unable to connect.\n%s' % e # view com ports
            self.tn = None

    def set_temperature(self, setpoint):
        """Set an absolute temperature setpoint for the blackbody to reach. The controller takes a nontrivial amount of time to saturate before actually reaching this setpoint.
            :param setpoint: Temperature in Celsius.
            :type setpoint: float
            :returns: True if the setpoint was successfully set; False otherwise.
            :rtype: bool
        """
        self.tn.write('DA%f\r\n' % setpoint)
        self.setpoint = setpoint
        if self.read_until(timeout=self.timeout):
            return False
        return True

    def get_temperature(self):
        """Get the current absolute temperature (not its setpoint) of the blackbody.
            :returns: Current absolute surface temperature in Celsius.
            :rtype: float
        """
        self.tn.write('M2\r\n')
        response = self.read_until(timeout=self.timeout)
        
