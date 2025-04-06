import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Tar Load Estimation", layout="centered")

# Title and Description
st.title("Tar Load Estimation in Human Lungs")
st.markdown("👋 **Welcome!** This Streamlit app helps estimate tar accumulation in human lungs using Machine Learning.")
st.markdown("---")

# File Upload Section
st.header("🚀 Upload Your Input File")
st.caption("Choose a CSV file containing the following columns: `age`, `years_smoking`, `cigarettes_per_day`, `gender`, `passive_smoking`")
uploaded_file = st.file_uploader("Drag and drop file here", type="csv")

# Main App Logic
if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        # Show available columns
        st.write("📄 **Columns in uploaded file:**", df.columns.tolist())

        # Display uploaded data
        st.subheader("📊 Uploaded Data")
        st.dataframe(df)

        # Check required columns exist
        required_columns = ['age', 'years_smoking', 'cigarettes_per_day', 'gender', 'passive_smoking']
        missing_cols = [col for col in required_columns if col not in df.columns]
        
        if missing_cols:
            st.error(f"❌ Missing columns in uploaded file: {missing_cols}")
        else:
            # Dummy Tar Load Estimation logic (replace with ML model later)
            df['Predicted Tar Load'] = df['years_smoking'] * df['cigarettes_per_day'] * 0.1

            # Display Results
            st.subheader("🧠 Predicted Tar Load")
            st.dataframe(df[['age', 'years_smoking', 'cigarettes_per_day', 'gender', 'passive_smoking', 'Predicted Tar Load']])

    except Exception as e:
        st.error(f"⚠️ An error occurred while processing the file:\n\n{e}")

# Footer
st.markdown("---")
st.markdown("Developed by **Lakshya Rawat**")

   
