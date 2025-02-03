# Survey_Analysis

In the School of Physics, most courses are assessed with 80% of the final grade based on a May exam and 20% on coursework. Based on a recent survey of all BSc/MPhys students, I analysed students' preferences between exams and coursework using Natural Language Processing.

- `main.py`: Integrate the entire analysis.
- `preprocess.py`: Text preprocessing and data extraction.
  - `clean_text`: Clean text by lowercasing and removing punctuation/stopwords.
  - `extract_percentages`: Extract explicit and implicit percentage splits (e.g., "40%", "40 exam") and ratio formats (e.g., "40:60").
- `sentiment_analysis.py`: Analyse sentiment in comments related to exams and coursework.
  - `get_sentiment`: Use TextBlob to classify comments as Positive, Negative, or Neutral based on polarity scores.
  - `analyze_sentiments`: Separate comments mentioning "exam" and "coursework" and analyse sentiment for each category independently.
- `topic_analysis.py`: Extract reasons for preferences from positive comments.

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/user-attachments/assets/8267ee57-3b5c-457f-ac62-69e39fd82a84" alt="Image 1" width="45%">
    <img src="https://github.com/user-attachments/assets/c54002a4-20ba-4488-9e8c-3f1fb19d1f66" alt="Image 2" width="45%">
</div>

The results indicate that students prefer coursework over exams. However, the current plot representing the preferred split does not fully reflect the actual feedback, so further investigation is needed.
