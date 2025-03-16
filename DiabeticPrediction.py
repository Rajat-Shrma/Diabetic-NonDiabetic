import pickle
import pandas as pd
import sklearn
import streamlit as st
import numpy as np
import time as t
load_model=pickle.load(open('diabeticPrediction.sav','rb'))
def check(input_data):
    if load_model.predict(input_data)==1:
        return "Negative"
    else:
        return "Positive"
    

    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
st.title("Diabetic Prediction Web App")
Pregnancies= st.slider("No. of Pregnancies",0,20)
Glucose= st.text_input("Glucose level")
BloodPressure= st.text_input("Blood pressure")
SkinThickness= st.text_input("Skin Thickness")
Insulin= st.text_input("Insulin")
BMI= st.text_input("BMI")
DiabetesPF= st.text_input("DiabetesPedigreeFunction")
Age= st.text_input("Age")
data=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPF,Age]
input_narray=np.asarray(data)
input_data=input_narray.reshape(1,-1)
if st.button("Report"):
        
    st.spinner("just wait")
    with st.spinner("just wait"):
        t.sleep(2)

    report=check(input_data)
    if report=="Positive":
        st.success("You Non diabetic Person")
    else:
        st.warning("You are a diabetic Person.Get yourself checked!")
