import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name= st.text_input("Enter your name", "Type Here...")

if name:
    st.write(f"Hello {name}!")
else:
    st.write("Please enter your name above.")



st.title("Streamlit Slider Input")

age = st.slider("Select your age", 0, 100, 25)
if age:
    st.write(f"You are {age} years old.")
else:
    st.write("Please select your age above.")

st.title("Streamlit Selectbox Input")

options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an option", options)

if selected_option:
    st.write(f"You selected: {selected_option}")
else:
    st.write("Please select an option above.")  


st.title("DataFrame Display")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
st.write(df)


uploaded_file=st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write(df_uploaded)
else:
    st.write("Please upload a CSV file to display its contents.")