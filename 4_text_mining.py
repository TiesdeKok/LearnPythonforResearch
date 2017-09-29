
# coding: utf-8

# # python hands-on session

# By: Ties de Kok  
# Version: Python 2.7 (see any notes for Python 3.5)

# 1. handling files
# 2. data handling
# 3. web scraping
# 4. **text mining**
# 5. (interactive) visualisations

# ## Introduction

# In the previous notebooks we have either worked with quantitative data (Pandas) or we have extracted information from webpages or documents.  
# In this notebook we will try to convert qualitative data, more specifically text, into something that we can use for analysis.  
# 
# Extracting this "information" from text is often called "text mining" or "natural language processing" (NLP)
# 
# NLP is a sub-field that can easily fill an entire separate workshop, here I will only touch upon the basics.

# Basic steps for NLP:
# 1. Obtain and load some raw text
# 2. Process this text ("clean" the text)
# 3. Analyse the text

# **Note: For the sake of consistency I have prepared this notebook with Python 2.7**  
# **However, when doing text analysis I highly recommend to use Python 3.5 instead because of improved unicode support!**

# ## Overview of tools

# There are many different "NLP" tools in the Python eco-system.  
# 
# Several well known options:  
# 1. NLTK (Natural Language Toolkit) (http://www.nltk.org/)
# 2. TextBlob (http://textblob.readthedocs.io/en/dev/#)
# 3. Spacy (https://spacy.io/)
# 
# **Installation instructions:**
# 1. NLTK: 
#     - `pip install nltk` 
#     - run `nltk.download()` **in the notebook** to download and install the NLTK data
# 2. TextBlob: 
#     - `pip install -U textblob`
#     - `python -m textblob.download_corpora` **in the console** to download data
# 3. Spacy: 
#     - `conda install -c spacy spacy=0.101.0`
#     - `python -m spacy.en.download` **in the console** to download data

# ## Get some example text

# We obviously need some text to extract information from, for this example we will get some text from Twitter.  
# 
# **Note: You can skip this step by loading the pre-downloaded tweets, this is explained if you scroll down a couple of cells.**
# 
# To download some twitter data we will use the `tweepy` package. (http://tweepy.readthedocs.io/en/v3.5.0/)  
# Install `tweepy` using `pip install tweepy`.  
# 
# Before we can use `tweepy` we need a twitter account that allows us to use the API.  
# 
# Go to: https://apps.twitter.com and login with your twitter account.  
# Create a new app and fill something in like:
# 
# ![](https://dl.dropboxusercontent.com/u/1265025/python_tut/Python_tweepy.PNG)
# 
# *Note:* you need to have verified your Twitter account with your mobile phone (https://twitter.com/settings/devices)
# 
# After you have created your app click the `Keys and Access Tokens` tab.  
# Click `Generate my access token and Token Secret`.
# 
# You will need 4 things from this page:  
# 1. Consumer Key
# 2. Consumer Secret
# 3. Access Token
# 4. Access Token Secret

# ### Authenticate ourselfs

# In[1]:

import tweepy
from tweepy import OAuthHandler


# Fill in your details below:

# In[ ]:

consumer_key = 'YOUR-CONSUMER-KEY'  
consumer_secret = 'YOUR-CONSUMER-SECRET'  
access_token = 'YOUR-ACCESS-TOKEN'  
access_secret = 'YOUR-ACCESS-SECRET'  


# In[3]:

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# ### Download 20 most recent tweets from @TheEconomist

# In[4]:

tweets = []
for status in tweepy.Cursor(api.user_timeline, id="TheEconomist").items(20):
    tweets.append(status.text)
    print(status.text)


# ### Note:

# If you cannot or do not want to use `tweepy` you can also load the tweets from a file that I included:  
# 
# ```
# import pickle
# tweets = pickle.load(open("tweets.p", "rb"))
# ```
# 
# If you want to follow the examples below it is best to load the data from the file as well.

# In[ ]:

import pickle
tweets = pickle.load(open("tweets.p", "rb"))


# ## Clean the text (pre-processing)

# We, for example, are not interested in the link. So we would like to remove any links:

# In[3]:

import re


# In[4]:

def remove_link(text):
    clean = re.sub(r'http(.*)', '', text)
    clean = clean.strip()
    return clean


# In[5]:

c_tweets = [remove_link(x) for x in tweets]
c_tweets[0:5]


# ## Basic example NLTK

# In[6]:

import nltk


# ### Split text into a list of sentences

# In[7]:

nltk.sent_tokenize(c_tweets[1])


# In[8]:

sentences = [nltk.sent_tokenize(x) for x in c_tweets]
sentences[0:3]


# ### Split text into a list of words

# In[9]:

words = [nltk.word_tokenize(x) for x in c_tweets]
words[0]


# ### Part-of-speech tagging

# In[10]:

pos = [nltk.pos_tag(x) for x in words]
pos[0]


# ### Lemmatizer

# In[11]:

words[0][6]


# In[12]:

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize(words[0][6])


# ### Classification

# You can do a lot of classification tasks using `NLTK` but they require a training set.  
# To prevent turning this notebook into a `machine learning` tutorial I will skip this, however the internet is full of resources.  
# For example:  
# https://github.com/nltk/nltk/wiki/Sentiment-Analysis

# ## Basic example TextBlob

# In[13]:

from textblob import TextBlob


# ### Turn text into a `TextBlob`

# In[14]:

text_tb = [TextBlob(x) for x in c_tweets]


# In[15]:

text_tb[0]


# ### Access characteristics of a piece of text

# In[16]:

text_tb[0].tags


# In[17]:

text_tb[0].noun_phrases


# In[18]:

text_tb[0].sentences


# In[19]:

text_tb[0].words


# ### Lemmatize

# In[20]:

for x in text_tb[0].words:
    print(x, x.lemmatize())


# ### Retrieve definition of a word

# In[21]:

for x in text_tb[0].words[0:6]:
    print(x, x.definitions[0])


# ### Detect language

# In[22]:

for x in text_tb[0:5]:
    print(x.detect_language())


# ### Sentiment Analysis

# *Note:* when it comes to sentiment analysis there really is no one-size-fits all solution.  
# The below is decent but it is better to use a sentiment resource (e.g. a list with positive / negative words) that is custom to your type of text and goal.

# In[23]:

for text in text_tb[0:5]:
    for sentence in text.sentences:
        print(sentence)
        print(sentence.sentiment)


# ## Basic example Spacy

# *Note:* Loading the English file might take a while.

# In[24]:

from spacy.en import English
parser = English()


# In[25]:

spacy_text = [parser(x) for x in c_tweets]


# In[26]:

spacy_text[1]


# ### Access characteristics of text

# In[27]:

for token in spacy_text[3]:
    print(token.orth_, token.lower_, token.lemma_, token.prob)


# *Note, **prob**:* The unigram log-probability of the word, estimated from counts from a large corpus, smoothed using Simple Good Turing estimation. 

# ### Detect named entities

# In[28]:

for token in spacy_text[1]:
    if token.ent_type_ != "":
        print(token, token.ent_type_)


# ## Sentiment Analysis

# There are also packages available that are more focussed on particular tasks, such as sentiment analysis.  
# One that is, for example, easy to use is: `AFINN` --> http://neuro.compute.dtu.dk/wiki/AFINN
# 
# In essence it is a word list but you can also install it directly by doing `pip install afinn`

# In[29]:

from afinn import Afinn
afinn = Afinn()


# In[30]:

afinn.score('This is utterly excellent!')


# In[31]:

for text in spacy_text:
    for sentence in text.sents:
        print(afinn.score(sentence.text), sentence)


# ## Search Reddit for threads about Egyptian Airline crash

# To get some more text to work with we will extract some text from the website http://www.reddit.com  
# 
# We could directly use the API and `requests` but it is easier to use a wrapper called `praw`.
# 
# You can install `praw` by running `pip install praw` and information is available here: https://praw.readthedocs.io/en/stable/index.html

# ### Getting the Reddit data

# In[32]:

import praw


# In[33]:

r = praw.Reddit(user_agent='Python tutorial')


# In[34]:

new_news = r.get_subreddit('worldnews').get_top_from_day(limit=100)


# In[35]:

submission_titles = []
for submission in new_news:
    submission_titles.append(submission.title)


# *Note:* you can load the submission titles I am using by loading:  
# ```
# import pickle
# submission_titles = pickle.load(open(r'submission_titles.p', 'r'))
# ```

# In[36]:

submission_titles[0:5]


# ### Find reddit threads that talk about the Egyptian airplane that went missing

# We could use a very simple word-search based approach:

# In[37]:

for x in submission_titles:
    if 'egypt' in x.lower():
        print(x)


# However, the problem is that we also get result that are not related to the plane crash, such as:
# > Egypt Gets $25 Billion Loan From Russia for Nuclear Plant

# We can try to add additional keywords such as 'plane' and 'flight'

# In[38]:

for x in submission_titles:
    if 'egypt' in x.lower():
        if 'plane' in x.lower() or 'flight' in x.lower():
            print(x)


# However, this becomes tedious if we want to keep adding additional keywords such as 'aircraft'.  
# A better approach is to, for example, include synonyms for the word 'airplane'.  
# 
# We can do this using one of the above libraries but we could also use `PyDictionary`, `pip install PyDictionary`

# In[39]:

from PyDictionary import PyDictionary
dictionary=PyDictionary()


# In[40]:

print(dictionary.synonym('airplane'))


# In[41]:

plane_words = dictionary.synonym('airplane') + ['airplane', 'flight']


# In[42]:

for x in submission_titles:
    if 'egypt' in x.lower():
        if any(word in x.lower() for word in plane_words):
            print(x)


# ## Machine learning: basic topic classification

# **Note:** I have little experience with machine learning, I base the code below on examples for the sake of illustration

# ### Get some data that we can classify:

# We will download the titles of the top posts from two sub-reddits: '/r/Python' and '/r/Java'.  
# 
# The goal is to build a classifier that can identify a title as being from either '/r/Python' or '/r/Java'.

# In[59]:

top_python = r.get_subreddit('python').get_top_from_year(limit=300)
top_python = [x.title for x in top_python]
top_python = top_python[50:]


# In[61]:

for x in top_python[0:5]:
    print(x)


# In[60]:

top_java = r.get_subreddit('java').get_top_from_year(limit=300)
top_java = [x.title for x in top_java]
top_java = top_java[50:]


# In[62]:

for x in top_java[0:5]:
    print(x)


# *Note:* I use `[50:]` to remove the first 50 titles as they are often not representative

# Convert it into a data structure that we can use for machine learning:

# In[110]:

python_tuple = tuple((x, 0, 'python') for x in top_python)
java_tuple = tuple((x, 1, 'java') for x in top_java)
data = list(python_tuple + java_tuple)


# ### Import machine learning tools

# *Note:* we will use `sklearn` which comes with `Anaconda`
# 
# This example is based on: http://nbviewer.jupyter.org/github/gmonce/scikit-learn-book/blob/master/Chapter%202%20-%20Supervised%20Learning%20-%20Text%20Classification%20with%20Naive%20Bayes.ipynb

# In[165]:

from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
import numpy as np


# ### Split the sample into our training and evaluation set:

# In[111]:

from random import shuffle
shuffle(data)


# In[145]:

SPLIT_PERC = 0.75
split_size = int(len(data)*SPLIT_PERC)

data_d = [x[0] for x in data]
data_t = [x[1] for x in data]

X_train = data_d[:split_size]
X_test = data_d[split_size:]
y_train = data_t[:split_size]
y_test = data_t[split_size:]


# ### Text Classification with Naïve Bayes

# In[146]:

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer


# In[147]:

def evaluate_cross_validation(clf, X, y, K):
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    scores = cross_val_score(clf, X, y, cv=cv)
    print scores
    print ("Mean score: {0:.3f} (+/-{1:.3f})").format(
        np.mean(scores), sem(scores))


# The initial data consists of text, while we need numerical data for the classifier.  
# In the example below I use `CountVectorizer` : http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

# In[148]:

clf = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB()),
])


# In[149]:

evaluate_cross_validation(clf, data_d, data_t, 5)


# In[150]:

from sklearn import metrics

def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    
    clf.fit(X_train, y_train)
    
    print "Accuracy on training set:"
    print clf.score(X_train, y_train)
    print "Accuracy on testing set:"
    print clf.score(X_test, y_test)
    
    y_pred = clf.predict(X_test)
    
    print "Classification Report:"
    print metrics.classification_report(y_test, y_pred)


# In[151]:

train_and_evaluate(clf, X_train, X_test, y_train, y_test)


# ### Eye-ball the results:

# In[159]:

expected_group = zip(X_test, y_test, clf.predict(X_test))


# *Note:* we code 0 to indicate Python and 1 to indicate Java:

# In[164]:

for text, actual, predict in expected_group[20:40]:
    print(text, actual, predict)

