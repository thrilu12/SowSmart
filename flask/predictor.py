from flask import Flask,render_template,request
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report

app = Flask(__name__)

@app.route("/")
def index():
    PATH = 'D:\pcl project\flask\Crop_recommendation.csv'
    df = pd.read_csv(PATH)
    features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
    target = df['label']
    labels = df['label']
    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)
    from sklearn.ensemble import RandomForestClassifier
    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(Xtrain,Ytrain)
    with open('RF.pkl', 'wb') as model_file:
        pickle.dump(RF, model_file) 
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])


    form_array = np.array([[N,P,K,temperature,humidity,ph,rainfall]])
    model=pickle.load(open('RF.pkl','rb'))
    prediction=model.predict(form_array)[0]
    result=prediction
    return render_template('result.html',result=result)


if __name__ == "__main__":
    app.run(debug=True, port=9457)
