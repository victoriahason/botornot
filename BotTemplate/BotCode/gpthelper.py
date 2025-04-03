from openai import OpenAI
import os
import json


client = OpenAI(api_key=os.getenv("ENV_VAR1"))

modelid='ft:gpt-4o-mini-2024-07-18:network-dynamics-lab::BIMvkIVN'

#for testing
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


messages_metadata = [
    {
        "role": "developer",  
        "content": "You are a helpful assistant that generates realistic twitter user metadata"
    },

    {
        "role": "user",
        "content": f''' Generate one set of user metadata in exactly this format:

        username-name-description-location-
        
        Here is an example:
        jamie66679-Jamie-These bitches don\u2019t even know who Rick James is!!-Philadelphia, PA

        '''
    }
]

prompt1 = "You are a helpful assistant that generates a JSON dataset of realistic tweets. "

##took tthis out
#Write your tweets on the following topics: {topics}


def generate_tweet_3(examples, topics):

    prompt2 = f'''
    The below dataset is a set of 35 thoughts and opinions on various topics.
    Please analyze the dataset thouroughly, and explain the specifics of its distinctive stylistic elements in terms of vocabulary, sentence structure, topics, sentiment, etc. 
    Analyse what words seem important to the data and use these words in your blurbs.
    You must be very specific to the dataset. For example, if the dataset references specific people or events, you can bring these up as well.

    Finally, generate a JSON dataset of 10 blurbs on the same topics. make it extremely similar in style to the rest of the data. 
    
    Here are 3 important things to keep in mind:
    1. Use the slang and important words discovered in your generated blurbs.
    2. Each blurb should be around 40 words (130 characters).
    3. Don't use emojis.

    Here is the dataset:
    {examples}
    '''

#"content": "you are an expert analyst and linguist who is helping create blurbs based off a dataset. "
#DESCRIPTION: A list of 10 generated blurbs similar to the dataset.
    messages_tweets = [
    {
        "role": "developer",  
        "content": "You are a content generator that create blurbs based off a dataset"},
    {
        "role": "user",
        "content": prompt2
    }]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_tweets,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "tweet_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "analysis": {  
                            "description": "write your analysis about the distinctive stylistic elements in terms of vocabulary, sentence structure, and sentiment",
                            "type": "string",
                            },
                        "number of interactions": {  
                            "description": "How many tweets use @mention or https://t.co/twitter_link? You should aim to keep the same ratio",
                            "type": "string",
                            },
                        "slang Used":{
                            "description": "write the informal slang or swear words that are used. Use these words in your blurbs."
                        },
                        "topics": {  
                            "description": "write the 3 main topics the blurbs are on here.",
                            },
                        "important words and specific things/people mentioned": {  
                            "description": "Write the most important words in the dataset. Use specific words instead of generic words. Use these words in your blurbs.",
                            "type": "string",
                            },

                        "tweets": {  
                            "description": "Generate 10 blurbs",
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

    arguments_dict = json.loads(response.choices[0].message.content)    
    with open("generated_tweets.json", "r") as json_file:
        existing_data = json.load(json_file)
        existing_data.append(arguments_dict)
    
    with open("generated_tweets.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
        
    #print(f"Data successfully saved to generated_tweets.json")
    return arguments_dict


    

def generate_metadata():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages_metadata
    )
    result = response.choices[0].message.content
    return(result) 





#generate_tweet_3(['Oh Jesus I never thought I’d agree with WTF James Charles has to say but here we are https://t.co/twitter_link', 'bruh this shi mad crazy', 'NHL Play: \n\nSabres Red Wings Over 6 - 120\n\nMoving', 'Jesus on the Radio.', 'Would it be easier to build from earth to space or from space down to earth. If there is no gravity in space could you technically build down. I wonder where "gravity" would start to  pull the structure down, or is zero gravity stronger then gravity. #questions #science #earth', '“I’ll love.\n\nEven for that first time.\n\nAnd you  for any of our last times …\n\n+ I took from you and I…\n\nYou quit.\n\nAnd I understand why”\n\nLove you beautiful woman!\n\nAlways will.', 'K IS SO FUNNY IM CRYING', 'BREAKING NEWS : Justin fields will be traded to the Steelers tomorrow noon 🕛 you heard first \n\n#CTESPN', 'Watching Poor Things. This is an absolutely tremendous piece of full body acting from Emma Stone rather than just “looking serious and putting on an accent”.', 'What are you thinking abt rn? \n\nMy mind: https://t.co/twitter_link', 'I really just held the door open for some bitch who critized me for the way I did it. I should have drug her ass back on the other side of the door and told her fuck you.\n\nShe really said “mmm wow you do it the opposite way” like bitch I’m not your door man I’m being polite.', 'Done this shit two weeks in a row I’m burnt out already. Don’t see how yall still do this shit weekly', 'OK we have to beat Liverpool so we can have a chance at meeting Coventry', '"We were really shaky in the first quarter," - Popovich \n\nNuggets 117, Spurs 106: What they said after the game\nhttps://t.co/twitter_link #porvida #nba #sanantonio #gospursgo #milehighbasketball', "Martin opens the scoring on a wraparound three seconds after Kelly's penalty ended. Joseph and Korpisalo collided. However, it was unlikely he would've got over quick enough to stop Martin. 1-0 NYI @mention", 'Tyler Toffoli looks pretty happy after the fans went nuts following his goal.', 'Flat out, one of the best performances to ever.... EVER happen. \n\nPrince had to remind people just how damn GREAT he was on the guitar https://t.co/twitter_link', 'This is me https://t.co/twitter_link', 'She’s taking the stage soon and I need to get a good spot. Y’all have fun fighting', 'you know its crazy because Eric Collins didnt even react https://t.co/twitter_link', 'hello sunnytwt what have i missed the past few days'], 'sports, pop muisc')
#generate_metadata()
#generate_tweet_3(["she’s actually so cool but the comments are full of “oh ik she would’ve boycotted x” - while boycotting is good it’s not the end all and be all of activism that people should use to justify if someone is a good person or not https://t.co/twitter_link","Bread loaf gonna cost $10,000 \n\nI hate when illiterate people spend more time talking than reading \n\nHistorically the grand promise ppl make when they wanna rise to power is “debt forgiveness” \n\nMike Hudson has some Yt videos u can use as a starting point to find anecdotes https://t.co/twitter_link","He needs to take the hanger out his jacket before he puts it on \n\nIf u don’t address the business model underneath it all, this will transfer the cost back to customers bc companies hate losing profit \n\nThere’s other solutions like expand SBA that would empower workers https://t.co/twitter_link","Orlando brown was a child actor that had his life stolen for ur entertainment and y’all are making content of is mental issues shaming him \n\nDisgusting internet behavior needs to be blocked, muted, discouraged\n\nClean up ur acts and hold each other accountable u bitches", "“The last time these two played each other game went to 2 OTs and was decided by one point \n\nThats the definition of hoops you fuck\n\nIf you don’t like basketball other sports out there for your dumbass https://t.co/twitter_link"], "")
