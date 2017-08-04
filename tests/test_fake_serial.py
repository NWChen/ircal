import unittest
from fake_serial import FakeSerial
from itertools import izip

class FakeSerialTestCase(unittest.TestCase):
    
    def setUp(self): 
        FAKE_PORT = 1
        self.serial = FakeSerial(port=FAKE_PORT)

    def tearDown(self):
        if self.serial.is_open:
            self.serial.close()

    def _send_and_respond(self, command):
        self.serial.write(command)
        return self.serial.readline()

    def test_interrogation(self):
        queries = ['CAL ?\n', 'TEMP\n', 'RAD\n', 'UNIT ?\n']
        expected_responses = ['2.0\n', '25.0\n', '0.0\n', 'C\n']
        for query, expected_response in izip(queries, expected_responses):
            response = self._send_and_respond(query)
            print query, response, expected_response
            self.assertEqual(response, expected_response)

def get_tests():
    tests = ['test_interrogation']
    return unittest.TestSuite(map(FakeSerialTestCase, tests))

if __name__ == '__main__':
    sys.exit(unittest.main())
