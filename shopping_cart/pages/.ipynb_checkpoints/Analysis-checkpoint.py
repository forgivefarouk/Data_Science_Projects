import pandas as pd
import plotly.express as px
import streamlit as st


# Title
st.title("Shopping Cart Analysis")

# Load data
df = pd.read_csv("sources/shopping_data.csv")

st.info('### what is the total money that each gender spent ?')
con1 = st.container()
col1, col2 = con1.columns(2)

d1 = df.groupby('gender')[['total_price']].sum(
).sort_values(by='total_price', ascending=False)

col1.markdown('#### Gender')
col1.write(d1)
col2.plotly_chart(px.bar(d1, x=d1.index, y='total_price',width=450))

# import eda
#col1.write(gender_money_df)
#col2.plotly_chart(gender_money_fig)

##########################################################

st.warning('###  what is the most day that get highest income ?')
con2 = st.container()
col1, col2 = con2.columns(2)

d2 = df.groupby('name_day_order')[['total_price']].sum(
).sort_values(by='total_price', ascending=False)

col1.markdown('#### Day')
col1.write(d2)
col2.plotly_chart(px.bar(d2, x=d2.index, y='total_price',width=450))

##########################################################

st.error('###  what is the highest month that get the highest sales?')
con3 = st.container()
col1, col2 = con3.columns(2)

d3 = df.groupby('month_order')[['total_price']].sum(
).sort_values(by='total_price', ascending=False)

col1.markdown('#### Month')
col1.write(d3)
col2.plotly_chart(px.bar(d3, x=d3.index, y='total_price',width=450))

##########################################################
