import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Placement Prediction System")

st.subheader("Enter Student Details")

# 🔹 Inputs
cgpa = st.number_input("CGPA", 0.0, 10.0, step=0.1)
ssc = st.number_input("SSC Percentage", 0.0, 100.0, step=0.1)
hsc = st.number_input("HSC Percentage", 0.0, 100.0, step=0.1)
aptitude = st.number_input("Aptitude Score", 0.0, 100.0, step=0.1)

internships = st.number_input("Internships", 0, 10)
projects = st.number_input("Projects", 0, 10)
communication = st.slider("Communication Skills (1-10)", 1, 10)

training = st.selectbox("Placement Training", ["No", "Yes"])
training_val = 1 if training == "Yes" else 0

# 🔹 Prediction
if st.button("Predict"):

    # 🚨 Eligibility Criteria
    if ssc < 40 and hsc < 40:
        st.error("❌ Failed in SSC & HSC → Not Eligible")
    
    elif ssc < 40:
        st.error("❌ Failed in SSC → Not Eligible")

    elif hsc < 40:
        st.error("❌ Failed in HSC → Not Eligible")

    elif cgpa < 6:
        st.warning("⚠️ Low CGPA → Not Eligible")

    elif aptitude < 60:
        st.warning("⚠️ Low Aptitude → Not Eligible")

    else:
        st.success("✅ Eligible for Placement Process")

        # 🤖 ML Prediction
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

        # 🔹 Output with Reason
        if result[0] == 1:
            st.success("🎉 Prediction: Student WILL be Placed")

            st.info("💡 Reason: Good academic performance + skills")

        else:
            st.error("❌ Prediction: Student will NOT be Placed")

            st.info("💡 Reason: Skills or performance not sufficient")
