import streamlit as st
import matplotlib.pyplot as plt


def page_2_body():
    st.write("## Project Hypotheses")

    st.write("""I hypothesize that most of the listed features in the available
student dataset will have some degree of influence on the overall
performance of the student.""")
    
    st.info("""### Gender:
depending on the subject, gender will probably influence the students
overall performance.""")
    
    st.info("""### EthnicGroup:
ethnicity (when regarded in socio-economic terms) will influence
student performance. In this case, the specific groups are anonymized.""")
    
    st.info("""### ParentEduc:
Parental education will influence student performance as I hypothesize
that higher educated individuals will also prioritize the education
of their children.""")
    
    st.info("""### LunchType:
similar to ethnicity, the availability of a healthy regular meal will
most likely influence performance by affecting concentration, but
also indirectly as a factor of other socio-economic variables such as
financial security enabling additional schooling support (materials,
study partners etc)""")
    
    st.info("""### TestPrep:
Availability and participation in test prep courses most likely will
influence test performance for most students""")
    
    st.info("""### ParentMaritalStatus:
parental status might influence students' performance motivationally
as well as more basic factors such as available study time with less
distractions""")
    
    st.info("""### PracticeSport:
Presumably, regular sport will also help with concentration and brain
development, leading to better academic performance""")
    
    st.info("""### IsFirstChild:
First children tend to have more focused attention from their
parents and might have a better start in their education path""")
    
    st.info("""### NrSiblings:
more younger siblings might negatively impact performance due to
distractions and additional chores. Older siblings might help, however,
in providing additional help in school studies. I hypothesize that
this will not be an obvious indicator of student performance.""")
    
    st.info("""### TransportMeans:
transportation will presumably have some influence again in
socio-economic terms (private transport might equate to access to
other extracurricular activities that might help student performance)""")
    
    st.info("""### WklyStudyHours:
I hypothesize that the amount of study time per week devoted to exam
preparation will have a significant impact on student performance.""")

    