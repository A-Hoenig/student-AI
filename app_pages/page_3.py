import os
import streamlit as st
import pandas as pd
from src.data_management import load_original_data, load_cleaned_data, load_image


def page_3_body():
    st.write("## DATASET")
    st.write("### Original Dataset")
    df_input = load_original_data()
    st.write(df_input)

    st.info(
        "This dataset is very comprehensive with over 30000 rows and 14"
        " Columns. Scanning through, you can see some cells containing"
        " NaN which stands for Not a Number. This is where the data import"
        " found a blank cell. The unnamed column is also redundant and will "
        "be removed in a later step. We can summarize the empty cells with a "
        "function:\n"
    )
    
    st.image(
        load_image("EDA.png"),
        caption='Your caption here',
        use_column_width=True)


    df_clean = load_cleaned_data()
    st.write(df_clean)