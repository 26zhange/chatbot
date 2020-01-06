import io
import random
import string
import warnings
import numpy as np
import spacy
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('popular', quiet=True) 
nltk.download('punkt') 
nltk.download('wordnet')
def chat():
    print("Hi, this is Chatbot 1.0")
    
    f=open('chatbot.txt','r',errors = 'ignore')
    raw=f.read()
    raw = raw.lower()# converts to lowercase
    user_input = input("user:")
    bot_response = ""
    responses = {
        "hi":"hi",
        "hello":"hello",
        "what's your name"or "what is your name":"My name is chatbot"

        }
    if '?' or '.' in user_input:
        string.remove('?')
        string.remove('.')
    if user_input in responses:
        print("bot:"+ responses[user_input])
 