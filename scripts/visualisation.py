import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure results directory exists
os.makedirs("results/figures", exist_ok=True)

# Function to plot sentiment analysis results
def plot_sentiments(sentiment_counts, title, filename):
    # Dynamically set colors based on sentiment categories
    colors = {"Positive": "green", "Neutral": "gray", "Negative": "red"}
    sentiment_colors = [colors.get(cat, "blue") for cat in sentiment_counts.index]

    plt.figure(figsize=(6, 4))
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=sentiment_colors)
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Comments")
    plt.title(title)
    plt.savefig(f"results/figures/{filename}")
    plt.show()

# Function to plot exam vs coursework percentage split
def plot_preferred_splits(split_counts):
    if split_counts.empty:
        print("No data available for plotting preferred splits.")
        return

    plt.figure(figsize=(12, 6))
    sns.barplot(data=split_counts, x="Split", y="Respondents", palette="Blues_d", edgecolor="black")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
    plt.xlabel("Preferred Split (Exam/Coursework)")
    plt.ylabel("Number of Respondents")
    plt.title("Preferred Exam/Coursework Splits")
    plt.tight_layout()
    plt.savefig("results/figures/preferred_splits.png")
    plt.show()