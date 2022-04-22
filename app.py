import streamlit as st
from multiapp import MultiApp
from scripts import home, exit  # import your app modules here

app = MultiApp()

# st.markdown("""
# # Multi-Page App
# This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
# """)

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Exit", exit.app)
# The main app
app.run()
