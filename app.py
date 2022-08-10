# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import warnings
import sklearn

pickle_in = open("RandomForest.pkl","rb")
classifier = pickle.load(pickle_in)


def predict_crop(N,P,K,Temp,Hum,Ph,Rainfall):
    prediction = classifier.predict([[N,P,K,Temp,Hum,Ph,Rainfall]])
    print(prediction)
    return prediction


def welcome():
    return "Welcome"

def main():
    st.title("Crop Prediction")
    html_temp = """
      <div style="background-color:orange;padding:10px">
      <h2 style="color:white;text-align:center;">Streamlit Crop Predictor ML App by Hardik</h2>
      </div>
      """
    st.markdown(html_temp, unsafe_allow_html=True)
    N = st.text_input("Nitrogren")
    P = st.text_input("Phosphorus")
    K = st.text_input("Pottasium")
    Temp = st.text_input("Temprature")
    Hum = st.text_input("Humidity")
    Ph = st.text_input("PH Value")
    Rainfall = st.text_input("Rainfall")
    result = ""
    if st.button("Predict"):
        try:
            result = predict_crop(N,P,K,Temp,Hum,Ph,Rainfall)
            st.title("You should grow "+result[0]+" in your area")
        except Exception as e:
            st.title(e)
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with ❤ by Hardik")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

