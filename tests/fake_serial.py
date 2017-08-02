from serial import Serial

class Responder():
    """Generates mock KT/CT output given environment information."""

    def __init__(self):
        
        self.bkgd_temp = 25         
        self.query = []

    def _process_query(self, query):
        self.query.append(query[:3])
        self.query.extend(query.split()[1:]) 

    def respond():
        

class FakeSerial(Serial):
    """A mock class for serial device behavior."""

    def __init__(self, port)
        """Create a mock serial object.
            :param port: Serial port, we don't really care what format.
            :type port: String
        """
        self.name = self.port = port
        self.baudrate = 9600
        self.responder = Responder() # Delegate generating KT/CT-like responses to a separate object. Whenever mock KT/CT command output is desired, a call to self.responder should be made.

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
        
        
    
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
