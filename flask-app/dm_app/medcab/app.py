"""App to serve models based on user input"""

from flask import Flask, request, jsonify
from .predictions import get_prediction
from .functions import disease_filter

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'This Works'

    @app.route('/prediction', methods=['GET', 'POST'])
    def api_return():
        data = request.args or request.form
        prediction = get_prediction(data)
        disease = disease_filter(data.get('disease'))
        json = jsonify(strains=prediction, info=disease)
        return json

    return app
