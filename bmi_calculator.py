

import streamlit as st


# Page config
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #012a1c; /* deep forest green */
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background-color: #014034;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 12px rgba(0, 255, 200, 0.1);
        color: white;
    }

    h1, h2, h3 {
        color: #7fffd4; /* aquamarine */
    }

    .stButton>button {
        background-color: #20c997;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #198754;
    }

    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox div[role="combobox"] {
        background-color: #e3f9f4;
        color: black;
    }

    .css-1offfwp {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💪🏽 BMI Calculator")
st.subheader("Check your Body Mass Index and get wellness tips instantly!")
st.markdown("**Created by Precious Ochiobi**", unsafe_allow_html=True)

# Input fields
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Select", "Female", "Male", "Other"])
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (meters)", min_value=0.5, step=0.01)

# Calculate BMI
if st.button("Calculate BMI"):
    if name and gender != "Select":
        if height > 0:
            bmi = round(weight / (height ** 2), 2)
            st.success(f"Hey {name}, your BMI is: **{bmi} kg/m²**")

        # BMI Categories and Health Tips
        if bmi < 18.5:
            st.warning("⚠️ You are underweight.")
            st.markdown("""
                **💡 Health Tip:**  
                - Eat more frequently and increase calorie intake  
                - Include healthy fats and protein-rich foods  
                - Consult a healthcare provider if needed
            """)
        elif  bmi < 25:
            st.success("✅ You are of normal weight.")
            st.markdown("""
                **💡 Keep it up:**  
                - Maintain a balanced diet  
                - Exercise regularly  
                - Keep monitoring your health metrics
            """)
        elif bmi < 30:
            st.warning("⚠️ You are overweight.")
            st.markdown("""
                **💡 Health Tip:**  
                - Incorporate more physical activity  
                - Reduce intake of sugary and processed foods  
                - Drink more water and track your portions
            """)
        else:
            st.error("❗ You are in the obese range.")
            st.markdown("""
                **💡 Health Tip:**  
                - Start a structured fitness routine  
                - Focus on whole foods and portion control  
                - Seek professional health guidance
            """)
    else:
        st.error("Please fill out all fields correctly.")
    
         


