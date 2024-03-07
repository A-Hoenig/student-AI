import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_1 import page_1_body
from app_pages.page_2 import page_2_body
from app_pages.page_3 import page_3_body
from app_pages.page_4 import page_4_body
from app_pages.page_5 import page_5_body
from app_pages.page_6 import page_6_body
from app_pages.page_7 import page_7_body
from app_pages.page_8 import page_8_body

# Create an instance of the app
app = MultiPage(app_name="Student AI")

# Add your app pages here using .add_page()
app.add_page("INTRO: Introduction", page_1_body)
app.add_page("INTRO: Project Hypotheses", page_2_body)
app.add_page("ANALYSIS: Data Intro / Cleaning", page_3_body)
app.add_page("ANALYSIS: Data Analysis", page_4_body)
app.add_page("ANALYSIS: Machine Learning Details", page_7_body)
app.add_page("PREDICT: Generate Report", page_5_body)
app.add_page("PREDICT: Predict Student Results", page_6_body)
app.add_page("FINAL: Conclusion", page_8_body)

app.run()  # Run the app
