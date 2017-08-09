from telnetlib import Telnet

class Blackbody():
    """A wrapper and Python interface for a blackbody emitter over telnet."""

    def __init__(self, addr="192.168.200.161", port=7788):
        """Establish a telnet connection to a blackbody source.
            :param addr: IP address of the blackbody.
            :param port: Port over which to talk to the blackbody.
            :type addr: String
            :type port: int
        """
        try:
            self.tn = Telnet(addr, port)  
        except Exception, e:
            print 'Unable to connect.\n%s' % e # view com ports

    def set_temperature(self, setpoint):
        """Set an absolute temperature setpoint for the blackbody to reach. The controller takes a nontrivial amount of time to saturate before actually reaching this setpoint.
            :param setpoint: Temperature in Celsius.
            :type setpoint: float
            :returns: True if the setpoint was successfully set; False otherwise.
            :rtype: bool
        """
        pass

    def get_temperature(self):
        """Get the current absolute temperature (not its setpoint) of the blackbody.
            :returns: Current absolute surface temperature in Celsius.
            :rtype: float
        """
        pass
