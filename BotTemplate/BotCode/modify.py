import typo
import random

def swap(tweet):
    error1 = typo.StrErrer(tweet)
    return error1.nearby_char(preservefirst=True).result

def missing_char(tweet):
    error = typo.StrErrer(tweet)
    return error.missing_char(preservefirst=True).result

def introduce_errors(tweet):
    returntweet = tweet
    
    r = random.randint(1,15) #10 percent chance of error
    if (r == 1 or r==2):
        returntweet = swap(returntweet)
    
    x= random.randint(1,13) #10 percent chance of error
    if (x == 1 or x ==2):
        returntweet = missing_char(returntweet)

    z= random.randint(1,12) #50 percent chance of all lower
    if (z == 1 or z==2 or z==3):
        returntweet = returntweet.lower()

    return returntweet


def introduce_links(tweet):
    # 25% chance to append a link if it doesn't already exist
    if "https://t.co/twitter_link" not in tweet and random.randint(1, 4) == 1:
        return f"{tweet} https://t.co/twitter_link"
    return tweet


def introduce_mentions(tweet):
    returntweet = tweet
    
    r = random.randint(1,33)
    if (r == 1):
        returntweet = f"{tweet} @mention"
    elif (r == 2):
        returntweet = f"@mention {tweet}"

    return returntweet