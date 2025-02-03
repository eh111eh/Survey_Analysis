import pandas as pd

# Function to extract reasons from positive comments
def extract_reasons(comments, sentiments):
    sentiments = sentiments.reindex(comments.index, fill_value="Neutral")  # Align index, set default as Neutral
    positive_comments = comments.loc[sentiments[sentiments == "Positive"].index]
    return positive_comments.reset_index(drop=True)  # Reset index