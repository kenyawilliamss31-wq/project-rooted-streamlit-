import streamlit as st

st.set_page_config(
    page_title="Project ROOTED",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Migration", "Education", "Occupation"])

if page == "Home":
    st.title("Project ROOTED: Final Showcase")
    st.subheader("African American Migration, Education, and Occupation")
    st.write("Welcome to my final showcase.")
    st.write("Use the sidebar to explore migration, education, and occupation.")

elif page == "Migration":
    st.title("Migration")
    st.write("This page will show birthplace vs current state.")
    st.write("Content coming soon.")

elif page == "Education":
    st.title("Education")
    st.write("This page will show school attendance and literacy.")
    st.write("Content coming soon.")

elif page == "Occupation":
    st.title("Occupation")
    st.write("This page will show occupation distributions using OccupationTitle.")
    st.write("Content coming soon.")
