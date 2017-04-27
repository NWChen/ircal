import webview
import sys
import threading
import ktview
import json
import os

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__) 
app.secret_key = os.urandom(24)
host = '0.0.0.0' # localhost IP address
port = 5000      # default port; can be changed
debug = True     # make sure this is False when not testing the app

data = None

def _get_column(header, data):
    ''' Given the header for a column, returns that column without header from a list of tuples. Returns -1 if no such column (tuple) found. '''
    col_index = -1
    print session['headers']
    try:
        col_index = session['headers'].index(header)
    except ValueError:
        column = []
    else:
        column = data[col_index]
    return column

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Handles incoming requests on the index path, including the first time when the application loads. '''
    if request.method == 'POST':
        global data
        headers, data = ktview.read_data(request.files['file'])
        if headers != None:
            session['headers'] = headers = headers.split("\t")
        return render_template('index.html', headers=headers)
    return render_template('index.html')

@app.route('/_change_labels')
def change_labels():
    label = request.args.get('label')
    print label
    return jsonify(success=True)

@app.route('/_get_data')
def get_data():
    header = request.args.get('header')
    column = _get_column(header, data)
    return jsonify(data=column)

@app.route('/_get_xaxis')
def get_xaxis():
    ''' Retrieves time scale of data, assuming it is in the 0th column '''
    return jsonify(data=data[0])

def start_server():
    ''' Begins an instance of the Flask WSGI server. '''
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    if debug:
        start_server()
    else:
        t = threading.Thread(target=start_server)
        t.daemon = True
        t.start()
        webview.create_window('KTView', 'http://' + host + ':' + str(port))
        sys.exit()
