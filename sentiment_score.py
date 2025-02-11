import json
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
import seaborn as sns

# Open the CSV file and load it into a DataFrame
with open('showerthoughts_posts.csv', 'r') as file:
    df = pd.read_csv(file)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Perform sentiment analysis on the 'title' column
df['sentiment_scores'] = df['title'].apply(lambda x: analyzer.polarity_scores(str(x)))
df['sentiment_compound'] = df['sentiment_scores'].apply(lambda x: x['compound'])
df['sentiment_positive'] = df['sentiment_scores'].apply(lambda x: x['pos'])
df['sentiment_neutral'] = df['sentiment_scores'].apply(lambda x: x['neu'])
df['sentiment_negative'] = df['sentiment_scores'].apply(lambda x: x['neg'])

#new df
df2 = df[['title', 'sentiment_compound', 'sentiment_positive', 'sentiment_neutral', 'sentiment_negative']].copy()

# Save the updated DataFrame with sentiment scores
df2.to_csv('showerthoughts_posts_with_sentiment.csv', index=False)

# Display the first few rows to verify the data
#print(df.head())

# Example: Display basic statistics about sentiment scores
print(df[['sentiment_compound', 'sentiment_positive', 'sentiment_neutral', 'sentiment_negative']].describe())
