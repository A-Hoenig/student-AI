import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

IMAGE_PATH = "outputs/images/plots/"


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
    try:
        # Attempt to load the file
        return joblib.load(filename=file_path)
    except FileNotFoundError:
        # If not found
        return None

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

def load_text(filename):
    # Define the full path
    filepath = os.path.join(IMAGE_PATH, filename)
    
    try:
        # Load and return text
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None