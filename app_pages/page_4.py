import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_pkl_file


# set global width for all pictures
WIDTH=300


def render_column_data(column):

    # Display analysis for each variable
    st.markdown("""---""")
    st.write(f"# {column}\n")
    st.image(
        load_image(f"{column}-distribution"),
        caption=f'A distribution-plot of {column} data',
        width=WIDTH,
        )
    st.image(
        load_image(f"{column}-boxplot"),
        caption=f'A box-plot of {column} data',
        use_column_width = 'auto',
        )

    st.write(f"## Exam results based on {column}")
    df = load_pkl_file(f'outputs/images/plots/{column}-data.pkl')  
    st.write(df)  


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
    
    # display individual column / variable reports
    render_column_data('Gender')
    
    st.info(
        "This shows that the expected distribution of gender among students.\n"
        "\nThe mean shows that female students on average have better results,"
        " but specifically for Maths that fact is reversed.\n\n"
        " With a difference of only 3% in average score, the effect of gender"
        " however, is **not** a major contributing factor."
    )

    render_column_data('EthnicGroup')
    st.info(
        "Shows that group C is the clear majority in this specific school,"
        " and group A is the clear minority.\n\n"
        "However, Group E, the second minority, is significantly better"
        " than the other groups, while GroupA performs the worst.\n\n"
        "With a difference of 9% on average, it is clear that EthincGroup"
        " has a significant influence on the overall score of a student."
    )

    st.write("### PARENTAL EDUCATION\n")
    st.image(
        load_image("analysis-parenteduc"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### LUNCH TYPE\n")
    st.image(
        load_image("analysis-lunchtype"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### TEST PREPARATION\n")
    st.image(
        load_image("analysis-testprep"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### PARENT MARITAL STATUS\n")
    st.image(
        load_image("analysis-marriage"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### PRACTICE SPORT\n")
    st.image(
        load_image("analysis-sport"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### FIRST CHILD\n")
    st.image(
        load_image("analysis-firstChild"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )

    st.write("### NUMBER OF SIBLINGS\n")
    st.image(
        load_image("analysis-siblings"),
        caption='caption',
        width=WIDTH,
        )
    st.info(
        "Analysis"
    )
