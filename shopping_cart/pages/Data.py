import pandas as pd
import streamlit as st


# Title
st.title("Shopping Cart Data")

# Load data
df = pd.read_csv("sources/shopping_data.csv")

# Show data
st.write(df)
