import re
import serial

class Radiometer():
    """A wrapper and Python interface for KT/CT-15 radiometer commands."""

    def __init__(self, ser):
        """Establish a serial connection to a radiometer. This constructor takes a serial object, rather than a serial port, so that the user can access the list of serial ports without interacting with this class.
            :param ser: Serial object with a unique port. On Windows, this is a COM## port; on macOS, this is /dev/cu.usbserial-##; on Linux, this is /dev/tty/##.
            :type ser: serial.Serial
        """
        self.ser = ser
        if self.ser.timeout > 1:
            self.ser.timeout = 1
        self.device_params = ['KT15.15', 'DET A', 'SN 1234', '0.000', '0.000', 'C']

    def _get_value(self, query, regex='(\d+[.]*\d*|\d*[.]+\d+)'):
        """Ask the radiometer a query."""
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        pattern = re.compile(regex)
        self.ser.write(query)
        response = self.ser.read_very_eager()
        return pattern.search(response)

    def set_calibration(self, cal):
        """Change the calibration factor of the radiometer.
            :param cal: Calibration coefficient to send to the radiometer.
            :type cal: float
            :returns: True if the calibration factor was successfully set; False otherwise.
            :rtype: bool
        """
        self.ser.reset_input_buffer()
        self.ser.write('CAL %f\r\n' % cal)
        if self.ser.read_very_eager():
            return False
        return True

    def interrogate(self):
        """Interrogate device parameters. Analogous to the "INFO ?" command.
            :returns: Device parameters, including device type, detector type, serial number, initial temperature, and final temperature.
            :rtype: String
        """
        return ' '.join(self.device_params)

    def get_calibration(self):
        """Grab the current calibration factor of the radiometer.
            :returns: Current calibration factor setting of the radiometer.
            :rtype: float
        """
        exp = self._get_value(query='CAL ?\r\n', regex='(\d+[.]\d*)')
        if exp:
            return float(exp.group(1))
        raise ValueError('Serial/KT15 error. Try resetting your connection to the KT/CT controller.')

    def get_radiation(self):
        """Grab the instantaneous measured radiation of the radiometer.
            :returns: Temperature in Celsius.
            :rtype: float
        """
        exp = self._get_value(query='RAD\r\n')
        if exp:
            return float(exp.group(1))
        raise ValueError('Was not able to retrieve radiation. Try resetting the KT/CT controller.')

    def get_temperature(self):
        """Grab the instantaneous measured temperature of the radiometer.
            :returns: Temperature in Celsius.
            :rtype: float
        """
        exp = self._get_value(query='TEMP\r\n')
        if exp:
            return float(exp.group(1))
        raise ValueError('Was not able to retrieve temperature. Try resetting the KT/CT controller.')

    def get_unit(self):
        """Grab the current temperature unit of the radiometer.
            :returns: 'K' for Kelvin, 'C' for Celsius, or 'F' for Fahrenheit.
            :rtype: char
        """
        exp = self._get_value(query='UNIT ?\r\n', regex='(.)')
        if exp:
            return exp.group(1)
        raise ValueError('Was not able to retrieve unit. Try resetting the KT/CT controller.')
