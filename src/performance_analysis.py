import pandas as pd

def analyze_performance():
    """
    Reads student results and calculates topic-wise accuracy
    """
    df = pd.read_csv("data/student_results.csv")

    summary = df.groupby("topic")["correct"].mean().reset_index()
    summary["accuracy"] = summary["correct"] * 100

    return summary
