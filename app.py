import pickle
import json
import pandas as pd
import streamlit as st
from datetime import datetime

with open('xgb_model.pkl', 'rb') as f:
    best_xgb_model = pickle.load(f)
 
with open('features.json', 'r') as f:
    features = json.load(f)
    
st.title("Student's Exam Score Prediction 💯")
st.subheader("Input student's information 🔍")

# untuk menampilkan yes dan no instead of 1 and 0
def yes_no_to_binary(value):
    return 1 if value == "Yes" else 0


Hours_Studied = st.number_input("Number of hours spent studying per week", min_value=0, max_value=100)

Attendance = st.number_input("Percentage of classes attended", min_value=0, max_value=100)

Parental_Involvement = st.selectbox("Level of parental involvement in the student's education", ['Low', 'Medium', 'High']) 

Access_to_Resources = st.selectbox("Availability of educational resources", ['Low', 'Medium', 'High'])

Extracurricular_Activities_ui = st.selectbox("Participation in extracurricular activities", ["Yes", "No"]) # yes = 1, no = 0
Extracurricular_Activities = yes_no_to_binary(Extracurricular_Activities_ui)

Sleep_Hours = st.number_input("Average number of hours of sleep per night", min_value=0, max_value=24)

Previous_Scores = st.number_input("Scores from previous exams", min_value=0, max_value=100)

Motivation_Level = st.selectbox("Student's level of motivation", ['Low', 'Medium', 'High']) 

Internet_Access_ui = st.selectbox("Availability of internet access", ["Yes", "No"]) # yes = 1, no = 0
Internet_Access = yes_no_to_binary(Internet_Access_ui)

Tutoring_Sessions = st.number_input("Number of tutoring sessions attended per month", min_value=0, max_value=28)

Family_Income = st.selectbox("Family income level", ['Low', 'Medium', 'High']) 

Teacher_Quality = st.selectbox("Quality of the teachers", ['Low', 'Medium', 'High']) 

School_Type_ui = st.selectbox("Type of school attended", ["Private", "Public"]) # private = 1, public = 0
School_Type = 1 if School_Type_ui == "Private" else 0

Peer_Influence = st.selectbox("Influence of peers on academic performance", ['Positive', 'Neutral', 'Negative']) 

Physical_Activity = st.number_input("Average number of hours of physical activity per week", min_value=0, max_value=168)

Learning_Disabilities_ui = st.selectbox("Presence of learning disabilities", ["Yes", "No"]) # yes = 1, no = 0
Learning_Disabilities = yes_no_to_binary(Learning_Disabilities_ui)

Parental_Education_Level = st.selectbox("Parental_Education_Level",  ['High School', 'College', 'Postgraduate']) 

Distance_from_Home = st.selectbox("Distance from home to school", ['Near', 'Moderate', 'Far']) 

Gender_ui = st.selectbox("Gender of the student", ['Male', 'Female']) # male = 1, female = 0
Gender = 1 if Gender_ui == "Male" else 0


input_data = {
    "Hours_Studied": Hours_Studied,
    "Attendance": Attendance,
    "Parental_Involvement": Parental_Involvement,
    "Access_to_Resources": Access_to_Resources,
    "Extracurricular_Activities": Extracurricular_Activities,
    "Sleep_Hours": Sleep_Hours,
    "Previous_Scores": Previous_Scores,
    "Motivation_Level": Motivation_Level,
    "Internet_Access": Internet_Access,
    "Tutoring_Sessions": Tutoring_Sessions,
    "Family_Income": Family_Income,
    "Teacher_Quality": Teacher_Quality,
    "School_Type": School_Type,
    "Peer_Influence": Peer_Influence,
    "Physical_Activity": Physical_Activity,
    "Learning_Disabilities": Learning_Disabilities,
    "Parental_Education_Level": Parental_Education_Level,
    "Distance_from_Home": Distance_from_Home,
    "Gender": Gender
}

df = pd.DataFrame([input_data])
df = df[features]

# Predict
if st.button("Predict Score"):
    prediction = best_xgb_model.predict(df)[0]
    st.write(f"{'🔴' if prediction < 60 else '🟢'}")
    st.success(f"Predicted Exam Score: **{prediction:.2f}**")
    