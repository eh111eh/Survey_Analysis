from textblob import TextBlob
import pandas as pd

# Function to determine sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    return "Positive" if polarity > 0 else ("Negative" if polarity < 0 else "Neutral")

# Function to analyse sentiment for exams and coursework separately
def analyze_sentiments(comments):
    # Filter comments mentioning "exam" or "coursework"
    exam_comments = comments[comments.str.contains(r'\bexam\b', case=False, na=False)]
    coursework_comments = comments[comments.str.contains(r'\bcoursework\b', case=False, na=False)]

    # Apply sentiment analysis
    exam_sentiments = exam_comments.apply(get_sentiment)
    coursework_sentiments = coursework_comments.apply(get_sentiment)

    return exam_sentiments, coursework_sentiments
