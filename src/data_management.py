import os
import io
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from PIL import Image
from pandas.plotting import table
from sklearn.metrics import classification_report, confusion_matrix

IMAGE_PATH = "outputs/images/"
PLOT_PATH = "outputs/plots/"
DF_PATH = "outputs/dataframes/"
TXT_PATH = "outputs/text/"


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


def confusion_matrix_and_report(x, y, pipeline, label_map):
    output = io.StringIO()
    prediction = pipeline.predict(x)

    # Confusion matrix to markdown table
    cm_df = pd.DataFrame(confusion_matrix(y, prediction),
                         columns=[f"Actual {sub}" for sub in label_map],
                         index=[f"Prediction {sub}" for sub in label_map])
    output.write('#### Confusion Matrix\n\n')
    output.write(cm_df.to_markdown())
    output.write("\n\n")

    # Classification Report to markdown table
    report = classification_report(y, prediction,
                                   target_names=label_map,
                                   output_dict=True)
    report_df = pd.DataFrame(report).transpose()

    # Ensure 'support' is int before rounding
    report_df['support'] = report_df['support'].apply(
        lambda x: '' if pd.isna(x) else int(x))
    report_df = report_df.round(3)

    # Adjust accuracy row
    if 'accuracy' in report_df.index:
        accuracy = report_df.loc['accuracy', 'f1-score']
        report_df.loc['accuracy', ['precision', 'recall', 'support']] = ""
        report_df.loc['accuracy', 'f1-score'] = accuracy

    output.write('#### Classification Report\n\n')
    output.write(report_df.to_markdown())
    output.write("\n")

    return output.getvalue()


def clf_performance(
        train_features, train_scores,
        test_features, test_scores,
        pipeline, label_map, column):

    # Column Title
    column_cap = column.capitalize()

    # Train set analysis
    train_title = f"{column_cap} - Train Set\n\n"
    train_report = train_title + confusion_matrix_and_report(
        train_features, train_scores, pipeline, label_map)
    save_analysis(train_report, f'confusion-matrix-{column}-train.txt')
    print(train_report)

    # Test set analysis,
    test_title = f"{column_cap} - Test Set\n\n"
    test_report = test_title + confusion_matrix_and_report(
        test_features, test_scores, pipeline, label_map)
    save_analysis(test_report, f'confusion-matrix-{column}-test.txt')
    print(test_report)
