import streamlit as st
import pickle
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

vectorizer_path = 'vectorizer.pkl'
model_path = 'model.pkl'
ps = PorterStemmer()


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
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


with open(vectorizer_path, 'rb') as f:
    tfidf = pickle.load(f)

with open(model_path, 'rb') as f:
    model = pickle.load(f)
st.title('Email/SMS Spam Classifier')
input_sms = st.text_area("Enter the message")

if st.button('predict'):
    # preprocessing
    transformed_sms = transform_text(input_sms)

    # vectorize
    vector_input = tfidf.transform([transformed_sms])

    # predict
    result = model.predict(vector_input)[0]

    # display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
