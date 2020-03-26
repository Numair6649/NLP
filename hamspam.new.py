#import data/read file
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd    
data =pd.read_csv('smsspamcollection',sep ='\t',names=["label","message"])

#function to remove punctuations and stop words
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def text_process(msg):
    nupunc = [char for char in msg if char not in string.punctuation]
    nopunc = ''.join(nupunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# split test train data
from sklearn.model_selection import train_test_split
msg_train, msg_test, label_train, label_test = train_test_split(data['message'],data['label'], test_size=0.2)

#vectorization of training input data
from sklearn.feature_extraction.text import CountVectorizer
bow_transformer = CountVectorizer(analyzer = text_process).fit(msg_train)
msgtrain_bow = bow_transformer.transform(msg_train)

#tfidf transformation
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(msgtrain_bow)
msgtrain_bow_tfidf = tfidf_transformer.transform(msgtrain_bow)




####performing multinomial naive bayes classification ###
from sklearn.naive_bayes import MultinomialNB
classification = MultinomialNB().fit(msgtrain_bow_tfidf,label_train)




#generating score on training data
classification.score(msgtrain_bow_tfidf,label_train)

#generating score on test data
msgtest_bow = bow_transformer.transform(msg_test)
msgtest_bow_tfidf = tfidf_transformer.transform(msgtest_bow)
classification.score(msgtest_bow_tfidf,label_test)

#generating confusion metrics
predicted = classification.predict(msgtest_bow_tfidf)
from sklearn import metrics
metrics.confusion_matrix(label_test,predicted)


#example prediction
msg_new = ['Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&Cs apply 08452810075over18s']
#msg_new = ['free entry win tickects message send  money account number you win lottery98786798768976 sms lucky offer']
msg_new_bow = bow_transformer.transform(msg_new)
msg_new_bow_tfidf = tfidf_transformer.transform(msg_new_bow)
classification.predict(msg_new_bow_tfidf)

