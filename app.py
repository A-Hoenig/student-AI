import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_1 import page_1_body
from app_pages.page_2 import page_2_body
from app_pages.page_3 import page_3_body

app = MultiPage(app_name="Student AI")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Page 1", page_1_body)
app.add_page("Page 2", page_2_body)
app.add_page("Page 3", page_3_body)


app.run()  # Run the app
