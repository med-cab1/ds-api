"""make prediction based on request data sent over"""
import os
import pandas as pd
import pickle
from pathlib import Path
from sklearn.neighbors import NearestNeighbors

# Load Pickle Models
#dtm = pickle.load(https://github.com/med-cab1/ds-api/blob/master/dtm.pkl)
#tf = pickle.load(https://github.com/med-cab1/ds-api/blob/master/tf.pkl)

BASE = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'web_app'))
print(BASE)
dtm = pickle.load(open(os.path.join(BASE, 'dtm.pkl'), 'rb'))
tf = pickle.load(open(os.path.join(BASE, 'tf.pkl'), 'rb'))


def get_prediction(data):
    """use request data passed to make prediction"""

    df = pd.read_csv("https://raw.githubusercontent.com/med-cab1/ds-api/master/data/cannabis.csv")
    disease = pd.read_csv("https://raw.githubusercontent.com/med-cab1/ds-api/master/data/Disease.csv")

    df['Criteria'] = df['Effects'] + ',' + df['Flavor']

    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)

     # load request data, transform, get results
    entry = [data.args.get('effect1'), data.args.get('effect2'), data.args.get('effect3'), data.args.get('effect4'),data.args.get('effect5'), data.args.get('flavor1'),data.args.get('flavor2'), data.args.get('flavor3')]

    new = tf.transform(entry)
    results = nn.kneighbors(new.todense())

    # extract top 5 results
    weed_types = [strains['Strain'][results[1][0][i]] for i in range(5)]

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