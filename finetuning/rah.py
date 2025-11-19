import json
import random

# Load the tweets data
with open('session_16_results.json', 'r') as f:
    real_tweets = json.load(f)

posts = real_tweets["posts"]

# Select a random sample of 200 tweets
post_list = [post["text"] for post in random.sample(posts, 70)]  # Directly use the text

# Open the JSONL file for appending
with open("session_results.jsonl", 'a') as f:
    for post in post_list:
        # Create the desired JSONL structure for the current post
        output_data = {
            "messages": [
                {"role": "system", "content": "You are a twitter user that generates one realistic tweet. No links, use https://t.co/twitter_link. No mentions, use @mention instead."},
                {"role": "user", "content": ""},
                {"role": "assistant", "content": post}  # Directly use the text of the post
            ]
        }
        
        # Append the formatted data to the JSONL file
        json.dump(output_data, f)
        f.write('\n')  # Ensure each entry is on a new line for JSONL format

print("All posts have been added to the JSONL file.")
