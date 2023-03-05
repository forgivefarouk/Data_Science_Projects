import pandas as pd
import plotly.express as px
import streamlit as st


# Title
st.title("Shopping Cart Stats")

# Load data
df = pd.read_csv("sources/shopping_data.csv")

# container
con1 = st.container()

total_sales = df['total_price'].sum()
total_orders = df['order_id'].nunique()
total_items = df['quantity_sales'].sum()

col1, col2, col3 = con1.columns(3)
col1.metric("Total Sales ($) ", format(total_sales, ',.2f'))
col2.metric("Total Orders", format(total_orders, ',.0f'))
col3.metric("Total Items", format(total_items, ',.0f'))
