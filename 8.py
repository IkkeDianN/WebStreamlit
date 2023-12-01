import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

@st.cache(suppress_st_warning=True)
def get_value(val, my_dict):    
    for key, value in my_dict.items():        
        if val == key:            
            return value

app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction']) 
if app_mode == 'Home':    
    st.title('LOAN PREDICTION :')      
    st.image('neutral.jpg')    
    st.markdown('Dataset :')    
    data = pd.read_csv('test.csv')    
    st.write(data.head())    
    st.markdown('Applicant Income VS Loan Amount ')    
    st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))