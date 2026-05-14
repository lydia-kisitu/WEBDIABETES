from flask import Flask,render_template,request
import numpy as np
import pickle

# create a Flask instance for your app
app=Flask(__name__)

# load the trained model
model=pickle.load (open("C:\\Users\\user\\Documents\\webdesigningVisualBasic\\StreamlitApp\\FlaskDemDiabetes\\Diabetes\\model\\lr.pkl",'rb'))

# route the app to the root URL represented as "/"
@app.route("/")
def homepage():
    # call the homepage.html
    return render_template('homepage.html')


# route the app to the predict function
@app.route("/predict",methods=['POST']) #POST is used to process the form data
def predict():
    # request the values from the html page
    pregnancies=float(request.form['pregnancies'])
    glucose=float(request.form['glucose'])
    bp=float(request.form['bp'])
    skin_thickness=float(request.form['skin_thickness'])
    insulin=float(request.form['insulin'])
    bmi=float(request.form['bmi'])
    dpf =float(request.form['DPF'])
    age =float(request.form['AGE'])

    # Create the input test data in the form that the trained ML model can understand
    data=[np.array([pregnancies,glucose,bp,skin_thickness,insulin,bmi,dpf,age])]
    
    # call the predict function with the input test data and store the results
    result=model.predict(data)
    # print the result on console
    print(result)
    
    if (result == 0):
        msg="Prediction: Not Diabetic"
    else:
        msg="Prediction: Diabetic"
    
    # render the homepage.html with the prediction results
    return render_template('homepage.html',prediction_value=msg)

# run the Flask app
if __name__=='__main__':
    app.run(debug=True) 
