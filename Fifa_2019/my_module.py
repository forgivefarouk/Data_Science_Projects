
import streamlit as st
import pandas as pd
import plotly.express as px

def quant_analysis(df, col, group=None, n=5):
    st.write(f'Average {col} of Players (Mean , Median): ', round(df[col].mean(), 1),',', round(df[col].median(),1))
    st.write(f'Maximum {col} of Players: ', df[col].max(),'----> Player : ', df[df[col] == df[col].max()]['Name'].values[0])
    st.write(f'Minimum {col} of Players: ', df[col].min(),'----> Player : ', df[df[col] == df[col].min()]['Name'].values[0])    
    st.write('-'*50)
    if group:
        st.write(f'Largest Average {col} per {group} : ', df.groupby([group])[col].median().nlargest(n))
        st.write(f'Smallest Average {col} per {group} : ', df.groupby([group])[col].median().nsmallest(n))

def quant_viz(df, x, y= None, group=None, query=None):
    if y:
        st.plotly_chart(px.scatter(df, x=x, y=y, title=f'Scatter Plot of {x} vs {y}', width=500, height=500)) 
    else: 
        col1, col2 = st.columns(2)  
        col1.plotly_chart(px.histogram(df, x=x, nbins=20, title=f'Histogram of {x}', width=500, height=400)) 
        col2.plotly_chart(px.box(df, y=x, title=f'Box Plot of {x}', width=500, height=500)) 
        if group:
            st.plotly_chart(px.box(df[df[group] == query] ,y=x, title=f'Box Plot of {x} for {group} : {query}', width=1000, height=500)) 
