from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("ENV_VAR1"))


messages_metadata = [
      {
        "role": "developer",  
        "content": "You are a helpful assistant that generates realistic twitter user metadata"
    },

    {
        "role": "user",
        "content": "Generate user metadata in a similar format to the following dataset:"
    }
]


def generate_tweets(examples):

    messages_tweets = [
    {
        "role": "developer",  
        "content": "You are a helpful assistant that generates a list dataset of realistic tweets. No links, use ‘https://t.co/twitter link’ instead. No mentions, use ‘@mention’ instead."
    },

    {
        "role": "user",
        "content": f"Generate 50 blurbs in the same format to the following dataset:{examples}. Do not write anyhing else. Seperate the tweets with a comma only. Use the language and topics of the provided data to generate your burbs."
    }
]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_tweets
    )
    return(response.choices[0].message)

""" def generate_metadata():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages_metadata
    )
    print(response["choices"][0]["message"]["content"]) 
"""

#generate_tweets(['Oh Jesus I never thought I’d agree with WTF James Charles has to say but here we are https://t.co/twitter_link', 'NHL Play: \n\nSabres Red Wings Over 6 - 120\n\nMoving', 'Jesus on the Radio.', 'Would it be easier to build from earth to space or from space down to earth. If there is no gravity in space could you technically build down. I wonder where "gravity" would start to  pull the structure down, or is zero gravity stronger then gravity. #questions #science #earth', '“I’ll love.\n\nEven for that first time.\n\nAnd you  for any of our last times …\n\n+ I took from you and I…\n\nYou quit.\n\nAnd I understand why”\n\nLove you beautiful woman!\n\nAlways will.', 'K IS SO FUNNY IM CRYING', 'BREAKING NEWS : Justin fields will be traded to the Steelers tomorrow noon 🕛 you heard first \n\n#CTESPN', 'Watching Poor Things. This is an absolutely tremendous piece of full body acting from Emma Stone rather than just “looking serious and putting on an accent”.', 'What are you thinking abt rn? \n\nMy mind: https://t.co/twitter_link', 'I really just held the door open for some bitch who critized me for the way I did it. I should have drug her ass back on the other side of the door and told her fuck you.\n\nShe really said “mmm wow you do it the opposite way” like bitch I’m not your door man I’m being polite.', 'Done this shit two weeks in a row I’m burnt out already. Don’t see how yall still do this shit weekly', 'OK we have to beat Liverpool so we can have a chance at meeting Coventry', '"We were really shaky in the first quarter," - Popovich \n\nNuggets 117, Spurs 106: What they said after the game\nhttps://t.co/twitter_link #porvida #nba #sanantonio #gospursgo #milehighbasketball', "Martin opens the scoring on a wraparound three seconds after Kelly's penalty ended. Joseph and Korpisalo collided. However, it was unlikely he would've got over quick enough to stop Martin. 1-0 NYI @mention", 'Tyler Toffoli looks pretty happy after the fans went nuts following his goal.', 'Flat out, one of the best performances to ever.... EVER happen. \n\nPrince had to remind people just how damn GREAT he was on the guitar https://t.co/twitter_link', 'This is me https://t.co/twitter_link', 'She’s taking the stage soon and I need to get a good spot. Y’all have fun fighting', 'you know its crazy because Eric Collins didnt even react https://t.co/twitter_link', 'hello sunnytwt what have i missed the past few days'])