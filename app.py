import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tar Load Estimation", page_icon="🫁", layout="centered")

st.title("🫁 Tar Load Estimation in Human Lungs")

st.markdown("Welcome! This Streamlit app helps estimate tar accumulation in human lungs using Machine Learning.")
st.markdown("## 🚀 Upload Your Input File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Check required columns
    expected_columns = ['age', 'years_smoking', 'cigarettes_per_day', 'gender', 'passive_smoking']
    missing_cols = [col for col in expected_columns if col not in df.columns]

    if missing_cols:
        st.error(f"Missing columns in uploaded file: {missing_cols}")
    else:
        # Prediction logic
        df['Predicted Tar Load (mg)'] = df['years_smoking'] * df['cigarettes_per_day'] * 0.1

        # Risk message
        def risk_level(tar):
            if tar < 10:
                return "🟢 Low Risk"
            elif tar < 30:
                return "🟠 Medium Risk"
            else:
                return "🔴 High Risk"
        
        df['Risk Level'] = df['Predicted Tar Load (mg)'].apply(risk_level)

        st.markdown("## 🧠 Predicted Tar Load")
        st.dataframe(df)

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name='tar_predictions.csv',
            mime='text/csv',
        )

st.markdown("---")
st.markdown("Developed by **Lakshya Rawat**")

            
