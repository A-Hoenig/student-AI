import streamlit as st
import matplotlib.pyplot as plt


def page_2_body():
    st.write("## Project Hypotheses")

    st.write(
        "I hypothesize that most of the listed features in the available "
        "student dataset will have some degree of influence on the overall "
        "performance of the student."
    )

    st.info(
        "### Gender:\n"
        "depending on the subject, gender will probably influence the students"
        " overall performance.\n"
        "### EthnicGroup:\n"
        "ethnicity (when regarded in socio-economic terms) will influence "
        "student perfromance. In this case the specfic groups are anonymized."
        "\n"
        "### ParentEduc:\n"
        "Parental education will influence student performance as I "
        "hypothesize that higher educated individuals will also prioritize the"
        " education of their children.\n"
        "### LunchType:\n"
        "similar to ehtnicity, the availability of a healthy regular meal will"
        " most likely influence performance by affecting concentration, but "
        "also indirectly as a factor of other socio-economic variables such as"
        " financial security enabling additional schooling support (materials,"
        " study partners etc)\n"
        "### TestPrep:\n"
        "Availability and participation in test prep courses most likely will "
        "influence test performance for most students\n"
        "### ParentMaritalStatus:\n"
        "parental status might influence students performance motivationally "
        "as well as more basic factors such as avaialble study time with less "
        "distractions\n"
        "### PracticeSport:\n"
        "Presumably regular sport will also help with concentration and brain"
        "development, leading to better academic performance\n"
        "### IsFirstChild:\n"
        "First children tend to have more focussed attention from their "
        "parents and might have a better start in their education path\n"
        "### NrSiblings:\n"
        "more youngers siblings might negatively impact performance due to "
        "distrctions and additional chores. Older siblings might help, however"
        " in providing additional help in school studies. I hypothesize that "
        "this will not be an obvious lindicator of student performance.\n"
        "### TransportMeans:\n"
        "transportation will presumanbly have some influence again in "
        "socio-economic terms (private transport might equate to access to "
        "other extracurricular activites that might help student performance)"
        "\n"
        "### WklyStudyHours:\n"
        "I hypothesize that the mount of study time per week devoted to exam "
        "preparation will have a significant impact on student performance."
    )
    