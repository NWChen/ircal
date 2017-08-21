import unittest
import time
from fake_serial import FakeSerial
from test_fake_telnet import NonBlockingDaemon

import sys
sys.path.append('../src') # bring in Radiometer, Blackbody classes from ../src
from radiometer import Radiometer
from blackbody import Blackbody

class FakeSystemTestCase(unittest.TestCase):

    def setUp(self):
        try:
            self.nbd = NonBlockingDaemon()
        except Exception as e:
            print e
            sys.exit(0)
        time.sleep(1)
        FAKE_PORT = 1
        self.serial = FakeSerial(port=FAKE_PORT)
        self.radiometer = Radiometer(self.serial)
        self.blackbody = Blackbody(addr='localhost', port=9999)

    def tearDown(self):
        self.blackbody.close()
        if self.serial.is_open:
            self.serial.close()

    def test_blackbody_updates(self):
        self.blackbody.set_temperature(36.5)
        current_temp = self.blackbody.get_temperature()
        while(current_temp < 36.1):
            time.sleep(0.2)
            current_temp = self.blackbody.get_temperature()
            print current_temp
        import pdb; pdb.set_trace()
        return True

    def test_radiometer_blackbody_chatter(self):
        self.blackbody.set_temperature(1.1)
        current_temp = self.blackbody.get_temperature()
        while(current_temp > 1.1):
            self.serial.responder.device_values['temp'] = str(current_temp) # send blackbody temperature to radiometer
            time.sleep(0.2)
            current_temp = self.blackbody.get_temperature()
            print self.radiometer.get_temperature
        import pdb; pdb.set_trace()
        return True

if __name__ == '__main__':
    sys.exit(unittest.main())
