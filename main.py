from flask import Flask, make_response, jsonify
import json

from crud import CRUD
from models.stocks import TickerData
from store_data import read_json_and_store

app = Flask(__name__)

ob = CRUD()


@app.route('/save/<string:foldername>/<string:filename>', methods=['POST'])
def safe_data_from_file(foldername,
                        filename):
    try:
        result = read_json_and_store(foldername, filename)
        if result:
            res = make_response({'data': 'success'}, 200)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
    except Exception as e:
        return make_response(jsonify({'error': f'parameters missing{e}'}), 200)


@app.route('/insert/<string:params>', methods=['POST'])
def save_data(data):
    try:
        ob.insert(json.loads(data))
        res = make_response({'data': 'success'}, 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return make_response(jsonify({'error': f'parameters missing{e}'}), 200)


@app.route('/fetch/<string:id>', methods=['GET'])
def get_data():
    try:

        res = make_response({'data': ob.read()}, 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return make_response(jsonify({'error': f'parameters missing{e}'}), 200)


@app.route('/update/<string:data>', methods=['POST'])
def update_data(data):
    try:
        ob.update(data['id'], json.loads(**data))
        res = make_response({'data': 'updated'}, 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return make_response(jsonify({'error': f'parameters missing{e}'}), 200)


@app.route('/delete/<string:id>', methods=['POST'])
def delete_data(data):
    try:
        ob.delete(data['id'])
        res = make_response({"data": 'deleted'}, 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return make_response(jsonify({'error': f'parameters missing{e}'}), 200)


if __name__ == '__main__':
    app.run(debug=True)

    #save_data(json.dumps({"name": "bhoot"}))
