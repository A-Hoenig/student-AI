import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_image, load_plot, load_text

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

        The perfect case would have been a liner **regression model** that is
        accurate enough to predict the exact probable exam score within a
        few percent.

        Unfortunately, the available data did not allow a significant
        regression model to be trained that was able to achieve the 
        required accuracy.

        For this reason, the problem was converted from a **regression** task
        to a **classification** task. Simply put, instead of predicting the 
        precise exam results, the ML model would be changed to a classification
        task which aims to predict a much broader target derived from the
        numerical data of exam scores.

        This meant grouping the data into 'bins' which would then be the 
        objective to predict. Bins would represent relative positions of
        available grades such as *below average, average, above average,
        fail*, etc. 

        The hope was to be able to use the dataset features to teach the model 
        to predict which 'bin' a student would land in with reasonable 
        accuracy > 70%.

        Initially the data was grouped into 5 bins and assessed.

        The model was unable to predict the bulk of students in the middle
        of the dataset, eg the majority around the average. The same 
        applied to the attempted 3 bin solution.

        Finally the measured low accuracy forced the selection of only
        2 bins, allowing a classification of students for *below average*
        and *above average*, where the data was split at the mean value.

        This allowed a partial fullfillment of the business request to be able 
        to identify students in need of help and  thus increase the average
        passing grade for the school on average.
        """
    )

    st.write("# Building the Machine Learning Model")
    st.image(
        load_image("EDA"),
        caption='Machine Learning is a complex process',
        use_column_width= 'auto',
        )

    st.info(
        """
        The major step in preparing data for machine learning are shown above.
        All steps were considered and the results are documented here, as well
        as in detail in the accompining code notebooks viewable in the 
        GitHub repository. All steps can be recreated and reproduced.
        
        * Hypothesis
        * Missing Data
        * Duplication
        * Distribution and type
        * Anomalies and Outliers

        were all covered in the data cleaning portion.

        * Correlation
        * Target Imbalance
        * Figure out Patterns

        Were covered in the Data Analysis portion.

        Ulitmately the most significant features for each type of exam
        were determined and each individual model was trained on them.

        To test the models, 20% of the data was separated, and as such can
        be considered **unseen**, as the model was not given the data when 
        learning the relationships.

        A measure of how well the model works is to then give it the
        unseen data and see how well it predics without providing the
        answers. Those results are plotted in the confusion matrixes below.
        """
    )

    st.image(
        load_plot("feature_correlation_matrix"),
        caption=f'Mapping correlation of Variables',
        use_column_width= 'auto',
        )

    col_left, col_mid, col_rt = st.beta_columns(3)
    with col_left:
        st.image(
            load_plot("feature_correlation_MathScore"),
            caption='Features correlating with Math'
            )
    with col_mid:
        st.image(
            load_plot("feature_correlation_ReadingScore"),
            caption='Features correlating with Reading'
            )
    with col_rt:
        st.image(
            load_plot("feature_correlation_WritingScore"),
            caption='Features correlating with Writing'
            )   

    st.info(
        """
        The above seemingly complex chart shows how much a feature of the 
        student data relates to another. A value of 0 (grey) indicates **NO**
        correlation and a value of **1** or **-1** (Blue or Red) indicates 
        perfect correlation.

        This can been seen for binary variable such as *Male/Female*. 
        They correlate at 1/-1 since they are the inverse of each other.
        For this dataset it can be said that if the value is Male we are 100%
        sure it is not female and vice versa.

        For other variables it is not that easy.

        The exam results show the highest (not 1 or -1) correlation. This 
        makes sense, as students who do well in one subject typically also
        perform well in other school criteria. Since the mean is calculated
        from the other 3 exam results, obviously it also correlates highly.

        For ML learning it is of no use to predict, say the Math score, by 
        correlating it to the Reading score (as these are not available) and
        the objective is to **predict** all 3 values.

        For this reason, all but one score are removed from the data and we
        attempt to find correlations of the other features that are related to
        high specific exam scores.

        This can be seen individually in the plots underneath the matrix.

        If we disregard the other Numerical scores, we find that 5 features
        have values around 0.2. When seen in relation to all other features,
        a value of >0.2 can be considered to have some significance in 
        predicting the score. 

        Looking at the plots we can see that all 3 vary slightly, but the top
        features that are calculated are:

        * LunchType
        * EthnicGroup
        * Gender
        * ParentEducation
        * TestPreparation

        The order changes depending on the exam type. For instance,
        looking closely, we can see that for predicting writing, Gender is
        more important than LunchType. For Maths, Gender plays a smaller role.

        These relationships were used to assess the features in the dataset and
        then train the models based on these derived facts.
        """
    )

    st.write("# Final Model Confusion Matrix Results")
    exams = ['math', 'reading', 'writing']
    selected_exam = st.radio("Select Exam Subject:", exams)

    col1, col2 = st.beta_columns(2)
    with col1:
        model_version = "v2"
        st.image(
                f"outputs/models/{selected_exam}/{model_version}/"
                f"{selected_exam}-feature-importance.png",
                caption=f'Most significant features for predicting {selected_exam}',
                width=250
                )
    with col2:
        train_report = load_text(f'confusion-matrix-{selected_exam}-train.txt')
        if train_report:
            text_size = "10px" 
            # Force HTML/CSS to set font
            st.markdown(f"<p style='font-size: {text_size};'>{train_report}</p>", unsafe_allow_html=True)

        test_report = load_text(f'confusion-matrix-{selected_exam}-test.txt')
        if test_report:
            st.markdown(f"<p style='font-size: {text_size};'>{test_report}</p>", unsafe_allow_html=True)

    st.write('You can select each exam type using the buttons above.\n'
            'There are a lot of numbers which will be explained below.')
    st.info(
        """
        
        ### **TRAIN** vs **TEST** Data
        The TRAIN tables show the results of training the model using
        80% of the data available in the dataset.\n
        The TEST tables show the results of the model predicting scores
        based on **unseen** data since the remaining 20% of the data were
        deliberately held back for this purpose.

        Comparing the 2 allows us to assess how well the model training
        process worked. If the train and test results are low, then the model 
        might be *underfitted* and is not able to make any predictions on data
        in general. Not very useful.\n
        An *overfitted* model will have very good training results, but poor
        test results, indicating also that the model can perfectly predict 
        the trained data but is not able to generalize enough to assess unseen
        data.

        If the test values are the same or slightly better than train values
        and are reasonably high, then a good balance was achieved.

        ### Confusion Matrix
        There a 4 types of predictions used in this 'Confusion Matrix:\n
        |Type|Explanation |
        |:---:|:---:|:---:|
        | True Positive |  Model correctly predicts a student needs help|
        | False Positive |  Model incorrectly predicts a student needs help|
        | True Negative |  Model correctly predicts a student needs no help|
        | False Negative |  Model incorrectly predicts a student needs no help|
        
        * A false positive result would mean that some students are flagged as
        needing help when they might not. For the business case, this is
        acceptable as it still achieves the overall obective of improving
        average exam scores, but might use up a few more ressources.

        * A false negative is problematic, as this represents students who **DO**
        need help that are predicted to not need help. This would go against
        the business objective, so the model performance and accuracy should
        avoid too many false negatives in this case. 

        ### Classification Report
        * The Precision value indicates the percentage of times the model 
        identifies a student that needs help.
        * Recall indicates that the model is able to identify this percentage
        of all students who might need help.
        * F1 is a calculated balance between these 2 values and shows the 
        general performance of the model.
        
        These values are calculated for each class, in this case the student
        might need help, or will not need help.

        * The macro average balances the values for all classes and is the most
        general way of assessing the overall model performance.

        * The weighted average also factors in the distribution of the data so
        that the class with many more values would be considered. In this case
        both classes are similar in size (above / below average) so we expect
        the weighted average to be very close to the macro avg.

        **The specific results of the models will be assessed in the 
        Conclusion.**
        """
    )