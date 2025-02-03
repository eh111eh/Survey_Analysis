import pandas as pd
import string
import re

# Define a basic set of stopwords
STOPWORDS = set(["i", "me", "my", "we", "our", "ourselves", "you", "your", "he", "him", "his",
                 "she", "her", "it", "they", "them", "what", "which", "who", "this", "that",
                 "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
                 "have", "has", "had", "do", "does", "did", "doing", "a", "an", "the", "and",
                 "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
                 "with", "about", "against", "between", "into", "through"])

# Function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))  # Remove punctuation & lowercase
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]  # Remove stopwords
    return ' '.join(words)

# Function to extract percentage mentions from comments
def extract_percentages(comment):
    if not isinstance(comment, str):
        return []

    # Explicit percentage mentions
    percentages = re.findall(r'(\d{1,3})\s*%', comment)

    # Ratio formats (e.g., "40:60" or "40/60")
    ratios = re.findall(r'(\d{1,3})\s*[/:]\s*(\d{1,3})', comment)

    # Implicit mentions like "40 exam" or "60 coursework"
    implicit_exam = re.findall(r'(\d{1,3})\s*exam', comment, re.IGNORECASE)
    implicit_coursework = re.findall(r'(\d{1,3})\s*coursework', comment, re.IGNORECASE)

    # Process extracted values
    if percentages:
        return [int(p) for p in percentages if 0 <= int(p) <= 100]
    elif ratios:
        a, b = map(int, ratios[0])
        if a + b > 0:  # Prevent division by zero
            return [round((a / (a + b)) * 100), round((b / (a + b)) * 100)]
    elif implicit_exam:
        exam = int(implicit_exam[0])
        if 0 <= exam <= 100:
            return [exam, 100 - exam]
    elif implicit_coursework:
        coursework = int(implicit_coursework[0])
        if 0 <= coursework <= 100:
            return [100 - coursework, coursework]
    return []