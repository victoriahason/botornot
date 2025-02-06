from abc_classes import ABot
from teams_classes import NewUser, NewPost
from datetime import datetime
import json

class Bot(ABot):
    def create_user(self, session_info):
        #print(session_info.influence_target)
        new_users = [
            NewUser(username="vickyy1084", name="Vic", description="head in the clouds!", location="urmomshouse")
        ]
        return new_users

    def generate_content(self, datasets_json, users_list):
        posts = []
        user_posts = datasets_json.posts #so posts is not a json, its a list of dicts!

        ##get the current time (Might need to fix this)
        current_time = datetime.now() #Not sure if this is the right form!
        time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S") + ".000Z"

        for i in range(5): #this is hardcoded, not sure how to make it post a different number of times each subsession
            randompost = user_posts[i]["text"] #Not actually random, always the first one
            text = f"I can't believe someone said: {randompost}"
            posts.append(NewPost(text=text, author_id=users_list[0].user_id, created_at=time_string, user=users_list[0]))
        return posts
