"""Flask App for Med Cabinet"""


##NOTE -- THIS IS JUST A SKELETON, MORE WORK TO BE DONE AND REFINING NEEDED##

from flask import Flask, render_template
import requests
from flask_sqlalchemy import sqlalchemy


def creaate_app():

    APP = Flask(__name__)

    APP.config['SQLALCHEMY_DATABASE_URI'] = #####keys_from_matthew

    cannabis = pd.read_csv('..\data\cannabis.csv')
    disease = pd.read_csv('..\data\Disease.csv')

    #Mock DB class
    class Users(DB.model):
        id = DB.Column(DB.Integer, primary_key=True)
        username = DB.Column(DB.String(50))
        password = DB.Column(DB.String(50))

        def __repr__(self):
            return f'ID: {id}, username: {self.username}, password: {self.password}'

    @APP.route('/')
    def root():
        """Base route, either where we want to enter the user information form or where we want to have a welcome page"""

        return "dummy info until we solidfy route"

    @APP.route('/about')
    def about():
        """This page is used to describe the about page -- the mission statement of med cabinet as well as information about the app itself"""

        #return  render_template('####.html', title='ABOUT MED CABINET')

        #could render a template to beautify this a bunch just getting it created for time being

        return "The main purpose of the Med Cabinet Flask Application is to provide a scientific resource for dosage, consumption, and recommendation of cannabis for people who are fighting opioid addictions. In addition to that, this app is also boardened to help people struggling with different mental illnesses and diseases such as cancer, glaucoma, post stress disorders, siezures, autism, etc."


    @APP.route('/prediction', methods=['GET'])
    def predict():
        """Prediction route using a pipeline, no pickling."""
        if 'id' in request.args:
            id = int(request.args['id'])

            cannabis = cannabis.query.get(id)

            condition_id = cannabis.condition_id.condition_id ####unsure on this
            flavor_id = cannabis.flavor_id
            effect_id = cannabis.effect_id.effect_id ###unsure on this 
            ###where does strain factor into all this

            df = pd.DataFrame(
                columns=['condition_id', 'flavor_id', 'effect_id', 'strain'], #probably need more like condition severity, desire of consumption etc.
                data=[[condition_id, flavor_id, effect_id']
            )

            train = pd.read_csv('our cannabis csv file')
            target = 'strain'

            features = train.columns.drop(target)
            X_train = train[features]
            y_train = train[target]

            pipeline = make_pipeline(
                ce.OrdinalEncoder(),
                LinearRegression() ### K-NN, or NN
            )

            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(df)
            
            ### need to refine the list process rough outline of idea behind it....
            top_5 = []
            lenght = 5
            for pred in range(length):
                top_5 = top_5.append(pred)
                return top_5

            transformers = make_pipeline(
                ce.OrdinalEncoder(),
                SimpleImputer(strategy='mean')
            )

            X_train_transformed = transformers.fit_transform(X_train)

            model = LinearRegression() ####AGAIN dependant on what model we use
            model.fit(X_train_transformed, y_train)

            else:
                return "Error: no id field provided"

            return top_5



    @APP.route('/predpickle', methods=['GET'])
    def predpickle():
        """Prediction route using pickling."""

        ###Not entirely sure how to pickle in a LSTM model :/ ###

        if 'id' in request.args:
            id = int(request.args['id'])

            cannabis = cannabis.query.get(id)

            condition_id = cannabis.condition_id.condition_id ####unsure on this
            flavor_id = cannabis.flavor_id
            effect_id = cannabis.effect_id.effect_id ###unsure on this 
            ###where does strain factor into all this

            df = pd.DataFrame(
                columns=['condition_id', 'flavor_id', 'effect_id'], #probably need more like condition severity, desire of consumption etc.
                data=[[condition_id, flavor_id, effect_id']
            )
            y_preds = pipeline.predict(pred_df)[:5]
            return y_preds


    APP.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        init_db()
        #return render_template('####.html', title='DB Reset')
    return app




