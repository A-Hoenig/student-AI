import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_plot, load_text

def page_8_body():
    st.write("## Conclusions")

    st.write(
        """
        ### We remind ourselves of the business requirements:\n\n
        1. Analyse the given dataset and identify relationships to the final 
        student performance that might not be obvious at first glance.
        2. Provide an interface to an ML algorithm that, given a student's
        data, can predict their final score and flag students who will need 
        support.
        3. A dashboard should be created as the interface to the model.
        The school wishes to predict individual students or process an
        entire class by uploading a csv file.
        4. Due to personal data being involved, the interface should be
        deployed on their own server and offer a simple dashboard for school
        counsellors.

        ### Requirements Assessment:

        1. **Achieved.**\n
        The dataset provided shows some correlations that influence the 
        overall score. However the impact of these variables was quite weak
        to allow very accurate modelling.
        Some of the expanded dataset variables had almost no impact whatsoever:

        * PARENT MARITAL STATUS
        * PRACTICE SPORT
        * IS FIRST CHILD
        * NUMBER OF SIBLINGS
        * TRANSPORTATION MEANS
        * WEEKLY STUDY HOURS

        2. **Partially Achieved.**\n
        The goal of predicting the final score of a student could not be
        achieved. The given dataset did not have the required correlations
        for an accurate regression model prediction.\n
        In coordination with the product owner, the task was changed to a
        classification task to achieve the goal of still identifying weak
        students.\n
        This was attempted for 5, 3 and then 2 groupings (bins). Again, the 
        data did not allow training a model to predict 5 or 3 separate
        categories, and only dividing the data into 2 groups at the mean 
        allowed a reasonable prediction of which students would likely be in
        the below average groups indicating they might need assistance.\n

        3. **Achieved.**\n
        This dashboard is able to explain the dataset analysis and offers a
        working interface to select specific student variables and predict the
        outcome for Math, Reading and Writing scores.\n
        The same calculations can be done in bulk by uploading a csv file with
        a list of students and their data. The resulting report assesses each 
        student in the list and provides the prediction. The report can be
        filtered by the result and sorted to help counsellors identify those
        students most likely to be in need of help.

        4. **Achieved.**
         """ )
    st.info(
        """
        *In general, it can be assumed that the difficulty in achieving a high
        level of prediction with this dataset is in the fact that it is 
        fictional / synthetic. Whoever created it might not have been able to
        incorporate the nuanced relationships that might drive real world 
        exam results based on these types of student data.*

        *The code in this project was deliberately set up allow a quick 
        reconfiguration to a new dataset with a high degree of automation.*

        *It would be very interesting to test the model training on a real world
        dataset.*    
    """)
    
    st.write('---')
    st.write('Below are the specific test results of each model that was '
        'generated.')
    
    test_report = load_text(f'confusion-matrix-math-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>", unsafe_allow_html=True)

    test_report = load_text(f'confusion-matrix-reading-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>", unsafe_allow_html=True)

    test_report = load_text(f'confusion-matrix-writing-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>", unsafe_allow_html=True)