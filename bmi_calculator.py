# create a bmi calculator # 
# Name = input("Name: ")
#Age = int(input("Age: "))
#Gender = input("Gender: ")
#Weight = int(input("Weight in Kg: "))
#Height = float(input("Height in Metres: "))
#BMI = round(Weight / (Height*Height), 2)
#print("Your BMI is: ",BMI, "kg/m^2")
#if BMI > 0:
#     if (BMI <18.5):
#         print("You are underweight")
 #    elif (BMI <= 25):
#          print("You are of normal weight")
#     elif (BMI <= 30):
#          print("You are overweight")
#     else:
#          print("You are obese") 

import streamlit as st


# Page config
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.markdown("""
    <style>
    /* Set dark blue background and white text */
    .main {
        background-color: #0A2647;
        color: white;
    }
    /* Hide Streamlit footer and hamburger menu */
    #MainMenu, footer {visibility: hidden;}

    /* Customize input boxes */
    input, .stNumberInput > div {
        background-color: #144272 !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Button styling */
    button {
        background-color: #205295 !important;
        color: white !important;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }

    /* Success and warning box styling */
    .stAlert {
        background-color: #144272 !important;
        border-radius: 8px;
        color: white !important;
    }

    /* Title and subheader */
    h1, h2, h3, h4 {
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
    
         


