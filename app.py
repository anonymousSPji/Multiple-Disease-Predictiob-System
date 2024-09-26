# -*- coding: utf-8 -*-
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_model.sav', 'rb'))

# Page Layout
st.markdown("""
    <style>
    .main { background-color: #F0F2F6; }
    .stButton>button { background-color: #4CAF50; color: white; }
    .stTabs>div>div { border-bottom: 4px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# Tab Navigation
tabs = st.tabs(["Diabetes Prediction", "Heart Disease Prediction"])

# Diabetes Prediction
with tabs[0]:
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    Pregnancies = col1.slider('Number of Pregnancies', 0, 20, 0)
    Glucose = col2.slider('Glucose Level', 0, 200, 120)
    BloodPressure = col3.slider('Blood Pressure value', 0, 200, 80)
    SkinThickness = col1.slider('Skin Thickness value', 0, 100, 20)
    Insulin = col2.slider('Insulin Level', 0, 900, 30)
    BMI = col3.slider('BMI value', 0.0, 70.0, 25.0)
    DiabetesPedigreeFunction = col1.slider('Diabetes Pedigree Function value', 0.0, 2.5, 0.5)
    Age = col2.slider('Age of the Person', 0, 100, 25)

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

    # Heart Disease Prediction
    # with tabs[1]:
    #     st.title('Heart Disease Prediction using ML')
    #     col1, col2, col3 = st.columns(3)
        
    #     age = col1.slider('Age', 0, 100, 50)
    #     sex = col2.radio('Sex', ['Male', 'Female'])
    #     cp = col3.selectbox('Chest Pain types', ['Type 1', 'Type 2', 'Type 3', 'Type 4'])
    #     trestbps = col1.slider('Resting Blood Pressure', 0, 200, 120)
    #     chol = col2.slider('Serum Cholestoral in mg/dl', 100, 600, 200)
    #     fbs = col3.radio('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    #     restecg = col1.radio('Resting Electrocardiographic results', ['Normal', 'Abnormal'])
    #     thalach = col2.slider('Maximum Heart Rate achieved', 50, 220, 150)
    #     exang = col3.radio('Exercise Induced Angina', ['Yes', 'No'])
    #     oldpeak = col1.slider('ST depression induced by exercise', 0.0, 10.0, 1.0)
    #     slope = col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
    #     ca = col3.slider('Major vessels colored by flourosopy', 0, 4, 0)
    #     thal = col1.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])

    #     if st.button('Heart Disease Test Result'):
    #         user_input = [age, 1 if sex == 'Male' else 0, cp, trestbps, chol, 1 if fbs == 'Yes' else 0, restecg, thalach, 
    #                       1 if exang == 'Yes' else 0, oldpeak, slope, ca, thal]
    #         heart_prediction = heart_disease_model.predict([user_input])
    #         heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
    #         st.success(heart_diagnosis)

# Heart Disease Prediction
with tabs[1]:
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    age = col1.slider('Age', 0, 100, 50)
    sex = col2.radio('Sex', ['Male', 'Female'])
    cp = col3.selectbox('Chest Pain types', ['Type 1', 'Type 2', 'Type 3', 'Type 4'])
    trestbps = col1.slider('Resting Blood Pressure', 0, 200, 120)
    chol = col2.slider('Serum Cholestoral in mg/dl', 100, 600, 200)
    fbs = col3.radio('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    restecg = col1.radio('Resting Electrocardiographic results', ['Normal', 'Abnormal'])
    thalach = col2.slider('Maximum Heart Rate achieved', 50, 220, 150)
    exang = col3.radio('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = col1.slider('ST depression induced by exercise', 0.0, 10.0, 1.0)
    slope = col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = col3.slider('Major vessels colored by flourosopy', 0, 4, 0)
    thal = col1.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])

    if st.button('Heart Disease Test Result'):
        # Convert inputs to numeric values
        cp_mapping = {'Type 1': 0, 'Type 2': 1, 'Type 3': 2, 'Type 4': 3}
        restecg_mapping = {'Normal': 0, 'Abnormal': 1}
        slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
        thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversable Defect': 2}

        user_input = [
            age,
            1 if sex == 'Male' else 0,
            cp_mapping[cp],
            trestbps,
            chol,
            1 if fbs == 'Yes' else 0,
            restecg_mapping[restecg],
            thalach,
            1 if exang == 'Yes' else 0,
            oldpeak,
            slope_mapping[slope],
            ca,
            thal_mapping[thal]
        ]

        # Ensure input is in the correct format for the model
        user_input = [float(i) for i in user_input]  # Convert all inputs to floats

        # Predict
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(heart_diagnosis)


# # Breast Cancer Prediction Tab (Dummy for UI Consistency)
# with tabs[2]:
#     st.title("Parkinson's Prediction coming soon...")
#     st.write("This feature is under development.")
# # Breast Cancer Prediction Tab (Dummy for UI Consistency)
# with tabs[3]:
#     st.title("Breast Cancer Prediction coming soon...")
#     st.write("This feature is under development.")
