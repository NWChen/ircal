import serial
import threading
import time


class Ktct():

    def __init__(self, port="COM51"):
        self.ser = serial.Serial(port=port, timeout=1)
        try:
            self.ser.open()
        except serial.SerialException:
            pass

        if self.ser.isOpen():
            try:
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
            except serial.SerialException:
                pass

        thread = threading.Thread(target=_read)
        thread.start()

    def _read():
        return 

    def set_timeout(self, timeout):
        self.ser.timeout = timeout

    def get_temp(self):
        self.ser.write("TEMP\r\n")
        response = self.ser.readline()
        self.ser.reset_input_buffer()
        return response

    def get_calibration(self):
        self.ser.write("CAL ?\r\n")
        response = self.ser.readline()
        self.ser.reset_input_buffer()
        return response

    def set_calibration(self, calibration):
        self.ser.write("CAL " + str(calibration))
        response = self.ser.readline()
        self.ser.reset_input_buffer()
        return response

    def simulate(self):
        
