import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simple Streamlit application.")

##create a simple dataframe
data = {
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": ["A", "B", "C", "D", "E"],
    "Column 3": [10.5, 20.5, 30.5, 40.5, 50.5]
}
df = pd.DataFrame(data)

## Display the dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)


##create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)