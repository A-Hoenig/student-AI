import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
from pandas.plotting import table

IMAGE_PATH = "outputs/images/"
PLOT_PATH = "outputs/plots/"
DF_PATH = "outputs/dataframes/"
TXT_PATH = "outputs/test/"


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
    

def load_plot(image_name):
    # possible extensions
    extensions = ['.png', '.jpg', '.jpeg', '.gif']
    
    for ext in extensions:
        try:
            # Attempt to open the image with each extension
            full_path = f"{PLOT_PATH}{image_name}{ext}"
            image = Image.open(full_path)
            return image
        except FileNotFoundError:
            # If not found continue to the next extension type
            continue
    
    # no file is found 
    image = Image.open("src/doc_images/plot-not-found.png")
    return image


def load_text(filename):
    # Define the full path
    filepath = os.path.join(TXT_PATH, filename)
    
    try:
        # Load and return text
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


def save_plot(figure, filename, directory=PLOT_PATH):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the full path
    filepath = os.path.join(directory, filename)

    # If a file with the same name already exists, remove it
    if os.path.isfile(filepath):
        os.remove(filepath)

    # Save the figure
    figure.savefig(filepath, bbox_inches='tight')


def save_df(df, filename, directory=DF_PATH):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the full path
    filepath = os.path.join(directory, filename)

    # If a file with the same name already exists, remove it
    if os.path.isfile(filepath):
        os.remove(filepath)

    # Save the DataFrame using pickle
    with open(filepath, 'wb') as file:
        pickle.dump(df, file)


def save_analysis(text, filename, directory=TXT_PATH):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Define the full path
    filepath = os.path.join(directory, filename)
    
    # If a file with the same name already exists, remove it
    if os.path.isfile(filepath):
        os.remove(filepath)
    
    # Save the text
    with open(filepath, 'w') as file:
        file.write(text)