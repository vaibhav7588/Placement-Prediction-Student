import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Placement Prediction")

# 🔹 FLOAT INPUTS
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)

ssc = st.number_input("10th Percentage (SSC)", min_value=0.0, max_value=100.0, step=0.1)

hsc = st.number_input("12th Percentage (HSC)", min_value=0.0, max_value=100.0, step=0.1)

aptitude = st.number_input("Aptitude Score", min_value=0.0, max_value=100.0, step=0.1)

# 🔹 OTHER INPUTS
internships = st.number_input("Internships", min_value=0, step=1)

projects = st.number_input("Projects", min_value=0, step=1)

communication = st.slider("Communication Skills (1-10)", 1, 10)

training = st.selectbox("Placement Training", ["No", "Yes"])

# Convert training
training_val = 1 if training == "Yes" else 0

# 🔹 Prediction Button
if st.button("Predict"):

    # 🚨 FAIL CONDITION (IMPORTANT)
    if ssc < 35 or hsc < 35:
        st.error("❌ Student will NOT be Placed (Failed in SSC/HSC)")
    
    else:
        # Normal prediction
        input_data = np.array([[
            float(cgpa),
            float(ssc),
            float(hsc),
            float(internships),
            float(projects),
            float(aptitude),
            float(communication),
            float(training_val)
        ]])

        result = model.predict(input_data)

        if result[0] == 1:
            st.success("✅ Student will be Placed")
        else:
            st.error("❌ Student will NOT be Placed")
