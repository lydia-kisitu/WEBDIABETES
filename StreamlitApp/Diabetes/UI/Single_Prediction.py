
import streamlit as st
import pickle
import numpy as np


st.title("Welcome to Diabetes Test")
st.header("Please fill in your details")

preg=st.number_input("Enter Preganancies",0,10,5)
glucose=st.number_input("Enter glucose level",0,200)
blood_pressure=st.number_input("Enter blood pressure",0,200)
skin=st.number_input("Enter skin thickness",0,200)
insulin = st.number_input("Enter insulin level",0,200)
bmi = st.number_input("Enter bmi",0,200)
pedigreefn = st.number_input("Enter DiabetesPedigreeFunction",0,200)
age = st.slider('Select your age:', 0, 100, 25)

#create a button to predict output
predict_clicked=st.button("Get the prediction")

if predict_clicked==True:
    import pickle

    #load the test data into numpy array
    data=[np.array([preg,glucose,blood_pressure,skin,insulin,bmi,pedigreefn,age])]
    with open("C:\\Users\\user\\webDiabetes\\StreamlitApp\\Diabetes\\Model_Development\\classifier.pkl",
    "rb") as file:
          model = pickle.load(file)

    #call the model to predict the price
    result=model.predict(data)
    if (result):
        result_string = "Diabetic"
    else:
        result_string = "Non-Diabetic"

    #display the predicted price on the webpage
    st.success("The outcome for your diabetes test is "+result_string)

    #calling the model

    #load the test data into numpy array
    #data=[np.array([preg,glucose,blood_pressure,skin,insulin,bmi,pedigreefn,age])]

    #display the predicted price on the webpage
    st.success("The outcome for your diabetes test is "+result_string)




