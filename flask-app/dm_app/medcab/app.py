"""App to serve models based on user input"""

from flask import Flask, request, jsonify
from .predictions import get_prediction
from .functions import disease_filter

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'This Works'

    @app.route('/prediction', methods=['GET'])
    def api_return():
        
        prediction = get_prediction(request)
        disease = disease_filter(request.args.get('disease'))
        json = jsonify(strains=prediction, info=disease)
        return json
        
    return app
