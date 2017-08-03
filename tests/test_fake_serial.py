import unittest
from fake_serial import FakeSerial

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
        queries = ['CAL ?', 'TEMP', 'RAD', 'UNIT ?']
        expected_responses = ['2.0', '25.0', '0.0', 'C']
        for query, expected_response in izip(queries, expected_responses):
            response = self._send_and_respond(query)
            self.assertEqual(response, expected_response)

def suite():
    tests = ['test_write']
    return unittest.TestSuite(map(FakeSerialTestCase, tests))

if __name__ == '__main__':
    unittest.main()
