from flask import Flask, request, jsonify
import json

from utils import create_orders


app = Flask(__name__)


@app.route('/create_orders', methods=['POST'])
def create_orders_endpoint():
    try:
        data = request.get_json()

        if not data or not isinstance(data, dict):
            return jsonify({'error': 'Invalid data format'})

        orders = create_orders(data)

        return jsonify({'orders': orders})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
