import streamlit as st
import pickle
import pandas as pd

# Load the models and vectorizer
with open("/Users/apple/Downloads/Project/Sentiment-Analysis-End-to-End-NLP-Project/research/Random_Forest_sentiment_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

with open("/Users/apple/Downloads/Project/Sentiment-Analysis-End-to-End-NLP-Project/research/sentiment_model.pkl", "rb") as f:
    other_model = pickle.load(f)

with open("/Users/apple/Downloads/Project/Sentiment-Analysis-End-to-End-NLP-Project/research/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("💬 Sentiment Analysis App")
st.markdown("Enter a sentence below and get the predicted sentiment.")

# Model selection
model_option = st.radio("Choose a model:", ("Random Forest", "Other Model"))

# Text input
user_input = st.text_area("Enter your text here:", height=150)

# Prediction function
def predict_sentiment(text, model):
    if not text.strip():
        return "Please enter some text."
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]

# Button to trigger prediction
if st.button("Predict Sentiment"):
    model = rf_model if model_option == "Random Forest" else other_model
    result = predict_sentiment(user_input, model)
    st.markdown(f"### 🧠 Prediction: **{result}**")

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name]")
