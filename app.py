import streamlit as st

st.set_page_config(page_title="Tar Load Estimation", layout="centered")

st.title("Tar Load Estimation in Human Lungs")
st.markdown("---")
st.write("👋 Welcome! This Streamlit app helps estimate tar accumulation in human lungs using Machine Learning.")

st.subheader("🚀 Upload Your Input File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    # You can add code to load & show the data
    # For example: st.dataframe(pd.read_csv(uploaded_file))

st.markdown("---")
st.caption("Developed by Lakshya Rawat")

