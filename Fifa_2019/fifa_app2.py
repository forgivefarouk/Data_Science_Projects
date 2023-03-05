
import streamlit as st
import pandas as pd
import plotly.express as px
import my_module as m

fifa = pd.read_csv('fifa_eda.csv')
quant_features = [col for col in fifa.columns if fifa[col].dtypes != 'O']
qualt_features = [col for col in fifa.columns if fifa[col].dtypes == 'O']
   

st.title('FIFA 2019')
st.markdown('''
This app performs simple EDA on FIFA 2019 data
''')
feature = st.selectbox('Select a feature', fifa.columns)
group = st.selectbox('Select a group',fifa.columns)
if feature in quant_features:
    m.quant_analysis(fifa, feature, group=group)
    m.quant_viz(fifa, feature)
else:
    st.write(fifa[feature].value_counts())
    
    
