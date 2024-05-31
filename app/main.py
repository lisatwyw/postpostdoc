
import streamlit as st
import pandas as pd
from pathlib import Path
import sys, os


# ================================ config ================================ 
st.set_page_config(layout="wide") 

# ================================ admin ================================ 
parent_dir = os.path.dirname( os.path.realpath( __file__))  # /mount/src/postpostdoc/app/main.py 
gparent_dir = os.path.dirname( parent_dir )

# ================================ data ================================ 
f =  Path( parent_dir, '2023_NB_Canada.csv.csv' )
dat = pd.read_csv(f )

st.write( gparent_dir )
st.write( parent_dir)
st.write( f )

# ================================ app body ================================ 

mkd = '''
# Happily after PhD

## About

Various resources to help faciliate post graduation.

'''

st.markdown( mkd )
st.dataframe( dat ) 

