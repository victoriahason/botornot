from abc_classes import ABot
from teams_classes import NewUser, NewPost
from datetime import datetime, timedelta
import json
import random
from api_requests import get_session_info
from BotTemplate.BotCode.gpthelper import generate_tweets
import re


#get session metadata
session_info_response, session_info = get_session_info()
sub_session_info = session_info.sub_sessions_info
influence_target = session_info.influence_target
medatata = session_info.metadata

##randomly gets tweets from the tweets list and then removes htem
def pop_random_tweet(tweet_list):
    if len(tweet_list) == 0:
        return None 

    random_index = random.randint(0, len(tweet_list) - 1)
    return tweet_list.pop(random_index) 

##extract tweets from gpt generated output
def extract_tweets(gpt_output):
    # Extract content text
    if hasattr(gpt_output, 'content'):
        text = gpt_output.content
    else:
        text = str(gpt_output)  # Fallback to string conversion if it's not an object

    # Remove surrounding single or double quotes if present
    text = text.strip("'\"")

    # Split on ', ' while ignoring commas inside links or special cases
    tweets = re.split(r"',\s*'", text)

    # Clean up individual tweets
    cleaned_tweets = [tweet.strip("'\"") for tweet in tweets if tweet.strip()]

    return cleaned_tweets

#function that generates a random time within the subsession window
def generate_time(start, end):
        # Convert string inputs to datetime objects
        start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
        end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Generate a random timestamp in the given range
        random_seconds = random.uniform(0, (end_dt - start_dt).total_seconds())
        random_dt = start_dt + timedelta(seconds=random_seconds)

        # Format back to the required string format
        return random_dt.strftime("%Y-%m-%dT%H:%M:%S") + ".000Z"

#functiont that randomly selects 50 posts from the subsession posts
def get_random_posts(posts, num_samples=30):
    if not posts:
        return []  # Return empty list if no posts available

    # Ensure we don't sample more than available posts
    num_samples = min(num_samples, len(posts))

    # Randomly sample posts and extract only the text
    return [post["text"] for post in random.sample(posts, num_samples)]

class Bot(ABot):

    def create_user(self, session_info):
        new_users = [
            NewUser(username="Twitterfiend23", name="Emma", description="I could do this all day!", location="austin")
        ]
        return new_users

    def generate_content(self, datasets_json, users_list):

        ## get start time and end time for the session
        for subsession in sub_session_info:
            if subsession['sub_session_id'] == datasets_json.sub_session_id:
                start = subsession['start_time']
                end = subsession['end_time']

        posts = []
        user_posts = datasets_json.posts #so posts is not a json, its a list of dicts!
        subsession_posts_sample = get_random_posts(user_posts)

        output = generate_tweets(subsession_posts_sample)
        tweets = extract_tweets(output)

        numtweets = random.randint(3,8) #fix this
        for i in range(numtweets): #this is hardcoded, not sure how to make it post a different number of times each subsession
            text = pop_random_tweet(tweets)
            if text == None: #No more tweets left
                return []
            time = generate_time(start, end)
            posts.append(NewPost(text=text, author_id=users_list[0].user_id, created_at=time, user=users_list[0]))
        
        return posts
