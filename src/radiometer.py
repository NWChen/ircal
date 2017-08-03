import serial

class Radiometer():
    """A wrapper and Python interface for KT/CT-15 radiometer commands."""

    def __init__(self, ser):
        """Establish a serial connection to a radiometer.
            :param port: Serial object with a unique port. On Windows, this is a COM## port; on macOS, this is /dev/cu.usbserial-##; on Linux, this is /dev/tty/##.
            :type port: serial.Serial
        """
        pass

    def set_calibration(self, cal):
        """Change and the calibration factor of the radiometer.
            :param cal: Calibration coefficient to send to the radiometer.
            :type cal: float
            :returns: True if the calibration factor was successfully set; False otherwise.
            :rtype: bool
        """
        pass

    def interrogate(self):
        """Interrogate device parameters. Analogous to the "INFO ?" command.
            :returns: Tuple containing device type, detector type, serial number, initial temperature, and final temperature.
            :rtype: (string, char, int, float, float)
        """
        pass

    def get_calibration(self):
        """Grab the current calibration factor of the radiometer.
            :returns: Current calibration factor setting of the radiometer.
            :rtype: float
        """
        pass

    def get_radiation(self):
        """Grab the instantaneous measured radiation of the radiometer.
            :returns: Temperature in Celsius.
            :rtype: float
        """
        pass

    def get_temperature(self):
        """Grab the instantaneous measured temperature of the radiometer.
            :returns: Temperature in Celsius.
            :rtype: float
        """
        pass

    def get_unit(self):
        """Grab the current temperature unit of the radiometer.
            :returns: 'K' for Kelvin, 'C' for Celsius, or 'F' for Fahrenheit.
            :rtype: char
        """
        pass
