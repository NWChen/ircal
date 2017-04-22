import webview
import sys
import threading
import ktview
import json

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
host = '0.0.0.0'
port = 5000

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        label = request.args.get('label')
        print label
    if request.method=='POST':
        labels, data = ktview.read_data(request.files['file'])
        if labels != None:
            labels = labels.split("\t")
        return render_template('index.html', labels=labels)
    return render_template('index.html')

''' Route POST requests to /upload and redirect to /, in case POSTing to / is not supported. '''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    label = request.get_json()['label']
    
    return redirect(url_for('index', label=label))

def start_server():
    app.run(host=host, port=port)

if __name__ == '__main__':
    start_server()
    #t = threading.Thread(target=start_server)
    #t.daemon = True
    #t.start()

    #webview.create_window('KTView', 'http://' + host + ':' + str(port))
    #sys.exit()
