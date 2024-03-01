import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_cleaned_data, load_pkl_file
from src.ml.prediction_engine import (
    maths, reading, writing)


def page_5_body():
    st.write("## Prediction Report")

    csv_file = st.file_uploader(
        "Upload CSV file student list", type=['csv'])
    
    if csv_file is not None:
        csv_file.seek(0)
        df = pd.read_csv(csv_file)
        
        # Check for missing values
        if df.isnull().values.any():
            st.error('The uploaded CSV file contains missing values.\n'
            'Please correct them and upload the file again.')
            return 
        
        subjects = ['math', 'reading', 'writing']

        # Process file
        for subject in subjects:
            st.write(f"## {subject.capitalize()} Report")
            csv_file.seek(0)
            report_df = batch_process_scores(csv_file, subject)
            
            # Display dynamic filter labels
            unique_labels = report_df[f'{subject} Prediction'].unique()
            selected_labels = st.multiselect(
                f"Filter options for {subject.capitalize()}:",
                options=unique_labels, default=unique_labels)
            
            # Filter dataframe
            filtered_df = report_df[
                report_df[f'{subject} Prediction'].isin(selected_labels)]
            
            st.dataframe(filtered_df)


def batch_process_scores(csv_file_path, score_type):
    PATH = "outputs/models/"
    VERSION = "v1"

    # load given model
    pipeline = load_pkl_file(
        f"{PATH}{score_type}/{VERSION}/{score_type}-model.pkl")
    label_map = load_pkl_file(
        f"{PATH}{score_type}/{VERSION}/{score_type}-labels.pkl")

    # load trained features
    features = pd.read_csv(
        f"{PATH}{score_type}/{VERSION}/{score_type}"
        "-train-features.csv").columns.tolist()

    # load csv from drag and drop object 
    csv_file_path.seek(0)
    students_df = pd.read_csv(csv_file_path)

    # Get row number as Student ID
    student_ids = students_df.iloc[:, 0]

    # Filter for features
    students_df = students_df.filter(features, axis=1)
    results = pd.DataFrame()

    # run predictions
    predictions = pipeline.predict(students_df)
    predictions_proba = pipeline.predict_proba(students_df)[:, 1]

    # add labels
    labels = [label_map[pred] for pred in predictions]

    # create dataframe for outout
    results['Student ID'] = student_ids
    results[f'{score_type} Prediction'] = labels
    prob = (predictions_proba * 100).round(2)
    results[f'{score_type} Probability'] = prob

    return results
