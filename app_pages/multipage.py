import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")  # You may add an icon, to personalize your App
        # check links below for additional icons reference
        # https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
        # https://twemoji.maxcdn.com/2/test/preview.html

    def add_page(self, title, func, group=None) -> None:
        self.pages.append({"title": title, "function": func, "group": group})

    def run(self):
        st.title(self.app_name)
        # Initial = no group
        current_group = None

        for page in self.pages:
            # Check for new group
            if page['group'] != current_group:
                # not the first group, add a separator
                if current_group is not None:
                    st.sidebar.markdown("---")
                # Update current group to new group
                current_group = page['group']
                # Add group name as a header if you want
                if current_group:
                    st.sidebar.header(current_group)

            # list the pages normally
            if st.sidebar.button(page['title']):
                page['function']()
                break
