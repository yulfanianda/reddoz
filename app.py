import streamlit as st
import pickle
import pandas as pd
import numpy as np

try:
    model_female = pickle.load(open('lr_bodyfat_female.pckl', 'rb'))
    model_male = pickle.load(open('lr_bodyfat_male.pckl', 'rb'))
except FileNotFoundError:
    st.error("Error: Model file not found. Please ensure the file exists in the current directory.")
    st.stop() # Stop further execution

st.title('Body Fat Prediction')

# Select Gender
gender = st.selectbox("Select Gender", ["Male", "Female"])

# Input features
#density = st.number_input('Density', min_value=0.0, max_value=1.0)
age = st.number_input('Age', min_value=10, max_value=100)
weight = st.number_input('Weight (lbs)', min_value=50.0, max_value=500.0)
height = st.number_input('Height (inches)', min_value=36.0, max_value=100.0)
neck = st.number_input('Neck Circumference (cm)', min_value=20.0, max_value=60.0)
chest = st.number_input('Chest Circumference (cm)', min_value=50.0, max_value=200.0)
abdomen = st.number_input('Abdomen Circumference (cm)', min_value=50.0, max_value=200.0)
hip = st.number_input('Hip Circumference (cm)', min_value=50.0, max_value=200.0)
thigh = st.number_input('Thigh Circumference (cm)', min_value=30.0, max_value=100.0)
knee = st.number_input('Knee Circumference (cm)', min_value=20.0, max_value=80.0)
ankle = st.number_input('Ankle Circumference (cm)', min_value=15.0, max_value=50.0)
biceps = st.number_input('Biceps Circumference (cm)', min_value=15.0, max_value=60.0)
forearm = st.number_input('Forearm Circumference (cm)', min_value=15.0, max_value=50.0)
wrist = st.number_input('Wrist Circumference (cm)', min_value=10.0, max_value=30.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    #'Density': [density],
    'Age': [age],
    'Weight': [weight],
    'Height': [height],
    'Neck': [neck],
    'Chest': [chest],
    'Abdomen': [abdomen],
    'Hip': [hip],
    'Thigh': [thigh],
    'Knee': [knee],
    'Ankle': [ankle],
    'Biceps': [biceps],
    'Forearm': [forearm],
    'Wrist': [wrist],
})

#Button to predict
if st.button("Predict Body Fat"):
    if gender == "Female":
        model = model_female
    else:
        model = model_male

    try:
      prediction = model.predict(input_data)[0]
      st.write(f'Predicted Body Fat: {prediction:.2f}%')
    except ValueError as e:
        st.error(f"Error during prediction: {e}")
        st.error("Please check your inputs and make sure they are valid numbers.")
