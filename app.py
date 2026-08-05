import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Project ROOTED",
    page_icon="📊",
    layout="wide"
)

# Try to load the CSV from the repo
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("ROOTED_10000_with_titles.csv")
        return df
    except FileNotFoundError:
        return None

df = load_data()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Migration", "Education", "Occupation"])

if page == "Home":
    st.title("Project ROOTED: Final Showcase")
    st.subheader("African American Migration, Education, and Occupation")
    st.write("Welcome to my final showcase.")
    st.write("Use the sidebar to explore migration, education, and occupation.")

    if df is not None:
        st.markdown("### Dataset preview")
        st.write(df.head())
    else:
        st.warning("CSV file not found. Make sure ROOTED_10000_with_titles.csv is in the repo.")

elif page == "Migration":
    st.title("Migration")

    if df is None:
        st.warning("CSV file not found. Migration content will load once the file is available.")
    else:
        st.write("This page will show birthplace vs current state.")
        st.markdown("#### Top state-of-residence vs birthplace combos")
        combo = df.groupby(["StateName", "BirthplaceName"]).size().sort_values(ascending=False).head(10)
        st.write(combo)

elif page == "Education":
    st.title("Education")

    if df is None:
        st.warning("CSV file not found. Education content will load once the file is available.")
    else:
        st.write("This page will show school attendance and literacy.")
        st.markdown("#### School attendance counts")
        st.write(df["SCHOOL"].value_counts())

        st.markdown("#### Literacy counts")
        st.write(df["LIT"].value_counts())

elif page == "Occupation":
    st.title("Occupation")

    if df is None:
        st.warning("CSV file not found. Occupation content will load once the file is available.")
    else:
        st.write("This page shows occupation distributions using OccupationTitle.")

        st.markdown("#### Top occupations")
        occ_counts = df["OccupationTitle"].value_counts().head(15)
        st.write(occ_counts)

        st.markdown("#### Bar chart of top occupations")
        st.bar_chart(occ_counts)
