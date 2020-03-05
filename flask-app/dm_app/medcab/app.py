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
        disease = disease_filter(data.get('disease'))
        json = jsonify(strains=prediction, info=disease)
        return json

    @app.route('/altpredict', methods=['GET', 'POST'])
    def json_return():
        json_form = request.form
        json_args = request.args
        # This returns a dict from the front-end
        #print([x for x in json_form.values()][0])
        #print(json_args)
        alt_data = request.args or request.form or request.json

        sample =  {'disease':'Glaucoma',
        'effect1':'Creative',
        'effect2':'Energetic',
        'effect3':'Tingly',
        'effect4':'Euphoric',
        'effect5':'Relaxed',
        'flavor1':'Earthy',
        'flavor2':'Sweet',
        'flavor3':'Citrus'}
        # Transforms the json received from users
        alt_prediction = get_prediction(alt_data)

        # This gets the first value of the first key of the json dictionary
        alt_disease = disease_filter([x for x in alt_data.values()][0])
        # Stores predict_dict in the session, so it can be gotten from /data
        # session['price'] = predict_dict
        alt_json = jsonify(strains=alt_prediction, info=alt_disease)
        return alt_json

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
