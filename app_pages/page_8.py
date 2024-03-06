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
    st.write('---')
    st.info(
        """
        *In general, it can be assumed that the difficulty in achieving a high
        level of prediction with this dataset is in the fact that it is 
        fictional / synthetic. Whoever created it might not have been able to
        incorporate the nuanced relationships that might drive real world 
        exam results based on these types of student data.*

        *The code in this project was deliberately set up allow a quick 
        reconfiguration to a new dataset with a high degree of automation.*

        *It would be very interesting to test the model training on a real
        world dataset.*    
        """)

    st.write('---')
    st.write('## Assessing the Hypotheses')
    st.write('### Below is the evaluation of the stated hypotheses.')

    st.write(
        """
        ### Gender:\n
        depending on the subject, gender will probably influence the students
        overall performance.\n
        """)
    st.info(
        """
        **TRUE**. with a Mean Range of 3.65, Gender was shown to have a small
        influence on the overall score.
        """
    )
    st.write("### EthnicGroup:\n"
        "ethnicity (when regarded in socio-economic terms) will influence "
        "student performance. In this case the specfic groups are anonymized."
        "\n")
    st.info(
        """
        **TRUE**. with a mean range of 9.07 ethinc group shows an influence
        over the exam performance. However it did not have much significance
        in ML model predictions.
        """
    )
    st.write("### ParentEduc:\n"
        "Parental education will influence student performance as I "
        "hypothesize that higher educated individuals will also prioritize the"
        " education of their children.\n")
    st.info(
        """
        **TRUE**. This was shown to be that case with a mean range of 10.03.
        Also for training the models it had some valid predictive power.
        """
    )
    st.write("### LunchType:\n"
        "similar to ehtnicity, the availability of a healthy regular meal will"
        " most likely influence performance by affecting concentration, but "
        "also indirectly as a factor of other socio-economic variables such as"
        " financial security enabling additional schooling support (materials,"
        " study partners etc)\n")
    st.info(
        """
        **TRUE**. A mean range of 9.57 indicates a significant score difference
        for students who eat free lunches to those who don't need one. LunchType
        also had an influence on model training and prediction power.
        """
    )
    st.write("### TestPrep:\n"
        "Availability and participation in test prep courses most likely will "
        "influence test performance for most students\n")
    st.info(
        """
        **TRUE**. Test prep has a small influence with a mean range of 6.73.
        The model training also identified TestPrep as having an influence
        in predicting Reading and Writing Scores.
        """
    )
    st.write("### ParentMaritalStatus:\n"
        "parental status might influence students performance motivationally "
        "as well as more basic factors such as avaialble study time with less "
        "distractions\n")
    st.error(
        """
        **FALSE**. Mean range 0.7 shows this had no influence on the exam
        results.
        """
    )
    st.write("### PracticeSport:\n"
        "Presumably regular sport will also help with concentration and brain"
        "development, leading to better academic performance\n")
    st.error(
        """
        **FALSE**. Mean range 2.78 shows this had very small influence on 
        exam reaults and was not identified by ML algorithms as being 
        significant.
        """
    )
    st.write("### IsFirstChild:\n"
        "First children tend to have more focussed attention from their "
        "parents and might have a better start in their education path\n")
    st.error(
        """
        **FALSE**. Mean range 0.39 shows this had no influence on the exam
        results.
        """
    )
    st.write("### NrSiblings:\n"
        "more youngers siblings might negatively impact performance due to "
        "distrctions and additional chores. Older siblings might help, however"
        " in providing additional help in school studies. I hypothesize that "
        "this will not be an obvious lindicator of student performance.\n")
    st.error(
        """
        **FALSE**. Mean range 1.26 shows this had no influence on the exam
        results.
        """
    )
    st.write("### TransportMeans:\n"
        "transportation will presumanbly have some influence again in "
        "socio-economic terms (private transport might equate to access to "
        "other extracurricular activites that might help student performance)"
        "\n")
    st.error(
        """
        **FALSE**. Mean range 0.07 shows this had zero influence on the exam
        results.
        """
    )
    st.write("### WklyStudyHours:\n"
        "I hypothesize that the mount of study time per week devoted to exam "
        "preparation will have a significant impact on student performance."
    )
    st.warning(
        """
        **PARTIALLY FALSE**. While a mean range of 3.0 shows a small impact on
        exm results, again, it was not shown to have any predictive power for
        the ML algorithms. This was somewhat surprising, as the amount of
        study would normally be assumed to have a significant impact on
        student performance.
        """
    )
    
    st.write('---')
    st.write('## Machine Learning Conclusions')
    st.write('### Below are the specific test results of each model that was '
        'generated.')
    
    test_report = load_text(f'confusion-matrix-math-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>",
        unsafe_allow_html=True)
    st.info(
        """
        The Math Model was the only one that was only trained on 2 features:
        EthnicGroup and ParentalEducation.
        The precision is on the lower side with an F1 of 0.68/0.42. Combined
        with the recall of 0.83 for students needing assistance, the model has
        more false positives which is in line with business objective no2.
        The recall indicates that 82% of students requiring help will be
        identified.
        """
    )

    test_report = load_text(f'confusion-matrix-reading-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>",
        unsafe_allow_html=True)
    st.info(
        """
        The Reading Model was trained on 3 features:
        LunchType, Gender and TestPreparation.
        The precision is on the lower side with an F1 of 0.66/0.59. Combined
        with the recall of 0.69 for students needing assistance, the model has
        more false positives which is in line with business objective no2.
        The recall indicates that 69% of students requiring help will be
        identified.
        """
    )
    test_report = load_text(f'confusion-matrix-writing-test.txt')
    if test_report:
        st.markdown(f"<p style='font-size: 8;'>{test_report}</p>",
        unsafe_allow_html=True)
    st.info(
        """
        The Writing Model was trained on 3 features:
        LunchType, Gender and TestPreparation.
        The precision is on the lower side with an F1 of 0.68/0.65. Combined
        with the recall of 0.67 for students needing assistance, the model has
        more false positives which is in line with business objective no2.
        The recall indicates that 67% of students requiring help will be
        identified.
        """
    )