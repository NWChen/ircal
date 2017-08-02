from serial import Serial

class FakeSerial(Serial):
    """A mock class for serial device behavior."""

    def __init__(self, port)
        """Create a mock serial object.
            :param port: Serial port, we don't really care what format.
            :type port: String
        """
        self.port = port

    def readline(self):
        """Provide a mock response from the serial object.
            :returns: Fake response corresponding to the input query specified by a write().
            :rtype: String
        """
        pass

    def write(self, query):
        """Accept a query and generate potential responses, to be consumed in readline().
            :param query: Input string usually sent to a serial object.
            :type query: String
        """
        pass

    def is_open(self):
        """Describe whether this serial connection is open."""
        pass 
