import streamlit as st
import pandas as pd
import joblib  # using joblib to load model

# Load the trained model pipeline
model = joblib.load('student_performance_model_joblib.pkl')

# Streamlit UI setup
st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("🎓 Student Performance Index Predictor")

st.markdown("Enter the student details below to predict their Performance Index:")

# Input fields
hours_studied = st.number_input("Hours Studied", min_value=0.0, max_value=24.0, value=5.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0, max_value=100.0, value=70.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
sample_papers = st.number_input("Sample Question Papers Practiced", min_value=0, max_value=50, value=5)
extracurricular = st.selectbox("Extracurricular Activities", options=["Yes", "No"])
internet_access = st.selectbox("Internet Access", options=["Yes", "No"])
weekly_study_hours = st.number_input("Weekly Study Hours", min_value=0.0, max_value=100.0, value=10.0)
parental_support = st.selectbox("Parental Support", options=["Yes", "No"])
health_status = st.selectbox("Health Status", options=["Good", "Average", "Poor"])

# Create DataFrame for prediction
input_df = pd.DataFrame({
    'Hours Studied': [hours_studied],
    'Previous Scores': [previous_scores],
    'Sleep Hours': [sleep_hours],
    'Sample Question Papers Practiced': [sample_papers],
    'Extracurricular Activities': [extracurricular],
    'Internet Access': [internet_access],
    'Weekly Study Hours': [weekly_study_hours],
    'Parental Support': [parental_support],
    'Health Status': [health_status]
})

# Predict when button is clicked
if st.button("Predict Performance Index"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted Performance Index: **{prediction:.2f}**")
