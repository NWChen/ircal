import webview
import sys
import threading
from flask import Flask, render_template

app = Flask(__name__)
host = '0.0.0.0'
port = 5000

@app.route('/')
def load():
    return render_template('index.html')

def start_server():
    app.run(host=host, port=port)

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window('KTView', 'http://' + host + ':' + str(port))
    sys.exit()
