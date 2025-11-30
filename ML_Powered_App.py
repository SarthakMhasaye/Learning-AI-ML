#  INSTALL matplotlib and scikit-
import streamlit as st
import pickle
import numpy as np

# TITLE
st.title("HOME PRICE CALCULATOR")\

#user input
area =st.number_input("Enter the number:",500,10000)
rooms = st.slider("Number of rooms:",1,10)

model = pickle.load(open("Houcepricemodel.pkl","rb"))

# Predict price
if st.button("Predict price"):
    features = np.array([[area,rooms]])
    prediction = model.predict(features)
    st.write(f"Predicted Price: ${prediction[0]:,.2f}")