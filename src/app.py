import streamlit as st

from src import performance_analysis
from src import weakness_detection
from src import difficulty_engine
from src import question_generator

st.set_page_config(page_title="AI Exam Generator", layout="wide")

st.title("🧠 AI-Driven Personalized Exam Question Generator")

summary = performance_analysis.analyze_performance()
result = weakness_detection.detect_weakness(summary)

st.subheader("📊 Student Performance Analysis")
st.dataframe(result, use_container_width=True)

st.subheader("📝 Personalized Exam Questions")

for _, row in result.iterrows():
    difficulty = difficulty_engine.assign_difficulty(row["level"])
    questions = question_generator.generate_questions(row["topic"], difficulty)

    st.markdown(f"### 📘 {row['topic']} — {difficulty.upper()}")

    if questions:
        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q}")
    else:
        st.warning("No questions available for this topic.")

