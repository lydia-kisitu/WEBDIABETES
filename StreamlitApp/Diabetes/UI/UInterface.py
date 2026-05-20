import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open(
    "C:\\Users\\user\\webDiabetes\\StreamlitApp\\Diabetes\\Model_Development\\classifier.pkl",
    "rb"
) as f:
    model = pickle.load(f)
    # Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
    This app predicts the likelihood of diabetes
    using Machine Learning.

    Model trained using the Pima Indians Diabetes Dataset.
    """
)

st.sidebar.header("Model Information")

st.sidebar.write("Algorithm: Random Forest Classifier")

st.sidebar.write("Created with Streamlit")

# App title
st.title("Welcome to Diabetes Prediction App")
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
    Diabetes Prediction App
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


st.header("Please fill in your details")
st.subheader("Patient Health Information")

st.write("Enter patient details below to predict diabetes risk.")
st.info(
    "Fill in the patient measurements below and click Predict.")

# Form
with st.form("prediction_form"):

    pregnancies = st.slider("Pregnancies", 0, 15, 1)

    glucose = st.slider("Enter glucose level", 0, 200)

    blood_pressure = st.slider("Enter blood pressure", 0, 200)

    skin = st.slider("Enter skin thickness", 0, 200)

    insulin = st.slider("Enter insulin level", 0, 900)

    bmi = st.slider("Enter BMI", 0.0, 70.0, 25.0)

    pedigreefn = st.slider(
        "Enter Diabetes Pedigree Function",
        0.0,
        2.5,
        0.5
    )

    age = st.slider("Select your age:", 0, 100, 25)

    # Submit button
    submit = st.form_submit_button("Predict")

# Prediction
if submit:

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin,
        insulin,
        bmi,
        pedigreefn,
        age
    ]])

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    if prediction[0] == 0:
           st.success(
            f"Non-Diabetic ✅ "
            f"(Confidence: {probability[0][0] * 100:.2f}%)"
        )

    else:

        st.error(
            f"Diabetic ⚠️ "
            f"(Confidence: {probability[0][1] * 100:.2f}%)"
        )

    # Create dataframe
    chart_data = pd.DataFrame({
        "Feature": [
            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "Pedigree Function",
            "Age"
        ],

        "Value": [
            pregnancies,
            glucose,
            blood_pressure,
            skin,
            insulin,
            bmi,
            pedigreefn,
            age
        ]
    })

    # Display chart
    st.subheader("Patient Data Visualization")

    st.bar_chart(chart_data.set_index("Feature"))
             