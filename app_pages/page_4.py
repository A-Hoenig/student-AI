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




