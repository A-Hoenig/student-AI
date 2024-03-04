import streamlit as st
import matplotlib.pyplot as plt


def page_1_body():
    st.write("## Project Summary")

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
        "3. Due to personal data being involved, the interface should be "
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
        "produce a report of students likely to need help\n"
        "* Technical Explanations - for technical staff that want to follow"
        " the ML rationale and understand the process."
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
        "* Variables that influence another are referred to as **FEATURES.**\n"
        "* Variables that we are want to predict are called **TARGET.**\n"
        "* Categorical Variables assign a category. male/female, true/false,"
        " 1 or 2 or 3 etc\n"
        "* Numerical Variables are continuous between 2 limits and can be"
        " integers or even decimals\n\n"
        "This project will frequently use ML nomenclature."
    )

    st.info(
        "### Dataset Introduction\n"
        "The provided data set was very extensive, but contained some missing"
        "values.\n The following student information (**FEATURES**) are in the"
        " data set.\n\n"

        "#### GENDER (Categorical)\n"
        "Two values only (non binary / none not considered).\n"
        "* Male\n"
        "* Female\n"

        "#### ETHNIC GROUP (Categorical)\n"
        "5 groups in total. "
        "No reference made to which group is which ethnicity.\n"
        "* Group A\n"
        "* Group B\n"
        "* Group C\n"
        "* Group D\n"
        "* Group E\n"

        "#### PARENTAL EDUCATION (Categorical)\n"
        "Indicates the level of education the parents of the student have.\n"
        "The 6 options are:\n"
        "- Some High School\n"
        "- High School\n"
        "- Some College\n"
        "- Associate's Degree\n"
        "- Bachelor's Degree\n"
        "- Master's Degree\n"

        "#### LUNCH TYPE (Categorical)\n"
        "Two values only. The assumption made was that Standard indicates a "
        "homemade lunch whereas free/reduced indicates some kind of government"
        " assistance program.\n"
        "* Standard\n"
        "* Free / Reduced\n"

        "#### TEST PREPARATION (Categorical)\n"
        "Two values only. Self explanatory.\n"
        "* Completed\n"
        "* None\n"

        "#### PARENT MARITAL STATUS (Categorical)\n"
        "4 options in dataset.\n"
        "* Married\n"
        "* Single\n"
        "* Divorced\n"
        "* Widowed\n"

        "#### PRACTICE SPORT (Categorical)\n"
        "3 options in dataset.\n"
        "* Regularly\n"
        "* Sometimes\n"
        "* Never\n"

        "#### IS FIRST CHILD (Categorical)\n"
        "Binary option Yes/No.\n"
        "* Yes\n"
        "* No\n"

        "#### NUMBER OF SIBLINGS (Categorical/Numerical)\n"
        "This variable is categorical OR numerical. The dataset contains "
        "values from 0 to 7. "
        "Theoretically the number could be much higher also.\n"
        "* 0\n"
        "* 1\n"
        "* 2\n"
        "* 3\n"
        "* 4\n"
        "* 5\n"
        "* 6\n"
        "* 7\n"

        "#### TRANSPORTATION MEANS (Categorical)\n"
        "Binary option.\n"
        "* School bus\n"
        "* Private\n"

        "#### WEEKLY STUDY HOURS (Categorical/Numerical)\n"
        "This can also be a numerical variable. This dataset is grouped into"
        " 3 categories.\n"
        "* '< 5'\n"
        "* '5 - 10'\n"
        "* '> 10'\n\n"

        "#### TARGET variables (Numerical)\n"
        "Numerical Value from 0-100. The presumption is that it is a standard"
        " percent value.\n"
        "No information is given to a specific passing grade or "
        "classification of performance.\n"
        "All values are integers (ie no decimal value).\n"
        "* FINAL MATH SCORE **(TARGET)**\n"
        "* FINAL READING SCORE **(TARGET)**\n"
        "* FINAL WRITING SCORE **(TARGET)**\n"
    )

    st.write("the detailed files behind this project can be viewed here:\n\n"
        "https://github.com/A-Hoenig/student-AI"
    )
    