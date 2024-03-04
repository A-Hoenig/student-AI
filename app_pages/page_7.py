import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_plot

def page_7_body():
    st.write("## Technical Explanation")
    
    st.image(
        load_image("ml_diagram"),
        caption='Types of machine learning models',
        use_column_width= 'auto',
        )

    st.info(
        """
        The business model stated the desire to predict the exam scores of
        students based on all available other variables the school is 
        allowed to record for its students.

        The perfect case would have been a liner regression model that is
        accurate enough to predict the exact probable exam score within a
        few percent.

        Unfortunately, the available data did not allow a significant
        regression model to be trainind that was able to achieve the 
        required accuracy.

        For this reason, the problem was converted from a regression task
        to a classification task. Simply put, instead of predicting the precise
        exam results, the ML model would be changed to a classification task
        which aims to predict the a much broader target derived from 
        the numerical data of exam scores.

        This meant grouping the data into 'bins' which would then be the 
        objective to predict. Bins would represent relative positions of
        available grades such as **below average, average, above average,
        fail**, etc. 

        The hope was to be able to use the dataset features to teach the model 
        to predict which 'bin' a student would land in with reasonable 
        accuracy > 70%.

        Initially the data was grouped into 5 bins and assessed.

        The model was unable to predict the bulk of students in the middle
        of the dataset, eg the majority around the average. The same 
        applied to the attempted 3 bin solution.

        Finally the measured low accuracy forced the selection of only
        2 bins, allowing a classification of students for **below average**
        and **above average**, where the data was split at the mean value.

        This allowed at least a partial fullfillment of the business 
        request to be able to identify students in need of help and  thus
        increase the average passing grade for the school on average.
        """
    )

    st.image(
        load_image("EDA"),
        caption='Machine Learning is a complex process',
        use_column_width= 'auto',
        )

    