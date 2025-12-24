import sys
import os

# 🔑 IMPORTANT: Add src directory to Python path (for Streamlit Cloud)
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from performance_analysis import analyze_performance
from weakness_detection import detect_weakness
from difficulty_engine import assign_difficulty
from question_generator import generate_questions

st.set_page_config(page_title="AI Exam Generator", layout="wide")

st.title("🧠 AI-Driven Personalized Exam Question Generator")

# Step 1: Analyze performance
summary = analyze_performance()

# Step 2: Detect weaknesses
result = detect_weakness(summary)

st.subheader("📊 Student Performance Analysis")
st.dataframe(result, use_container_width=True)

st.subheader("📝 Personalized Exam Questions")

# Step 3: Generate questions per topic
for _, row in result.iterrows():
    difficulty = assign_difficulty(row["level"])
    questions = generate_questions(row["topic"], difficulty)

    st.markdown(f"### 📘 {row['topic']} — {difficulty.upper()}")

    if questions:
        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q}")
    else:
        st.warning("No questions available for this topic.")
