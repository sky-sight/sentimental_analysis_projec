import string
from collections import Counter

import pandas as pd

import snscrape.modules.twitter as sntwitter


import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import emoji








# reading text file
text = open('read.txt',encoding="utf-8").read()
#text = get_tweets()



# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)

# splitting text into words
tokenized_words = word_tokenize(cleaned_text,"english")
print(tokenized_words)



# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)

# Get emotions text
emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()

        if not clear_line:
            continue

        word, emotion = clear_line.split(':')

        if word in final_words:


            emotion_list.append(emotion)

w = Counter(emotion_list)
print(w)

def sentiment_analyzer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    a = score['pos']
    b = score['neg']
    c = score['neu']
    d = score['compound']

    if(a>b):
        print("class : Positive")
        print("\n")

    else:
        print("Class : Negative ")
        print("\n")


    text = max(a,b,c,d)




    table = {'Emotion': ['Positive','Negative','Neutral','Compound'],
            'Conclusion': [a, b, c, d]}
    df = pd.DataFrame(table)
    print(df)

    def return_key(val):
        for key, value in score.items():
            if value == text:
                return key


    ans = return_key(text)

    print("Highest Polarity of the text is : " + str(text) + " " +
          "and Emotion is : " + str( '\033[1m' + ans))
    print("\n")

    if (text == a):
        print(emoji.emojize(":grinning_face_with_big_eyes:"))
    elif (text == b):
        print("\U0001F923")

    elif (text == c):
        print(emoji.emojize(":zipper-mouth_face:"))

    else:
        print("\U0001F606")


sentiment_analyzer(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
