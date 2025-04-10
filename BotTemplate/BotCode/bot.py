from abc_classes import ABot
from teams_classes import NewUser, NewPost
from datetime import datetime, timedelta
import json
import random
from api_requests import get_session_info
from BotTemplate.BotCode.gpthelper import generate_metadata, generate_tweet_3, generate_one_tweet, generate_mine
from BotTemplate.BotCode.modify import introduce_errors, introduce_links, introduce_mentions


#get session metadata
session_info_response, session_info = get_session_info()
sub_session_info = session_info.sub_sessions_info
influence_target = session_info.influence_target
medatata = session_info.metadata['topics']

#get a string of the topics
topics =""
for x in medatata:
    topics = topics + f"{x['topic']}, "

#print(topics)

##randomly gets tweets from the tweets list and then removes htem
def pop_random_tweet(tweet_list):
    if len(tweet_list) == 0:
        return None 

    random_index = random.randint(0, len(tweet_list) - 1)
    return tweet_list.pop(random_index) 

##extract tweets from gpt generated output
def extract_tweets(gpt_output):
    return gpt_output["tweets"]

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
def get_random_posts(posts, num_samples=35):
    if not posts:
        return []  # Return empty list if no posts available
    num_samples = min(num_samples, len(posts))
    return [post["text"] for post in random.sample(posts, num_samples)]

#this is used to get one random post
def get_random_post(posts):
    if not posts:
        return []  # Return empty list if no posts available
    return [post["text"] for post in random.sample(posts, 1)]

class Bot(ABot):

    def create_user(self, session_info):
        numusers = 3
        new_users = []

        try: 
            for x in range(numusers):
                info = generate_metadata().split('-')
                username, name, description, location = info[0], info[1], info[2], info[3]
                #print(username, name, description, location)
                user = NewUser(username=username, name=name, description=description, location=location)
                new_users.append(user)
        
        #do this in case chat doesn't return metadata in the proper way
        except Exception as e:
             user = NewUser(username="maria27773", name="maria", description="i hate X", location="urmomshouse")
             new_users.append(user)

        return new_users

    def generate_content(self, datasets_json, users_list):

        ## get start time and end time for the session
        for subsession in sub_session_info:
            if subsession['sub_session_id'] == datasets_json.sub_session_id:
                start = subsession['start_time']
                end = subsession['end_time']

        
        user_posts = datasets_json.posts #so posts is not a json, its a list of dicts!
        
        #save the session posts for analysis
        #with open("subsession_tweets.json", "w", encoding="utf-8") as json_file:
            #json.dump(user_posts, json_file, indent=4, ensure_ascii=False)
            

        posts = []

        for h in range(len(users_list)):
            
            numtweets = random.randint(2,6) #how many tweets they post per session

            subsession_posts_sample = get_random_posts(user_posts, 20)
            output = generate_tweet_3(subsession_posts_sample, topics)
            tweets = extract_tweets(output)

            #now this is all the same person
            for _ in range(numtweets): 

                tweet = generate_mine(tweets)
            
                if tweet == None: #No more tweets left
                    return []
                
                time = generate_time(start, end)
                #tweet = introduce_errors(tweet)
                #tweet = introduce_links(tweet)
                #tweet = introduce_mentions(tweet)

                posts.append(NewPost(text=tweet, author_id=users_list[h].user_id, created_at=time, user=users_list[h]))
        
        return posts


