import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_1 import page_1_body
from app_pages.page_2 import page_2_body
from app_pages.page_3 import page_3_body
from app_pages.page_4 import page_4_body
from app_pages.page_5 import page_5_body
from app_pages.page_6 import page_6_body

app = MultiPage(app_name="Student AI")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Introduction", page_1_body)
app.add_page("Hypothesis", page_2_body)
app.add_page("EDA", page_3_body)
app.add_page("Report", page_4_body)
app.add_page("Predict", page_5_body)
app.add_page("AI performance", page_6_body)


app.run()  # Run the app
