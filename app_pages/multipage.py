import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = {}
        self.app_name = app_name
        self.first_page_set = False

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🎓")
        
        # Remember the session state
        if 'selected_page' not in st.session_state:
            st.session_state.selected_page = None

    def add_page(self, title, func, group_name=None) -> None:
        if group_name not in self.pages:
            self.pages[group_name] = []
        self.pages[group_name].append({"title": title, "function": func})
        # Load first page by default
        if not self.first_page_set:
            st.session_state.selected_page = func
            #remember page has been loaded
            self.first_page_set = True

    def run(self):
        st.title(self.app_name)
        
        for group_name, pages in self.pages.items():
            if group_name:
                st.sidebar.header(group_name)
            for page in pages:
                button_key = f"button_{group_name}_{page['title']}"
                if st.sidebar.button(page['title'], key=button_key):
                    st.session_state.selected_page = page['function']
        
        # Run the selected page
        if st.session_state.selected_page:
            st.session_state.selected_page()