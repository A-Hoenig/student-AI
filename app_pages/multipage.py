import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🎓")

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        # Create a list of page titles
        page_titles = [page['title'] for page in self.pages]

        selected_page_title = st.sidebar.radio("Navigation", page_titles)

        # load page
        for page in self.pages:
            if page['title'] == selected_page_title:
                page['function']()
                break