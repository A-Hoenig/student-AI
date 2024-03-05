import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = {}
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🎓")
        
        if 'selected_page_key' not in st.session_state:
            st.session_state.selected_page_key = None
            st.session_state.selected_page = None

    def add_page(self, title, func, group_name=None) -> None:
        key = f"{group_name}_{title}" 
        if group_name not in self.pages:
            self.pages[group_name] = []
        self.pages[group_name].append({"title": title, "function": func, "key": key})
        
        # Automatically set the first added page as the default
        if not st.session_state.selected_page:
            st.session_state.selected_page = func
            st.session_state.selected_page_key = key

    def run(self):
        st.title(self.app_name)
        
        for group_name, pages in self.pages.items():
            if group_name:
                st.sidebar.header(group_name)
            for page in pages:
                button_key = f"nav_button_{page['key']}"
                if st.sidebar.button(page['title'], key=button_key):
                    # Update the session state to the clicked page's function and key
                    st.session_state.selected_page = page['function']
                    st.session_state.selected_page_key = page['key']
        
        # Execute the selected page function
        if st.session_state.selected_page:
            st.session_state.selected_page()