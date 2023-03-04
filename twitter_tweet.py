def get_tweets():


    maxTweets = 1000000000000000000000

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:@IndiGo6E').get_items()):
        if i > maxTweets:
            break

            print(f"The tweet content is {tweet.content}")

        return tweet.content
