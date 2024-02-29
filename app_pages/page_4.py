import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image


def page_4_body():
    st.write(
        "## Exploratory Data Analysis\n"
        "To gain insight into the data meaning and possible conclusions"
        " we can use various plotting and statistical techniques to visualize"
        " the data and assess where features might be related.\n\n"
        "Below, each variable will be visualized and assessed. The average"
        " (mean) of Maths, Reading and Writing was also added to assess"
        " student overall performance related to that variable.\n"
    )

    st.write("### GENDER\n")
    st.image(
        load_image("analysis-gender"),
        caption='A plot of gender data',
        width=300,
        )
    st.info(
        "This shows that the expected distribution of gender among students.\n"
        "\nThe mean shows that female students on average have better results,"
        " but specifically for Maths that fact is reversed.\n\n"
        " With a difference of only 3% in average score, the effect of gender"
        " however, is **not** a major contributing factor."
    )

    st.write("### ETHNIC GROUP\n")
    st.image(
        load_image("analysis-ethnicgroup"),
        caption='A plot of all 5 Ethnic Groups (A-E)',
        width=300,
        )
    st.info(
        "Shows that group C is the clear majority in this specific school,"
        " and group A is the clear minority.\n\n"
        "However, Group E, the second minority, is significantly better"
        " than the other groups, while GroupA performs the worst.\n\n"
        "With a difference of 9% on average, it is clear that EthincGroup"
        " has a significant influence on the overall score of a student."
    )

    st.write("### VAR\n")
    st.image(
        load_image(" "),
        caption='caption',
        width=300,
        )
    st.info(
        "Analysis"
    )