"""App to serve models based on user input"""

from flask import Flask, request, jsonify
from .predictions import get_prediction

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'This Works'

    @app.route('/prediction', methods=['GET'])
    def api_return():
        prediction = get_prediction(request)
        return jsonify(str(prediction))

    return app
