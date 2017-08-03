import re
from time import sleep
from functools import wraps
from random import randint
from itertools import chain
from serial import Serial, SerialException

class Responder():
    """Generates mock KT/CT output given environment information."""

    def __init__(self):
        """Create a mock KT/CT response generator.
        """
        self.device_values = {
            'temp': 25.0,
            'rad': 0.0,
            'unit': 'C',
            'calibration_factor': 2.0,
        }
        self.language = {
            '^CAL ?$': (lambda settings, device_values: device_values['calibration_factor']),
            '^CAL (\d+[.]\d*))$': (lambda settings, device_values: device_values.update({'calibration_factor': float(settings.group()[0])})),
            '^TEMP$': (lambda settings, device_values: device_values['temp']),
            '^RAD$': (lambda settings, device_values: device_values['rad']),
            '^UNIT ?$': (lambda settings, device_values: device_values['unit']),
            '^UNIT ([K|C|F])$': (lambda settings, device_values: device_values.update({'unit': settings.group()[0]}))
        }
        self.query = []

    def _timeout(self):
        """Simulates latency in serial device response.
            :returns: True if the message was delivered, False otherwise.
            :rtype: bool
        """
        sleep(randint(50, 500)/1000.0)
        failure_guess = randint(0, 10) # To be cautious, assume 1 in 10 serial messages will fail to deliver.
        return failure_guess != 10

    def ask(self, query):
        """Simulates receiving and processing an input query.
            :returns: True if the query was accepted, False if an error was found.
            :rtype: bool
        """
        if self._timeout():
            for token in query:
                if ord(token) > 127: # KT/CT only accepts ASCII characters.
                    break
                self.query.append(token)
            else:
                if len(query) <= 40: # KT/CT has a 40-character input buffer.
                    return True
        return False

    def respond():
        """Simulates the corresponding KT/CT response for a given query.
            :returns: The expected KT/CT output according to the Heitronics spec.
            :rtype: String
        """
        for command, response in self.language.items():
            settings = re.match(command, self.query)
            if settings:
                return response(settings, self.device_values)
        raise SerialException("ERROR 19: CAN'T DO IT")

class FakeSerial(Serial):
    """Simulates generic serial device behavior.
       This class does not mock serial.tools.list_ports.comports behavior,
       since that function call is expected to function regardless of whether a KT/CT is plugged in.
    """

    def __init__(self, port, baudrate=9600, timeout=0.2):
        """Create a mock serial object.
            :param port: Serial port, we don't really care what format.
            :type port: String
        """
        super(FakeSerial, self).__init__()
        self.name = self.port = port
        self.responder = Responder() # Delegate generating KT/CT-like responses to a separate object.
                                     # Whenever mock KT/CT command output is desired, a call to self.responder should be made.
        self.output_buffer = self.input_buffer = []
        self.baudrate = baudrate
        self.timeout = timeout
        self.is_open = True

    def check_connection(func):
        """Checks whether this connection is open prior to any member/function call.
           This is less invasive than checking for self._is_open in every function call.
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.is_open:
                raise SerialException("Cannot write, serial connection is not open.")
            else:
                return func(self, *args, **kwargs)
        return wrapper

    @check_connection
    def readline(self):
        """Provide a mock response from the serial object.
            :returns: Fake response corresponding to the input query specified by a write().
            :rtype: String
        """
        tokens = []
        if self.output_buffer:
            tokens = self.output_buffer.split('\n')
            response, self.output_buffer = tokens[0], list(chain.from_iterable(tokens[1]))
            return response
        sleep(self._timeout()) # Just like a real serial connection, block until EOF/EOL or timeout elapsed. We could choose to include the 1/10 failure rate here, but I chose not to.

    @check_connection
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

    @check_connection
    def open(self):
        """Pretends to open a serial connection.
        """
        self._is_open = True

    @check_connection
    def close(self):
        """Pretends to close a serial connection.
        """
        self._is_open = False
