import numpy as np
import pandas as pd 
import streamlit as st 

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x','y'])
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)