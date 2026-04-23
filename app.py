import streamlit as st
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Placement Prediction System")

# Inputs
cgpa = st.number_input("CGPA", 0.0, 10.0)
ssc = st.number_input("10th Percentage (SSC)", 0, 100)
hsc = st.number_input("12th Percentage (HSC)", 0, 100)
internships = st.number_input("Internships", 0, 5)
projects = st.number_input("Projects", 0, 10)
aptitude = st.number_input("Aptitude Score", 0, 100)
softskills = st.slider("Communication Skills (1-10)", 1, 10)
training = st.selectbox("Placement Training", ["No", "Yes"])

training_val = 1 if training == "Yes" else 0

# Prediction
if st.button("Predict"):
    input_data = np.array([[cgpa, ssc, hsc, internships, projects, aptitude, softskills, training_val]])
    result = model.predict(input_data)

    if result[0] == 1:
        st.success("✅ Student will be Placed")
    else:
        st.error("❌ Student will NOT be Placed")