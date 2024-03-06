import streamlit as st


def maths(
    input_features,
    math_features,
    math_pipeline,
    math_label_map):

    # Subset feature variables
    math_input_features = input_features.filter(math_features)

    # Make prediction
    math_prediction = math_pipeline.predict(math_input_features)
    math_prediction_probability = math_pipeline.predict_proba(
        math_input_features)

    # Display results
    probability = math_prediction_probability[0, math_prediction][0]*100
    math_label = math_label_map[math_prediction[0]]

    if math_prediction != 1:
        statement = (
            "## Math Exam:\n"
            "Prediction for student: "
            f" **{math_label}** (Probability: {probability.round(2)}%)"
        )
    else:
        statement = (
            "## Math Exam:\n"
            "Prediction for student: "
            f" **{math_label}**"
        )
    st.write(statement)


def reading(
    input_features,
    reading_features,
    reading_pipeline,
    reading_label_map):

    # subset feature variables
    reading_input_features = input_features.filter(reading_features)

    # Make prediction
    reading_prediction = reading_pipeline.predict(reading_input_features)
    reading_prediction_probability = (
        reading_pipeline.predict_proba(reading_input_features))

    # display results
    probability = reading_prediction_probability[0, reading_prediction][0]*100
    reading_label = reading_label_map[reading_prediction[0]]

    if reading_prediction != 1:
        statement = (
            "## Reading Exam:\n"
            "Prediction for student: "
            f" **{reading_label}** (Probability: {probability.round(2)}%)"
        )
    else:
        statement = (
            "## Reading Exam:\n"
            "Prediction for student: "
            f" **{reading_label}**"
        )
    st.write(statement)


def writing(input_features,
                    writing_features,
                    writing_pipeline,
                    writing_label_map):

    # subset feature variables
    writing_input_features = input_features.filter(writing_features)

    # Make prediction
    writing_prediction = writing_pipeline.predict(writing_input_features)
    writing_prediction_probability = (
        writing_pipeline.predict_proba(writing_input_features))

    # display results
    probability = writing_prediction_probability[0, writing_prediction][0]*100
    writing_label = writing_label_map[writing_prediction[0]]

    if writing_prediction != 1:
        statement = (
            "## Writing Exam:\n"
            "Prediction for student: "
            f" **{writing_label}** (Probability: {probability.round(2)}%)"
        )
    else:
        statement = (
            "## Writing Exam:\n"
            "Prediction for student: "
            f" **{writing_label}**"
        )
    st.write(statement)
