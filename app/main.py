
import streamlit as st
import pandas as pd

dat = pd.read_csv( '2023_NB_Canada.csv' )

mkd = '''

# Happily after PhD

## About

Various resources to help faciliate post graduation.

'''

st.markdown( mkd )
st.dataframe( dat ) 

