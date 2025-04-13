# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tYxY5PrsuM9yk4j-qBVWjkgZ8i7DegBy
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install streamlit

pip install streamlit pandas scikit-learn

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('/content/drive/MyDrive/AI LaB/Lab Project/career_ao_star_dataset.csv')

# Encode categorical columns
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

# A* style career recommendation based on user input
def a_star_search(education, skills, interest):
    node = {'Education': education, 'Skills': skills, 'Interest': interest}
    career_scores = {
        "Engineer": (education == "Science" and interest == "Technology" and skills == "High"),
        "Programmer": (education == "Science" and interest == "Technology" and skills == "Medium"),
        "Banker": (education == "Commerce" and interest == "Finance" and skills == "High"),
        "Manager": (education == "Commerce" and interest == "Finance" and skills == "Medium"),
        "Artist": (education == "Humanities" and interest == "Arts" and skills == "Low"),
        "Writer": (education == "Humanities" and interest == "Arts" and skills == "High"),
    }

    # Find the best career based on the score
    scores = {career: score for career, score in career_scores.items()}
    best_career = max(scores, key=scores.get)

    return best_career

# Streamlit interface
def career_advisor():
    st.title("Career Recommendation - A* Search")

    # Input fields
    education = st.selectbox('Select Education Level:', ['Science', 'Commerce', 'Humanities'])
    skills = st.selectbox('Select Skills Level:', ['High', 'Medium', 'Low'])
    interest = st.selectbox('Select Area of Interest:', ['Technology', 'Finance', 'Arts'])

    # Make a recommendation
    recommended_career = a_star_search(education, skills, interest)

    # Display the recommended career
    st.write(f"🎯 Recommended Career: {recommended_career}")

if __name__ == "__main__":
    career_advisor()