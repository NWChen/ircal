from flask import Flask, render_template, request, jsonify
from data_handler import DataHandler
import json

app = Flask(__name__)
dh = DataHandler('data.txt')

@app.route('/')
def index():
    data = dh.get_data( dh.get_headers()[1] )
    return render_template('index.html', dataPoints=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)
