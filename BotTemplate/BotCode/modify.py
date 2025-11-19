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



