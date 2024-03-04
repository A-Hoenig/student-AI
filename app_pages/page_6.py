import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_cleaned_data, load_pkl_file
from src.ml.prediction_engine import (
    maths, reading, writing)


def page_6_body():
    st.write("## Prediction Engine")

    st.info(
        "This page uses the generated ML models to predict whether or not"
        " a student might need help during their school year.\n\n"
        "Select the specific student criteria and press calculate predictions"
        " to see the result.\n"
    )

    PATH = "outputs/models/"
    VERSION = "v2"

    # load model files
    TYPE = "math"
    math_pipeline = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-model.pkl")

    math_label_map = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-labels.pkl")

    math_features = pd.read_csv(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-train-features.csv"
        ).columns.to_list()

    TYPE = "reading"
    reading_pipeline = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-model.pkl")

    reading_label_map = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-labels.pkl")

    reading_features = pd.read_csv(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-train-features.csv"
        ).columns.to_list()

    TYPE = "writing"
    writing_pipeline = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-model.pkl")

    writing_label_map = load_pkl_file(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-labels.pkl")

    writing_features = pd.read_csv(
        f"{PATH}{TYPE}/{VERSION}/{TYPE}-train-features.csv"
        ).columns.to_list()

    # Acquire live data
    input_features = AcquireInputs()

    if st.button("Calculate Predictions"):
        maths(
            input_features, math_features, math_pipeline, math_label_map)

        reading(
            input_features, reading_features, reading_pipeline, reading_label_map)

        writing(
            input_features, writing_features, writing_pipeline, writing_label_map)

def AcquireInputs():

    df = load_cleaned_data()

    column1, column2, column3 = st.beta_columns(3)

    input_features = pd.DataFrame([], index=[0])

    with column1:
        feature = 'EthnicGroup'
        streamlit_widget = st.radio(
            label=feature,
            options=sorted(df[feature].unique())
        )
    input_features[feature] = streamlit_widget

    with column2:
        feature = 'ParentEduc'
        streamlit_widget = st.radio(
            label=feature,
            options=df[feature].unique()
        )
    input_features[feature] = streamlit_widget

    with column3:
        feature = 'LunchType'
        streamlit_widget = st.radio(
            label=feature,
            options=df[feature].unique()
        )
    input_features[feature] = streamlit_widget

    # with column4:
    #     feature = 'TestPrep'
    #     streamlit_widget = st.selectbox(
    #         label=feature,
    #         options=df[feature].unique()
    #     )
    # input_features[feature] = streamlit_widget

    return input_features