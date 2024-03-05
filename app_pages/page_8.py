import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_plot, load_text

def page_8_body():
    st.write("## Conclusions")
    
    st.image(
        load_image("ml_diagram"),
        caption='Types of machine learning models',
        use_column_width= 'auto',
        )
