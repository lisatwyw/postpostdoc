
import streamlit as st
import pandas as pd
from libpath import Path
import sys, os

parent_dir = os.path.dirname( os.path.realpath( __file__))
gparent_dir = os.path.dirname( parent_dir )


dat = pd.read_csv( Path( os.path.realpath( __file__) , '2023_NB_Canada.csv' ) )

mkd = '''

# Happily after PhD

## About

Various resources to help faciliate post graduation.

'''

st.markdown( mkd )
st.dataframe( dat ) 

