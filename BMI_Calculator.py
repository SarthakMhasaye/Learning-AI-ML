import streamlit as st

#  Title of webpage
st.title("BMI CALCULATOR")

#  Asking for weight 
weight = st.number_input("Enter your weight (in kgs)")

#  Take height
height_unit = st.radio("Select your height format",('cms','meter','feet'))

bmi = 0
if height_unit == 'cms':
    height = st.number_input("Centimeters")
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

if height_unit == 'meter':
    height = st.number_input("meters")
    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")


if height_unit == 'feet':
    height = st.number_input("feet")
    try:
        bmi = weight / ((height/3.20)**2)
    except:
        st.text("Enter some value of height")

#  >Check if button is clicked or not
if st.button('Calculate BMI'):
    # print BMI index
    st.subheader("Your bmi index is {}".format(bmi))

    if bmi<16:
        st.error("uo are extremly underweight.")
    elif(bmi>=16 and bmi < 18.5):
        st.warning("Your are extremly under weight")
    elif(bmi>=18.5 and bmi <25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.warning("Extremly over weight")