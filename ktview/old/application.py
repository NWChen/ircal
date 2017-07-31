#!/usr/bin/env python
import csv
import webview
import sys
import threading
import json

from datetime import datetime
from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

data = []

class Data(object):
    """ Encapsulates a row of data, where the first element is a point in time. """
    pass

def _read_data(f):
    """ Takes a FileStorage object, and converts it to a list of tuples representing the data. """
    try:
        dialect = csv.Sniffer().sniff(f.read(), delimiters="\t")
        f.seek(0)
        headers = f.readline().replace("\r\n", "").split('\t')
        data = list(csv.reader(f, dialect))
        date_format = '%m/%d/%Y %H:%M:%S.%f'
        for row in data:
            row[0] = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S.%f')
            row[1:] = map(float, row[1:])
        return headers, zip(*data)
    except csv.Error:
        return None, None

def _get_column(data, col):
    """ Takes a 2d list (or a list of tuples) and a 1-indexed column index, and returns the corresponding column data. """
    return [data[i][col-1] for i in range(len(data))]

@app.route('/', methods=['GET', 'POST'])
def upload():
    """ Handles file upload of CSV data """
    if request.files:
        global data
        file = request.files['file']
        headers, data = _read_data(file)
        return render_template('index.html', headers=headers)
    if request.args and data:
        cols = request.args.get('cols').split(',')
        raw = []
        for col in cols:
            col = int(col)
            raw.append(_get_column(data, col))
        print "RAW DATA: ---"
        print raw
        return render_template('index.html', raw=raw, headers=headers)
    return render_template('index.html')

@app.route('/')
def index():
    """ Handles all other views """
    return render_template('index.html')

@app.route('/change_data', methods=['POST'])
def change_data():
    cols = request.args.get('cols')

    return redirect(url_for('upload', cols=cols))

def _start_server():
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    if DEBUG:
        _start_server()
    else:
        t = threading.Thread(target=_start_server)
        t.daemon = True
        t.start()
        webview.create_window('Calibration Dashboard', 'http://%s:%d' % (HOST, PORT))
        sys.exit()
