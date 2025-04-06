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
import streamlit as st
import pandas as pd

st.title("Tar Load Estimation in Human Lungs")
st.markdown("🔍 Upload a CSV file to estimate tar accumulation.")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    st.subheader("📊 Uploaded Data")
    st.write(df)

    # Dummy prediction logic
    st.subheader("🧠 Model Output")
    df['Predicted Tar Load'] = df['YearsSmoking'] * df['CigarettesPerDay'] * 0.1  # simple placeholder
    st.write(df[['Age', 'YearsSmoking', 'CigarettesPerDay', 'Gender', 'PassiveSmoking', 'Predicted Tar Load']])


