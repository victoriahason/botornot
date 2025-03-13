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
    
    r = random.randint(1,10) #10 percent chance of error
    if (r == 1):
        returntweet = swap(returntweet)
    
    x= random.randint(1,10) #10 percent chance of error
    if (x == 1):
        returntweet = missing_char(returntweet)

    z= random.randint(1,5) #20 percent chance of all lower
    if (z == 1):
        returntweet = returntweet.lower()

    return returntweet



