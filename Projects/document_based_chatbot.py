import numpy as nump
import nltk
import string
import random

f = open('/content/mlinfotochat','r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

import random

GREET_INPUTS = ("hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening", "yo", "what's up")
GREET_RESPONSES = ("Hello there!", "Hi!", "Hey!", "Greetings!", "Good morning/afternoon/evening to you too!", "Yo!", "What's up?")

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
  robo1_response=''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"Hey! I apologize, as I am still under development, I can't find anything else you asked for."
    return robo1_response
  else:
    robo1_response = robo1_response+sent_tokens[idx]
    return robo1_response

flag = True
print("Hello, I am ChatB, a AI language model here to assist you. Would you like to engage in a conversation with my counterpart,?")
while(flag==True):
  user_response = input()
  user_response=user_response.lower()
  if(user_response!='exit'):
    if(user_response=='thanks' or user_response=='thank you'):
      flag=False
      print("chatB:  It was my pleasure!")
    else:
      if(greet(user_response)!=None):
        print("chatB:  "+greet(user_response))
      else:
        sent_tokens.append(user_response)
        word_tokens=word_tokens+nltk.word_tokenize(user_response)
        final_words=list(set(word_tokens))
        print("chatB:  ",end="")
        print(response(user_response))
        sent_tokens.remove(user_response)
  else:
      flag=False
      print("chatB:  GreaTTalk inbetween, Thanks! <3")
