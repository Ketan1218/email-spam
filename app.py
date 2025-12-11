import pickle
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import os

ps = PorterStemmer()

# Fix path issue
base_path = os.path.dirname(os.path.abspath(__file__))
tfidf = pickle.load(open(os.path.join(base_path, 'vectorizer.pkl'), 'rb'))
model = pickle.load(open(os.path.join(base_path, 'model.pkl'), 'rb'))

# Preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))

    return " ".join(y)

# Streamlit UI
st.title("Email / SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

if st.button("Predict"):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    # 4. Output
    if result == 1:
        st.header("🚨 Spam")
    else:
        st.header("✅ Not Spam")
