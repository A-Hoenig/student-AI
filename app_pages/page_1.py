import streamlit as st
import matplotlib.pyplot as plt

def page_1_body():
    st.write("## Project Summary")

    st.info(
        f"### Rationale\n"
        f"A private school wants to improve their student passing rate by optimizing the support for students who may stuggle to graduate.\n"
        f"\n"
        f"They have heard of machine learning but are not sure if it will be able to assist in their goals.\n"
        f"They are asking us to analyse a given data set of previous students from several locations to see if ML can gleen insights into "
        f"what factors influence a students performance the most.\n"
        f"\n"
        f"Armed with that knowledge they want to test if an ML tool could predict the final score a student will likely achieve.\n"
        f"The ultimate goal is to identify which students will need help ahead of time and ensure the neccessary steps are in place "
        f"before it is too late to intervene and a student fails")

    st.info(
        f"### Business Requirement\n"
        f"To test the viability of ML in this context, we have agreed to the following business objectives:\n"
        f"\n"
        f"1. Analyse the given dataset and identify relationships to the final student performance that might not be obvious at first glance.\n"
        f"2. Provide an interface to an ML alogrithm that, given a students data, can predict their final score and flag students who will need support.\n"
        f"3. Due to personal sensitive data being involved, the interface should be deployed on their own server and offer a simple dashboard for school counsellors.\n"
    )

    st.info(
        f"### Initial Strategy\n"
        f"To achieve the objectives the following will be implemented:\n"
        f"* Hypothesis page - narrow down the expectations\n"
        f"* Exploratory Data Analysis - assess the data and see if ML is an option\n"
        f"* Predict Page - allow counsellor to input new student info and produce a preduction\n"
        f"* Report Page - allow counsellor to upload a list of students and produce a list of students needint help\n"
        f"* Technical Explanations - for technical staff that want to follow the ML rationale and understand the process\n"
       )

    st.info(
        f"### Ethical Assessment\n"
        f"The dataset is anonymized and ethnic grouping only references Group A-E without specific race categories being named\n"
        f"This is very good for handling the data during the exploratory phase.\n"
        f"In the deployed phase the data should remain anonymized and only specific staff should have access "
        f"to lists that can link a dataset entry to a specific student at the school. This information must be protected.\n"
        f"\n"
        f"*For the purpose of this project, the ENTIRE dataset is fictitious and sourced from kaggle.com.*\n"
        f"### Dataset variables\n"
        f"In an ML context:\n"
        f"* Variables that influence another are referred to as **FEATURES.**\n"
        f"* Variables that we are interested in predicting are called **TARGET.**\n"
        f"\n"
        f"The documentation of this projecet will make frequent use of this nomenclature \n"
       )

    st.info(
        f"### Dataset Introduction\n"
        f"The provided data set was very extensive, but does contain some missing values\n"
        f"The following student information is recorded in the data set.\n"
        f"\n"
        f"#### GENDER\n"
        f"#### ETHNIC GROUP\n"
        f"#### PARENTAL EDUCATION\n"
        f"#### LUNCH TYPE\n"
        f"#### TEST PREPARATIOM\n"
        f"#### PARENT MARITAL STATUS\n"
        f"#### PRACTICE SPORT\n"
        f"#### IS FIRST CHILD\n"
        f"#### NUMBER OF SIBLINGS\n"
        f"#### TRANSPORTATION MEANS\n"
        f"#### WEEKLY STUDY HOURS\n"
        f"#### FINAL MATH SCORE\n"
        f"#### FINAL READING SCORE\n"
        f"#### FINAL WRITING SCORE\n"
    )

