import pandas as pd
import re
import string
import nltk
import pickle
import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download stopwords
nltk.download('stopwords')

# Define file paths
MODEL_FILE = "sentiment_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Check if model exists
if os.path.exists(MODEL_FILE) and os.path.exists(VECTORIZER_FILE):
    with open(MODEL_FILE, 'rb') as model_file, open(VECTORIZER_FILE, 'rb') as vectorizer_file:
        model = pickle.load(model_file)
        tfidf_vectorizer = pickle.load(vectorizer_file)
    print("Loaded existing model and vectorizer.")
else:
    # Load Dataset
    df = pd.read_csv("AirlineReviews.csv")
    df = df[['Review', 'OverallScore']].dropna().head(2000)
    df['Sentiment'] = df['OverallScore'].apply(lambda x: 1 if x >= 7 else 0)
    
    # Apply Preprocessing
    df['CleanedReview'] = df['Review'].apply(preprocess_text)
    
    # Train Vector
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)
    X = tfidf_vectorizer.fit_transform(df['CleanedReview'])
    y = df['Sentiment']
    
    # Train Logistic Regression Model
    model = LogisticRegression()
    model.fit(X, y)
    
    # Save Model
    with open(MODEL_FILE, 'wb') as model_file, open(VECTORIZER_FILE, 'wb') as vectorizer_file:
        pickle.dump(model, model_file)
        pickle.dump(tfidf_vectorizer, vectorizer_file)
    print("Trained and saved new model and vectorizer.")

def predict_sentiment(review):
    review = preprocess_text(review)
    review_tfidf = tfidf_vectorizer.transform([review])
    prediction = model.predict(review_tfidf)[0]
    return "Positive" if prediction == 1 else "Negative"

# Get user input
text = input("Enter your Review:\n")
print(predict_sentiment(text))
