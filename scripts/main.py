import pandas as pd
from preprocess import clean_text, extract_percentages
from sentiment_analysis import analyze_sentiments
from topic_analysis import extract_reasons
from visualisation import plot_sentiments, plot_preferred_splits
import os

# Ensure results directory exists
os.makedirs("results/figures", exist_ok=True)

# Load the survey data
df = pd.read_excel("data/Exams_or_Coursework.xlsx")

# Preprocess comments
df["Cleaned Comments"] = df["Any optional comments?"].dropna().apply(clean_text)

# Extract sentiment analysis
exam_sentiments, coursework_sentiments = analyze_sentiments(df["Cleaned Comments"])
exam_reasons = extract_reasons(df["Cleaned Comments"], exam_sentiments)
coursework_reasons = extract_reasons(df["Cleaned Comments"], coursework_sentiments)

# Extract percentage preferences
df["Percentage Split"] = df["Cleaned Comments"].apply(extract_percentages)

# Convert percentages into structured DataFrame
exam_percentages, coursework_percentages = [], []
for comment, percentages in zip(df["Cleaned Comments"], df["Percentage Split"]):
    if len(percentages) == 2:
        # Two explicit percentages, assume exam first and coursework second
        exam_percentages.append(percentages[0])
        coursework_percentages.append(percentages[1])
    elif len(percentages) == 1:
        if "exam" in comment.lower() and "coursework" not in comment.lower():
            # Single percentage with "exam" mentioned
            exam_percentages.append(percentages[0])
            coursework_percentages.append(100 - percentages[0])
        elif "coursework" in comment.lower() and "exam" not in comment.lower():
            # Single percentage with "coursework" mentioned
            coursework_percentages.append(percentages[0])
            exam_percentages.append(100 - percentages[0])
        else:
            # Skip comments with unclear context
            continue

# Create structured DataFrame for plotting
percentage_df = pd.DataFrame({
    "Exam Percentage": exam_percentages,
    "Coursework Percentage": coursework_percentages
})

# Validate percentages to ensure only values between 0 and 100 are used
percentage_df = percentage_df[
    (percentage_df["Exam Percentage"] >= 0) & (percentage_df["Exam Percentage"] <= 100) &
    (percentage_df["Coursework Percentage"] >= 0) & (percentage_df["Coursework Percentage"] <= 100)
]

# Create labels for splits (e.g., "20/80")
percentage_df["Split Label"] = (
    percentage_df["Exam Percentage"].astype(str) + "/" +
    percentage_df["Coursework Percentage"].astype(str)
)

# Count occurrences of each split
split_counts = percentage_df["Split Label"].value_counts().reset_index()
split_counts.columns = ["Split", "Respondents"]

# Save results
df.to_csv("results/sentiment_results.csv", index=False)
split_counts.to_csv("results/preferred_splits_counts.csv", index=False)
exam_reasons.to_csv("results/reasons_supporting_exam.csv", index=False)
coursework_reasons.to_csv("results/reasons_supporting_coursework.csv", index=False)

# Generate visualizations
plot_sentiments(exam_sentiments.value_counts(), "Sentiment Towards Exams", "exam_sentiments.png")
plot_sentiments(coursework_sentiments.value_counts(), "Sentiment Towards Coursework", "coursework_sentiments.png")
plot_preferred_splits(split_counts)