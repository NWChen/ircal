from serial import Serial, SerialException

class Responder():
    """Generates mock KT/CT output given environment information."""

    def __init__(self):
        self.bkgd_temp = 25         
        self.query = []

    def ask(self, query):
        for token in query:
            if ord(token) > 127: # KT/CT only accepts ASCII characters.
                break
            self.query.append(token)
        else if len(query) <= 40: # KT/CT has a 40-character input buffer.
            return True
        return False

    def respond():
         

class FakeSerial(Serial):
    """Simulates generic serial device behavior."""

    def __init__(self, port, baudrate=9600, timeout=0.2)
        """Create a mock serial object.
            :param port: Serial port, we don't really care what format.
            :type port: String
        """
        self.name = self.port = port
        self.responder = Responder() # Delegate generating KT/CT-like responses to a separate object. Whenever mock KT/CT command output is desired, a call to self.responder should be made.
        self.output_buffer = self.input_buffer = []

    def __getattribute__(self, attr):
        if not self.is_open:
            raise SerialException("Cannot write, serial connection is not open.")
        return object.__getattribute__(self, attr)

    def readline(self):
        """Provide a mock response from the serial object.
            :returns: Fake response corresponding to the input query specified by a write().
            :rtype: String
        """
        try:
            newline = self.output_buffer.index('\n')
            return ''.join(self.output_buffer.pop
        except ValueError:
            sleep(self.timeout)
          

    def write(self, query):
        """Accept a query and generate potential responses, to be consumed in readline().
            :param query: Input string usually sent to a serial object.
            :type query: String
        """
        self.input_buffer.append(query.split(''))
        if self.responder.ask(self.input_buffer):
            self.output_buffer.append(self.responder.respond().split(''))
        else:
            raise SerialException("Invalid input query.")
 
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
