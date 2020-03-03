"""Flask App for Med Cabinet"""

from flask import Flask, request, jsonify
from .prediction import get_prediction
import pandas as pd
from .functions import *


def create_app():

    APP = Flask(__name__)

    #cannabis = pd.read_csv('..\data\cannabis.csv')
    #disease = pd.read_csv('..\data\Disease.csv')
    @APP.route('/')
    def root():
        """Base route, either where we want to enter the user information form or where we want to have a welcome page"""

        return "dummy info until we solidfy route"

    @APP.route('/about')
    def about():
        """This page is used to describe the about page -- the mission statement of med cabinet as well as information about the app itself"""


        return "The main purpose of the Med Cabinet Flask Application is to provide a scientific resource for dosage, consumption, and recommendation of cannabis for people who are fighting opioid addictions. In addition to that, this app is also boardened to help people struggling with different mental illnesses and diseases such as cancer, glaucoma, post stress disorders, siezures, autism, etc."

    @APP.route('/prediction', methods=['GET'])
    def predict():
        """Prediction route using pickling."""
        prediction = get_prediction(request)
        disease = disease_filter(request.args.get('disease'))
        json = jsonify(strains=prediction, info=disease)
        return json

    return APP

