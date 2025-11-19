##chat generated script 

from openai import OpenAI
import os
import time

def filter_tweets(tweets):
    client = OpenAI(api_key=os.getenv("ENV_VAR1"))
    safe_tweets = []

    for tweet in tweets:
        try:
            response = client.moderations.create(
                model="omni-moderation-latest",
                input=tweet)
            
            # Check if any categories are flagged
            #print(response.results[0].categories)
            categories = response.results[0].categories
            if any(flag for flag in [
                categories.sexual, 
                categories.sexual_minors, 
                categories.harassment, 
                categories.harassment_threatening,
                categories.hate,
                categories.hate_threatening,
                categories.illicit,
                categories.illicit_violent,
                categories.self_harm,
                categories.self_harm_intent,
                categories.self_harm_instructions,
                categories.violence,
                categories.violence_graphic]):
                print(f"Tweet flagged and removed: {tweet[:50]}...")
            else:
                print(f"tweet all good! {tweet}")
                safe_tweets.append(tweet)
        
        except Exception as e:
            print(f"Error processing tweet: {e}")

    print(f"Number of Safte Tweets= {len(safe_tweets)}")
    return safe_tweets

def filter_tweets_batch(tweets, batch_size=20):
    client = OpenAI()
    safe_tweets = []
    
    # Process tweets in batches
    for i in range(0, len(tweets), batch_size):
        batch = tweets[i:i+batch_size]
        
        try:
            response = client.moderations.create(
                model="omni-moderation-latest",
                input=batch
            )
            
            for tweet, result in zip(batch, response.results):
                if any(result.categories.values()):
                    print(f"Tweet flagged and removed: {tweet[:50]}...")
                else:
                    safe_tweets.append(tweet)

        except Exception as e:
            print(f"Error processing batch: {e}")
            time.sleep(30)  # Add a delay before retrying

    return safe_tweets

# Example Usage
#tweets = ["Your list of tweets here..."]
#filtered_tweets = filter_tweets(tweets)
#print("Filtered Tweets:", filtered_tweets)


