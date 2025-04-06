import streamlit as st
import pandas as pd

st.title("🫁 Tar Load Estimation in Human Lungs")

st.markdown("""
👋 Welcome! This Streamlit app helps estimate tar accumulation in human lungs using Machine Learning.
""")

uploaded_file = st.file_uploader("🚀 Upload Your Input File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required_columns = ['age', 'years_smoking', 'cigarettes_per_day', 'gender', 'passive_smoking']
    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        st.error(f"❌ Missing columns in uploaded file: {missing_cols}")
    else:
        # Predict tar load (placeholder logic)
        df['Predicted Tar Load (mg)'] = df['years_smoking'] * df['cigarettes_per_day'] * 0.1

        # Determine risk level
        def risk_level(tar):
            if tar <= 10:
                return "Low Risk"
            elif tar <= 30:
                return "Medium Risk"
            else:
                return "High Risk"

        df['Risk Level'] = df['Predicted Tar Load (mg)'].apply(risk_level)

        st.markdown("### 🧠 Predicted Tar Load")
        st.dataframe(df)
