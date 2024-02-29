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
        f"* Predict Page - allow counsellor to input new student info and make a prediction\n"
        f"* Report Page - allow counsellor to upload a list of students and produce a report of students likely to need help\n"
        f"* Technical Explanations - for technical staff that want to follow the ML rationale and understand the process\n"
       )

    st.info(
        f"### Ethical Assessment\n"
        f"The dataset is anonymized and ethnic grouping only references Group A-E without specific race categories being named.\n"
        f"This is useful for handling the data during the exploratory phase.\n"
        f"In the deployed phase the data should remain anonymized and only specific staff should have access "
        f"to lists that can link a dataset entry to a specific student at the school. This information must be protected.\n"
        f"\n"
        f"*For the purpose of this project, the ENTIRE dataset is fictitious and sourced from kaggle.com.*\n"
        f"### Machine Learning Terms\n"
        f"In an ML context:\n"
        f"* Variables that influence another are referred to as **FEATURES.**\n"
        f"* Variables that we are interested in predicting are called **TARGET.**\n"
        f"* Categorical Variables assign a category such as male/female, true/false, 1 or 2 or 3 etc\n"
        f"* Numerical Variables have a continuous value between 2 limits and can be integers or even decimals\n"
        f"\n"
        f"The documentation of this project will make frequent use of this nomenclature \n"
       )

    st.info(
        f"### Dataset Introduction\n"
        f"The provided data set was very extensive, but does contain some missing values\n"
        f"The following student information (**FEATURES**) are recorded in the data set.\n"
        f"\n"

        f"#### GENDER (Categorical)\n"
        f"Two values only (non binary / none not considered).\n"
        f"* Male\n"
        f"* Female\n"

        f"#### ETHNIC GROUP (Categorical)\n"
        f"5 groups in total. No reference made to which group is which ethnicity.\n"
        f"* Group A\n"
        f"* Group B\n"
        f"* Group C\n"
        f"* Group D\n"
        f"* Group E\n"

        f"#### PARENTAL EDUCATION (Categorical)\n"
        f"Indicates the level of education the parents of the student have.\n"
        f"The 6 options are:\n"
        f"- Some High School\n"
        f"- High School\n"
        f"- Some College\n"
        f"- Associate's Degree\n"
        f"- Bachelor's Degree\n"
        f"- Master's Degree\n"

        f"#### LUNCH TYPE (Categorical)\n"
        f"Two values only. The assumption made was that Standard indicates"
        f" a homemade lunch whereas free/reduced indicates some kind of government"
        f" assistance program.\n"
        f"* Standard\n"
        f"* Free / Reduced\n"

        f"#### TEST PREPARATION (Categorical)\n"
        f"Two values only. Self explanatory.\n"
        f"* Completed\n"
        f"* None\n"

        f"#### PARENT MARITAL STATUS (Categorical)\n"
        f"4 options in dataset.\n"
        f"* Married\n"
        f"* Single\n"
        f"* Divorced\n"
        f"* Widowed\n"

        f"#### PRACTICE SPORT (Categorical)\n"
        f"3 options in dataset.\n"
        f"* Regularly\n"
        f"* Sometimes\n"
        f"* Never\n"

        f"#### IS FIRST CHILD (Categorical)\n"
        f"Binary option Yes/No.\n"
        f"* Yes\n"
        f"* No\n"

        f"#### NUMBER OF SIBLINGS (Categorical/Numerical)\n"
        f"This variable can be seen as categorical or numerical. The dataset contains"
        f" values from 0 to 7. Theoretically the number could be much higher also.\n"
        f"* 0\n"
        f"* 1\n"
        f"* 2\n"
        f"* 3\n"
        f"* 4\n"
        f"* 5\n"
        f"* 6\n"
        f"* 7\n"
       
        f"#### TRANSPORTATION MEANS (Categorical)\n"
        f"Binary option.\n"
        f"* School bus\n"
        f"* Private\n"

        f"#### WEEKLY STUDY HOURS (Categorical/Numerical)\n"
        f"This could also be a numerical variable. In this dataset it is grouped into"
        f" 3 categories.\n"
        f"* '< 5'\n"
        f"* '5 - 10'\n"
        f"* '> 10'\n"

        f"\n"
        f"#### TARGET variables (Numerical)\n"
        f"Numerical Value from 0 - 100. The presumption is that it is a standard percent value.\n"
        f"No information is given to a specific passing grade or classification of performance.\n"
        f"All values are integers (ie no decimal value).\n"
        f"* FINAL MATH SCORE **(TARGET)**\n"
        f"* FINAL READING SCORE **(TARGET)**\n"
        f"* FINAL WRITING SCORE **(TARGET)**\n"
    )

