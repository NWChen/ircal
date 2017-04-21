import webview
import sys
import threading
import ktview

from flask import Flask, render_template, request, url_for

app = Flask(__name__)
host = '0.0.0.0'
port = 5000

@app.route('/')
def load():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data = ktview.read_data(request.files['file'])
    print data
    return render_template('index.html')

def start_server():
    app.run(host=host, port=port)

if __name__ == '__main__':
    start_server()
    #t = threading.Thread(target=start_server)
    #t.daemon = True
    #t.start()

    #webview.create_window('KTView', 'http://' + host + ':' + str(port))
    #sys.exit()
