#stuff i used in the past that i might need later


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


def generate_tweets2(examples, topics):

    prompt2 = f'''
    
    Create a dataset of 20 thoughts and opinions that capture a very informal, conversational tone typical of social media posts. 
    Use casual language and include slang words and abbreviations common in youth culture. Emphasize the use of expressive punctuation like exclamation marks and all-caps for intensity (e.g., 'K IS SO FUNNY IM CRYING'). 
    Include cultural and contemporary references to figures or events that are currently relevant, and feel free to incorporate rhetorical questions or humorous commentary on everyday situations. 
    Use varied topics such as pop culture, sports, personal anecdotes, philosophical musings, and emotional expressions, ranging from joy to frustration. 
    Incorporate informal language (like 'bruh,' 'shi,' 'bitch,' etc.) and be sure to write in a concise, sometimes fragmented, style that mirrors the brevity of social media interactions. 
    The writing should feel immediate, relatable, and authentic, as if shared among friends in a relaxed, informal digital space.

    Use links or mentions every 5th prompt. No links, use ‘https://t.co/twitter_link’ instead. No mentions, use ‘@mention’ instead.

    '''

    messages_tweets = [
    {
        "role": "developer",  
        "content": prompt1
    },

    {
        "role": "user",
        "content": prompt2
    }]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_tweets,
        presence_penalty = -1,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "tweet_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "tweets": {  
                            "description": "A list of 50 generated tweets",
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": ["tweets"],
                    "additionalProperties": False
                }
            }
        }
    )
    #return(response.choices[0].message)

    arguments_dict = json.loads(response.choices[0].message.content)    
    with open("generated_tweets.json", "w", encoding="utf-8") as json_file:
        json.dump(arguments_dict, json_file, indent=4, ensure_ascii=False)
        
    print(f"Data successfully saved to generated_tweets.json")
    return arguments_dict

def generate_tweets(examples, topics):

    prompt2 = f'''
    Return a JSON file of 20 tweets similar to the tweets this dataset:

    {examples}

    Use the language, syntax and topics of the provided data to generate your tweets. Base your tweets off of this dataset.
    
    Use links or mentions every 5th tweet. No links, use ‘https://t.co/twitter_link’ instead. No mentions, use ‘@mention’ instead.
   
    '''

    messages_tweets = [
    {
        "role": "developer",  
        "content": prompt1
    },

    {
        "role": "user",
        "content": prompt2
    }]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_tweets,
        presence_penalty = -1,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "tweet_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "tweets": {  
                            "description": "A list of 50 generated tweets",
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": ["tweets"],
                    "additionalProperties": False
                }
            }
        }
    )
    #return(response.choices[0].message)

    arguments_dict = json.loads(response.choices[0].message.content)    
    with open("generated_tweets.json", "w", encoding="utf-8") as json_file:
        json.dump(arguments_dict, json_file, indent=4, ensure_ascii=False)
        
    print(f"Data successfully saved to generated_tweets.json")
    return arguments_dict