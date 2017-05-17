#!/usr/bin/env python
import csv
import json

from datetime import datetime

class DataHandler(object):

    def  __init__(self, file='', file_by_name=True):
        """ Constructs a DataHandler which processes raw input data. """
        if file == '':
            self.headers, self.data = [], []
        else:
            try:
                # Grab data from the input file.
                if file_by_name:
                    file = open(file, 'r')
                dialect = csv.Sniffer().sniff(file.read(), delimiters='\t')
                file.seek(0)

                # Clean up the data.
                self.headers = file.readline().replace('\r\n', '').split('\t')
                data = list(csv.reader(file, dialect))
                DATE_FORMAT = '%m/%d/%Y %H:%M:%S.%f'
                start_time = datetime.strptime(data[0][0], DATE_FORMAT)
                for row in data:
                    row[0] = self.millisecond_timedelta(start_time, datetime.strptime(row[0], DATE_FORMAT))
                    row[1:] = map(float, row[1:])
                self.data = zip(*data)
            except AttributeError as e:
                print "Error in input file, no data received."
                print e
                self.headers, self.data = [], []
            except IOError as e:
                print "IOError, no data received."
                print e
                self.headers, self.data = [], []

    def millisecond_timedelta(self, start, end):
        return int((end - start).total_seconds() * 1000.0)

    def get_headers(self):
        return self.headers

    def get_data(self, header):
        x, y = [], []
        if len(self.data) > 0:
            x = self.data[0]
            y = self.data[self.headers.index(header)]
        return [dict([ ('x', pair[0]), ('y', pair[1]) ]) for pair in zip(x,y)]

'''
    def get_column(self, header):
        """ Gets all the data in the column with the desired header. """


        i = self.headers.index(header)
        return self.data[i]

    def get_columns(self, headers, time_column='TIME'):
        """ Gets all data in columns with the desired header. The first column is considered the time scale by default. """
        desired_data = [ self.get_serialized_time(time_column) ]
        for header in headers:
            desired_data.append(self.get_column(header))
        return desired_data

    def get_data(self, headers, time_column='TIME'):
        desired_data = dict(zip(*self.get_columns(headers, time_column)))
        return desired_data

    def get_serialized_time(self, time_column='TIME'):
        time_column = list(self.get_column(time_column))
        start_time = time_column[0]
        for i, time in enumerate(time_column):
            time_column[i] = int((time - start_time).total_seconds() * 1000.0)
        return time_column
'''
