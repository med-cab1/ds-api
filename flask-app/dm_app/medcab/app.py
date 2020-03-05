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
        data = request.args or request.form or request.json
        prediction = get_prediction(data)
        disease = disease_filter([x for x in data.values()][0])
        json = jsonify(strains=prediction, info=disease)
        return json


    """
    #test POST method with json data
    test_case = {'disease':'Glaucoma',
                'effect1':'Creative',
                'effect2':'Energetic',
                'effect3':'Tingly',
                'effect4':'Euphoric',
                'effect5':'Relaxed',
                'flavor1':'Earthy',
                'flavor2':'Sweet',
                'flavor3':'Citrus'
                }
    test_result = {'info': 'Daily Dosage: 5mg THC. Take 1 capsule.',
                  'strains': ['Blueberry-Trainwreck',
                              'Boggle-Gum',
                              'Kid-N-Cookies',
                              'Cronuts',
                              'Huckleberry-Hound']
                              }
    with app.test_client() as c:
        rv = c.post('/prediction', json=test_case)
        json_data = rv.get_json()
        assert json_data == test_result
    """

    return app
