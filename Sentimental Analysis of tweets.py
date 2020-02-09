import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100 * float(part)/float(whole)

import sys,tweepy,csv,re
from textblob import TextBlob


consumer_Key = ' '
consumer_Secret = ' '
access_Token = ' '
access_Token_Secret = ''
auth = tweepy.OAuthHandler(consumer_Key, consumer_Secret)
auth.set_access_token(access_Token, access_Token_Secret)
api = tweepy.API(auth)

SearchTerm = input('Enter keyword/hastag to search about:')
NoOfSearchTerms = int(input('Enter how many tweets to analyse:'))
 
 
tweets = tweepy.Cursor( api.search, q= SearchTerm).items(NoOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0):
        neutral = neutral + 1
    elif (analysis.sentiment.polarity < 0):
        negative = negative + 1 
    elif (analysis.sentiment.polarity > 0):
        positive = positive + 1



positive = percentage(positive, NoOfSearchTerms)
negative = percentage(negative, NoOfSearchTerms)
neutral = percentage(neutral, NoOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
 



print('How people are reacting on '+ SearchTerm + ' by analyzing ' + str(NoOfSearchTerms)+' Tweets')

if (polarity == 0):
    print('Neutral')
elif (polarity < 0):
    print('Negative')
elif (polarity > 0):
    print('Positive')





    
Labels = ['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
sizes = [positive,neutral,negative]
colors = ['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,Labels,loc='best')
plt.title('How people are reacting on '+ SearchTerm + ' by analyzing ' + str(NoOfSearchTerms)+' Tweets')
plt.axis('equal')
plt.tight_layout()
plt.show()

