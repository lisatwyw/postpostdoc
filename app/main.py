
import streamlit as st
import pandas as pdf

dat = pd.read_csv( 'data/' )


st.dataframe( dat ) 

