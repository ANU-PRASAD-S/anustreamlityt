# Your main Streamlit application code

import streamlit as st
from streamlit_option_menu import option_menu  # Import the option_menu function from the correct module

# Import the rest of the necessary libraries and code snippets

# Rest of your Streamlit code
# ...

# CREATING OPTION MENU
with st.sidebar:
    options = get_streamlit_options()  # Use the function to get Streamlit options
    selected = option_menu(
        None,
        [option["name"] for option in options],
        icons=[option["icon"] for option in options],
        default_index=0,
        orientation="vertical",
        styles={
            "nav-link": {
                "font-size": "30px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#C80101",
            },
            "icon": {"font-size": "30px"},
            "container": {"max-width": "6000px"},
            "nav-link-selected": {"background-color": "#C80101"},
        }
    )

# Rest of your Streamlit code
# ...
