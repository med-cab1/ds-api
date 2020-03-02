"""make prediction based on request data sent over"""
import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(BASE_DIR, 'model.pkl')

def get_prediction(data):
    """use request data passed to make prediction"""
    
    # load data from GET request into dataframe
    input = pd.DataFrame(
        columns=['disease', 'effect1', 'effect2', 'effect3',
                 'effect4', 'effect5', 'flavor1', 'flavor2',
                 'flavor3'],
        data=[data['disease'], data['effect2'], data['effect3'],
              data['effect4'], data['effect5'], data['flavor1'],
              data['flavor2'], data['flavor3']]
    )

    # load model from pickle file
    model = pickle.loads(MODEL)
    
    return model.predict(input)[:5] #return first 5 predictions

"""
Example:
data = {'disease':'Glaucoma',
'effect1':'Creative',
'effect2':'Energetic',
'effect3':'Tingly',
'effect4':'Euphoric',
'effect5':'Relaxed',
'flavor1':'Earthy',
'flavor2':'Sweet',
'flavor3':'Citrus'}
"""