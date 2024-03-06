import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_plot


def page_1_body():
    st.write("## Project Summary")

    st.image(
        load_image("title"),
        use_column_width='auto',
        )

    st.info(
        "### Rationale\n"
        "A private school wants to improve their student passing rate by "
        "optimizing the support for students who may struggle to graduate.\n\n"
        "They have heard of machine learning but are not sure if it will "
        "be able to assist in their goals. They are asking us to analyse a "
        "given data set of previous students from all locations to see if ML"
        " can get insights into what factors influence a students performance"
        " the most.\n\n"
        "Armed with that knowledge they want to test if an ML tool could "
        "predict the final score a student will likely achieve. The ultimate"
        " goal is to identify which students will need help ahead of time and "
        "ensure the necessary steps are in place before it is too late to "
        "intervene and a student fails."
    )

    st.info(
        "### Business Requirement\n"
        "To test the viability of ML in this context, we have agreed to the "
        "following business objectives:\n\n"
        "1. Analyse the given dataset and identify relationships to the final "
        "student performance that might not be obvious at first glance.\n"
        "2. Provide an interface to an ML algorithm that, given a student's"
        " data, can predict their final score and flag students who will need "
        "support.\n"
        "3. A dashboard should be created as the interface to the model. "
        "The school wishes to predict individual students or process an "
        "entire class by uploading a csv file.\n"
        "4. Due to personal data being involved, the interface should be "
        "deployed on their own server and offer a simple dashboard for school"
        " counsellors."
    )

    st.info(
        "### Initial Strategy\n"
        "To achieve the objectives the following will be implemented:\n"
        "* Hypothesis page - narrow down the expectations\n"
        "* Exploratory Data Analysis- assess data and see if ML is an option\n"
        "* Predict Page - allow counsellor to add new student info and make a"
        " prediction\n"
        "* Report Page - allow counsellor to upload a list of students and"
        " produce a report of students likely to need help\n"
        "* Technical Explanations - for technical staff that want to follow"
        " the ML rationale and understand the process"
    )

    st.info(
        "### Ethical Assessment\n"
        "The dataset is anonymized and ethnic grouping only references Group"
        "A-E without specific race categories being named. This is useful for"
        " handling the data in the exploratory phase. In the deployed phase, "
        "the data should remain anonymized and only specific staff must have "
        "access to lists that can link an entry to a specific student at the "
        "school. This information must be protected.\n\n"
        "*For the purpose of this project, the all data is fictitious and "
        "sourced from kaggle.com.*\n"
        "### Machine Learning Terms\n"
        "In an ML context:\n"
        "* Variables that influence another are referred to as **FEATURES**\n"
        "* Variables that we are want to predict are called **TARGET**\n"
        "* Categorical Variables assign a category. Male/Female, True/False,"
        " 1 or 2 or 3,  etc\n"
        "* Numerical Variables are continuous between 2 limits and can be"
        " integers or even decimals\n\n"
        "This project will frequently use ML nomenclature."
    )

    st.write(
        "the detailed files behind this project can be viewed here:\n\n"
        "https://github.com/A-Hoenig/student-AI"
    )
