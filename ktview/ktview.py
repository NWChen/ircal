#!/usr/bin/env python
from datetime import datetime
import csv
import logging
import serial
import string
import sys

def _die(message):
    sys.exit(message)

def ktct_init(port):
    try:
        ser = serial.Serial(port, timeout=0)
    except serial.SerialException:
        _die(port + " is not connected. Please try a different USB port.")
    if ser is None:
        _die("Serial connection detected but failed. Please try a different USB port.")
    return ser

def ktct_read(ser):
    out = ser.readline()
    if len(out) < 1:
        return ""
    return out

def ktct_ask_temp(ser):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write("TEMP\r\n")

def bb_init():
    try:
        tn = telnetlib.Telnet("192.168.200.161", "7788", timeout=2)
    except Exception, e:
        print e
        _die("IP or port not recognized. Please try again.")

def bb_read(tn):
    response = tn.read_very_eager()
    if len(response) < 1:
        return ""
    field = "T2="
    i = response.index(field) + len(field)
    response = response[i : response.index("\n", i)]
    response = filter(lambda c : c in string.digits + '.', response)
    return float(response)

def bb_set(tn, setpoint):
    tn.write("DA" + str(setpoint) + "\r\n")

def bb_get(tn):
    tn.write("M2\r\n")

def get_data(path):
    try:
        with open(path, 'rb') as f:
            dialect = csv.Sniffer().sniff(f.read(), delimiters="\t")
            f.seek(0)
            f.readline()
            data = list(csv.reader(f, dialect))
            for row in data:
                row[0] = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S.%f')
                row[1:] = map(float, row[1:])
            return data
    except IOError:
        print "file not found"
    else:
        return None

def read_data(f):
    """ Takes a FileStorage object, and converts it to a list of data. """
    dialect = csv.Sniffer().sniff(f.read(), delimiters="\t")
    f.seek(0)
    header = f.readline()
    data = list(csv.reader(f, dialect))
    for row in data:
        row[0] = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S.%f')
        row[1:] = map(float, row[1:])
    return header, data

if __name__ == '__main__':
    get_data('/home/nwchen/Desktop/ldeo/spring/2014_KT15_82_calib_217_155922.txt')
