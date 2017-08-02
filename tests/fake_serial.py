from serial import Serial, SerialException
from itertools import chain

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
        else:
            if len(query) <= 40: # KT/CT has a 40-character input buffer.
                return True
        return False

    def respond():
        pass 

class FakeSerial():#Serial):
    """Simulates generic serial device behavior."""

    def __init__(self, port, baudrate=9600, timeout=0.2):
        """Create a mock serial object.
            :param port: Serial port, we don't really care what format.
            :type port: String
        """
        self.name = self.port = port
        self.responder = Responder() # Delegate generating KT/CT-like responses to a separate object. Whenever mock KT/CT command output is desired, a call to self.responder should be made.
        self.output_buffer = self.input_buffer = []
        self.is_open = True

    def __getattribute__(self, attr):
        """Checks whether this connection is open prior to any member/function call. This is less invasive than checking for self.is_open in every function call.
        """
        if attr != 'is_open':
            if not self.is_open:
                raise SerialException("Cannot write, serial connection is not open.")
        return object.__getattribute__(self, attr)

    def readline(self):
        """Provide a mock response from the serial object.
            :returns: Fake response corresponding to the input query specified by a write().
            :rtype: String
        """
        tokens = self.output_buffer.split('\n')
        response, self.output_buffer = tokens[0], list(chain.from_iterable(tokens[1]))
        if tokens:
            return tokens
        sleep(timeout) # Just like a real serial connection, block until EOF/EOL or timeout elapsed.

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
