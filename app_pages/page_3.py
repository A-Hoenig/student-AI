import os
import streamlit as st
from src.data_management import load_original_data, load_cleaned_data
from src.data_management import load_image, load_pkl_file, load_text


def page_3_body():
    st.write("## DATASET")
    st.write("### Original Dataset")
    df_input = load_original_data()
    st.write(df_input)

    st.info(
        "This dataset is very comprehensive with over 30000 rows and 14"
        " Columns. Scanning through, you can see some cells containing"
        " <NA> which stands for not available. This is where the data import"
        " found a blank cell. The unnamed column is also redundant and will "
        "be removed in a later step."
    )

    st.write("### We can use a function to extract all the unique values:\n")
    unique_values = load_text(f'dataset_unique_values.txt')
    if unique_values:
        st.markdown(f"\n{unique_values}\n", unsafe_allow_html=True)

    st.write(
        "### We can summarize empty cells with a function:\n"
    )

    df = load_pkl_file(f'outputs/dataframes/dataset_missing_values.pkl')
    st.write(df)

    st.info(
        "There are many rows with missing data. Especially the transport"
        " means has 10.2% missing information. If we elimintate all rows"
        " with missing information we end up with 19243 remaining rows:"
    )

    st.image(
        load_image("dropped_rows"),
        caption='Remaining rows after missing value removal',
        width=400,
        )

    st.info(
        "Removing this much data will have a negative effect on the balance"
        " of the data as an entire row of data will be lost, even if just "
        "one field is empty. The lost data will bias the overall content and "
        "cause the ML model to lose accuracy."
    )

    st.write(
        "### Imputing Data\n"
        "Imputing data is the act of filling blank data cells with derived"
        " values that are based on the data set as a whole.\n\n"
        "* For categorical variables, one method is to fill gaps with the most"
        " common value (mode).\n"
        "* For numerical values you can add the value of the next row, or the"
        " average of all rows.\n\n"
        "For the NrSiblings column, I elected to impute the missing values "
        "using the median value. This is like using the average of all rows, "
        "but less sensitive to outliers, since a few rows show more than 5 "
        "siblings, which is unusual. This will prevent skewing the data "
        "towards having more siblings than the average would imply.\n"
        "The advantage is that all other values in the row that are not blank"
        " are still available.\n\n"
        )

    st.info(
        "I elected to impute using the **mode** to preserve all rows and data."
        "\n Once the feature analyis is complete (determining which variables "
        "actually have an effect on the score), the unneccessary data can be "
        "removed (dropped).  \n The objective is to reduce the features to as "
        "few as neccessary to simplify the model and increase speed and "
        "accuracy."

    )

    st.write(
        "### 'Cleaned' Dataset\n"
        "Below is the updated dataset with the missing "
        "data filled in. This is referred to as **'cleaned'.**\n "
    )
    df_cleaned = load_cleaned_data()
    st.write(df_cleaned)

    st.info(
        "### Dataset Variables Analysis\n"
        "The provided data set is very extensive.\n"
        "The student information (**FEATURES**) are explained below:\n\n"

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
        "I will group highschool and some highschool together to reduce "
        "complexity:\n"
        "The 5 options are then :\n"
        "- High School + Some High School\n"
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
