import streamlit as st
import pandas as pd
import matplotlib as plt

st.write("""
    # Anaslysing Austiran parliamentary speeches 
    This dashboard gives an overview over the speeches included in the ParlSpeechV2 dataset 
    It shows the probability distrbution over all parties and represents the results of my masters thesis. 
    You can explore the data by your self and even download the data sets. 
""")
# read final data set
filename = "data/processed_results.xlsx"
df = pd.read_excel(filename, index_col=0)