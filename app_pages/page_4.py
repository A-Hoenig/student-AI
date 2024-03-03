import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_pkl_file, load_text


# set global variables
# std histogram width
WIDTH=300

#Columns user can select in dropdown
columns_list = ['Gender', 'EthnicGroup', 'ParentEduc', 'LunchType', 
                    'TestPrep', 'ParentMaritalStatus', 'PracticeSport', 
                    'IsFirstChild', 'NrSiblings', 'TransportMeans']


def render_column_data(column):

    # Display analysis for each variable/column
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

    mean_max = df['MeanScore'].iloc[0]
    mean_min = df['MeanScore'].iloc[-1]
    spread = mean_max - mean_min
    spread_rounded = round(spread, 2)
    st.warning(f'**Mean Range: {spread_rounded}**')

    analysis = load_text(f'{column}-analysis.txt')
    if analysis:
        st.info(analysis)


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

    selected_column = st.radio(
        'Select a variable for analysis:', columns_list)

    render_column_data(selected_column)


    # # display individual column / variable reports
    # render_column_data('Gender')
    
    # st.info(
    #     "This shows that the expected distribution of gender among students.\n"
    #     "\nThe mean shows that female students on average have better results,"
    #     " but specifically for Maths that fact is reversed.\n\n"
    #     " With a difference of only 3% in average score, the effect of gender"
    #     " however, is **not** a major contributing factor."
    # )

    # render_column_data('EthnicGroup')
    # st.info(
    #     "Shows that group C is the clear majority in this specific school,"
    #     " and group A is the clear minority.\n\n"
    #     "However, Group E, the second minority, is significantly better"
    #     " than the other groups, while GroupA performs the worst.\n\n"
    #     "With a difference of 9% on average, it is clear that EthincGroup"
    #     " has a significant influence on the overall score of a student."
    # )

