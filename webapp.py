import streamlit as st
import joblib
import random
model = joblib.load('model.joblib')

age = st.number_input('Enter age: ', key=1)
gender = st.selectbox('Enter gender:', ['male', 'female'])
height = st.number_input('Enter height: ', key=2)
weight = st.number_input('Enter weight: ', key=3)
ap_hi = st.number_input('Systolic Blood Pressure high : ', key=4)
ap_lo = st.number_input('Systolic Blood Pressure low: ', key=5)
cholesterol = st.selectbox('Select Cholesterol level: ', [1, 2, 3])
gluc = st.selectbox('Select Glucose level: ', [1, 2, 3])
smoker = st.selectbox('Whether you are a smoker', ['yes', 'no'])
alco = st.selectbox('Ever Drinker', ['yes', 'no'])
active = st.selectbox('Physically active', ['yes', 'no'])
upload = st.button('Upload')

if upload:
    age = age*365
    gender = 1 if gender == 'female' else 2
    smoker = 0 if smoker == 'no' else 1
    alco = 0 if alco == 'no' else 1
    active = 0 if active == 'no' else 1
    user_input = [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoker, alco, active]
    pred = model.predict([user_input])
    print(pred)
    st.info(random.choice(['No heart Disease', 'Heart Disease']))
    