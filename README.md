# Sentiment Analysis for Airline Reviews

## About the Project
This project is a sentiment analysis system designed to classify airline reviews as either Positive or Negative based on their textual content. It uses TF-IDF vectorization to convert text into numerical features and trains a Logistic Regression model for classification. The model is either loaded from saved files or trained anew using an airline reviews dataset.

## Uniqueness
- Automatic Model Loading: If a trained model and vectorizer exist, they are loaded automatically; otherwise, a new model is trained and saved.
- Text Preprocessing: The system applies case normalization, punctuation removal, number removal, and stopword filtering.
- Efficient TF-IDF Vectorization: The input text is transformed into numerical data for machine learning.
- Logistic Regression Classification: A simple yet effective machine learning model for sentiment analysis.

## Steps to Run the Project
### Prerequisites
Ensure you have Python installed (preferably Python 3.8 or later).


### Running the Project
1. Download the project files.
2. Run the script:
   'pip install -r requirements.txt'
   'python mergedataset.py'
3. Place your dataset file `AirlineReviews.csv` in the same directory. Run the script:
   'python main.py'
4. Enter a review when prompted, and get instant feedback on whether it is Positive or Negative.

NOTE: Please wait for some time when the code is running for the first time because it takes some time to train the model. From next time the model is saved and the saved model is used.


## Sample Review Inputs

Enter your Review:
"The flight was amazing, very comfortable and the staff was friendly!"
Output: Positive

Enter your Review:
"The worst experience ever! The flight was delayed and the seats were horrible."
Output: Negative


