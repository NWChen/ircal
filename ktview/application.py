from flask import Flask, render_template, request, jsonify, url_for
from data_handler import DataHandler
from ktct import Ktct
from blackbody import Blackbody
from datetime import datetime
import json

app = Flask(__name__)
ktct = Ktct(debug=True)
bb = Blackbody(debug = True)
start_time = None

@app.route('/', methods=['GET', 'POST'])
def index():
    dh = DataHandler()
    data_series = []
    if request.method == 'POST':
        file = request.files['file']
        dh = DataHandler(file.filename)
        data_series = _prepare_data(dh, dh.get_headers())
    return render_template('index.html', headers=dh.get_headers(), dataSeries=data_series)

@app.route('/live_update')
def live_update():
    abs_temp = bb.read()
    exp_temp = ktct.read()
    time = DataHandler().millisecond_timedelta(start_time, datetime.now())
    return jsonify(x=time, y=abs_temp)

@app.route('/live')
def live():
    global start_time
    start_time = datetime.now()
    return render_template('live.html')

def _prepare_data(dh, headers):
    data_series = [{'type': 'line', \
                    'showInLegend': True, \
                    'name': header, \
                    'dataPoints': dh.get_data(header)} \
                    for header in headers]
    return json.dumps(data_series)

if __name__ == '__main__':
    app.run(debug=True)
