"""make prediction based on request data sent over"""
import os
import pandas as pd
import pickle
from pathlib import Path
from sklearn.neighbors import NearestNeighbors

# Load Pickle Models
#base_dir = Path(__file__) #returns web_app/prediction.py

# base_dir_par = Path(__file__).parent #returns web_app
# print(base_dir_par)

# BASE = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'web_app')) #returns /Users/blakelobato/Desktop/med_cab/flask-app/bl_app/web_app


# dtm = pickle.load(open(os.path.join(base_dir_par, 'dtm.pkl'), 'rb'))
# tf = pickle.load(open(os.path.join(base_dir_par, 'tf.pkl'), 'rb'))

dtm = pickle.load(open('dtm.pkl', 'rb'))
tf = pickle.load(open('tf.pkl', 'rb'))


def get_prediction(data):
    """use request data passed to make prediction"""

    #load in data
    df = pd.read_csv("https://raw.githubusercontent.com/med-cab1/ds-api/master/data/cannabis.csv")
    disease = pd.read_csv("https://raw.githubusercontent.com/med-cab1/ds-api/master/data/Disease.csv")

    df['Criteria'] = df['Effects'] + ',' + df['Flavor']

    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)

     # load requests
    entry = [data.args.get('effect1'), data.args.get('effect2'), data.args.get('effect3'), data.args.get('effect4'),data.args.get('effect5'), data.args.get('flavor1'),data.args.get('flavor2'), data.args.get('flavor3')]

    #transform the data
    new = tf.transform(entry)
    results = nn.kneighbors(new.todense())

    # extract top 5 results
    weed_types = [df['Strain'][results[1][0][i]] for i in range(5)]

    return weed_types

























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