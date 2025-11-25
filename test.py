import streamlit as st

# #  For writing 
# # Webpage title
# st.title("Web App")
# # Write on page
# st.write("Hey! There")
# # header
# st.header("This is header")
# #  Subheader
# st.subheader("This is subheader")
# # text
# st.text("This is sample text")

#  SUCCESS,INFO,WARNING,ERROR Exception
st.success("success")
st.error("error")
st.info("Information")
st.warning("Warning")

exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

# checkbox
if st.checkbox("show/hide"):
    st.text("DhaaAPA")

# radio button

status = st.radio("Select Gender:",("male","Female","Neutral"))

if status == "male":
    st.success("Male")
elif status == "Female":
    st.success("Female")
else:
    st.success("Neutral")


#  DROPDOWN MENU

hobby = st.selectbox("Select Hobbies:",["Playing Cricket","Playing games","Writing"])
st.write("Your hobby is:",hobby)

# Multi Select menu
hobbies = st.multiselect("Select Hobbies:",["Playing Cricket","Playing games","Writing"])
st.write("Your hobbies are:",len(hobbies),'hobbies')

# Creating Button
st.button("Click Me")

# putting operations
if st.button("See More"):
    st.write("More options available")

# TEXT INPUT

name = st.text_input("Enter Your Name","Type Here")
if st.button("Submit"):
    st.success(name.title())

level = st.slider("Select the level",1,100)
st.text("Selected :{}".format(level))