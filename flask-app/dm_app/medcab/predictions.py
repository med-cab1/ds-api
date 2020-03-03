"""make prediction based on request data sent over"""
import os
import pandas as pd
import pickle
from pathlib import Path
from sklearn.neighbors import NearestNeighbors

# pickles
BASE_DIR = Path(__file__).parents[3]
dtm = pickle.load(open(os.path.join(BASE_DIR, 'dtm.pkl'), 'rb'))
tf = pickle.load(open(os.path.join(BASE_DIR, 'tf.pkl'), 'rb'))

# data
URL = "https://raw.githubusercontent.com/med-cab1/ds-api/master/data/cannabis.csv" 

def get_prediction(data):
    """use request data passed to make prediction"""
    # load cannabis data
    strains = pd.read_csv(URL)
    # Combine the Effects and Flavors in one column
    strains['Criteria'] = strains['Effects'] + ',' + strains['Flavor']

    # Train model on dtm
    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)

    # load request data, transform, get results
    entry = [data['effect1'], data['effect2'], data['effect3'],
              data['effect4'], data['effect5'], data['flavor1'],
              data['flavor2'], data['flavor3']]
    new = tf.transform(entry)
    results = nn.kneighbors(new.todense())
    
    # extract top 5 results
    output = [strains['Strain'][results[1][0][i]] for i in range(5)]
    
    return output

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