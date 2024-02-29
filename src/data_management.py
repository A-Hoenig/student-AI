import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

IMAGE_PATH = "outputs/images/"


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_original_data():
    df = pd.read_csv("inputs/dataset/Expanded_data_with_more_features.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_cleaned_data():
    df = pd.read_csv(
        "outputs/dataset/Expanded_data_with_more_features_clean.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

def load_image(image_name):
    # possible extensions
    extensions = ['.png', '.jpg', '.jpeg', '.gif']
    
    for ext in extensions:
        try:
            # Attempt to open the image with each extension
            full_path = f"{IMAGE_PATH}{image_name}{ext}"
            image = Image.open(full_path)
            return image
        except FileNotFoundError:
            # If not found continue to the next extension type
            continue
    
    # no file is found 
    image = Image.open("src/doc_images/image-not-found.jpeg")
    return image