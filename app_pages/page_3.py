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
        "be removed in a later step. We can summarize the empty cells with a "
        "function:\n"
    )
    
    df = load_pkl_file(f'outputs/dataframes/dataset_missing_values.pkl')  
    st.write(df)

    st.info(
        "Those are many rows with missing data. Especially the transport"
        " means has 10.2% missing information. If we elimintate all rows"
        " with missing information we end up with 19243 remaining rows:"
    )

    unique_values = load_text(f'dataset_unique_values.txt')
    if unique_values:
        st.markdown(f"\n{unique_values}\n", unsafe_allow_html=True)


    st.image(
        load_image("dropped_rows"),
        caption='Remaining rows after missing value removal',
        width=400,
        )

    st.info(
        "removing this much data will have a negative effect on the balance"
        " of the data. A detailed report can be generated using pandas"
        " python library. The quick result is summarized below:\n"
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
        "I elected to impute using the mode to preserve all rows and data.\n"
        "Additionlly I decided to drop the **Transport Means** variable as "
        "it had the most missing values and would likely not contribute much "
        "to the prediction, since LunchType could also be considered an "
        "indicator of economic means a family has available. Since LunchType "
        "had zero missing values it was the logical choice."
    )

    st.write(
        "### 'Cleaned' Dataset\n"
        "Below is the updated dataset with the dropped column and missing "
        "data filled in. This is referred to as **'cleaned'.**\n "
    )
    df_cleaned = load_cleaned_data()
    st.write(df_cleaned)
    