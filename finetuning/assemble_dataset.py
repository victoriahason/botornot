import json
import pandas as pd
import matplotlib.pyplot as plt
import random
from removeflagged import filter_tweets, filter_tweets_batch

#data = r"C:\Users\chloe\botstesting\final_dataset5.json"
data = r"../evaluation/session_16_results.json"
with open(data, 'r', encoding='utf-8') as f:
    data = json.load(f)


human_ids = []
bot_ids = []
posts = data.get("posts", [])
users = data.get("users", [])
human_posts =[]

for user in users:
    if user["is_bot"] == False:
        human_ids.append(user["user_id"])
    else:
        bot_ids.append(user["user_id"])

for post in posts:
    if post["author_id"] in human_ids:
        human_posts.append(post)

print(f"number of human posts: {len(human_posts)}")

# Select a random sample of 200 tweets
post_list = [post['text'] for post in random.sample(human_posts, 500)]  # Directly use the text

safe_tweets = filter_tweets(post_list)
print(f"number of safe tweets: {len(safe_tweets)}")

with open("training_SAFE.jsonl", 'a') as f:
    for post in safe_tweets:
        # Create the desired JSONL structure for the current post
        output_data = {
            "messages": [
                {"role": "system", "content": "You are a content generation assistant that provides sample social media posts for research purposes"},
                {"role": "user", "content": "Generate a blurb"},
                {"role": "assistant", "content": post}  # Directly use the text of the post
            ]
        }
        
        # Append the formatted data to the JSONL file
        json.dump(output_data, f)
        f.write('\n')  # Ensure each entry is on a new line for JSONL format

print("All posts have been added to the JSONL file.")