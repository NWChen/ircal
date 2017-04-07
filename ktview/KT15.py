""" Controls and receives signals from a KT15 pyrometer"""
import logging
import sys
import serial

class KT15(object):
    """ Controls and receives signals from a KT15 pyrometer"""

    def __init__(self, port="COM51"):
        try:
            self.ser = serial.Serial(port, timeout=1)
        except serial.SerialException:
            self._die(port + " is not connected. Please try a different USB port.")
        if self.ser is None:
            self._die("Serial connection detected but failed. Please try a different USB port.")

    def temp(self):
        """Get absolute temperature recorded by the device."""
        self.ser.write("TEMP\r\n")
        response = self.ser.readline()
        while not response:
            response = self.ser.readline()
        return float(response[:response.index(" C")])

    def calibration_factor(self):
        """Get calibration factor stored by device."""
        self.ser.write("CAL ?\r\n")
        response = self.ser.readline()
        while not response:
            response = self.ser.readline()
        return float(response[4:])

    def set

    def set_calibration(self, calibration_factor):
        """Alter calibration factor of device."""
        request = "CAL " + str(calibration_factor)
        self.ser.write(request + "\r\n")
        self.ser.readline()
        return calibration_factor

    def _die(self, message):
        logging.exception(message)
        logging.exception("Leaving calibration utility, please try running again")
        sys.exit()
