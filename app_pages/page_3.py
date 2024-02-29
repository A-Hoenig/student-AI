import streamlit as st
import pandas as pd
from src.data_management import load_original_data, load_cleaned_data

def page_3_body():
    st.write("## DATASET")
    st.write("### Original Dataset")
    df_input = load_original_data()
    st.write(df_input)

    df_clean = load_cleaned_data()
    st.write(df_clean)