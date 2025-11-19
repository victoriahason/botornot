import json
import random
import csv

f''' this is convoluded lol.

Basically, by the end you have 2 csvs:

annotations.csv --> a csv of the generated tweets and the real tweets, randomly mixed

real_tweets.csv --> a csv of the real tweets, in order to find whether the annotations were correct

generated tweets are in tweets.json

BEFORE RUNNING: need subsession tweets and tweets, also delete annotations.csv

'''



def main():
    #parser = argparse.ArgumentParser(description="get 50 tweets")
    #parser.add_argument("-i", "--input_file", required=True, help="input dataset")

    #args = parser.parse_args()

    fields = ['tweet', 'annotation']
    
    with open('subsession_tweets.json', 'r') as f:
        real_tweets = json.load(f)

    with open('generated_tweets.json', 'r') as f:
        x = json.load(f)
    
    gpt_tweets = x['tweets']

    post_list_2=[]
    for t in gpt_tweets:
        post_list_2.append([t, ''])


    num_samples = 30
    #B FOR BOT, N FOR NOT
    post_list = [[repr(post["text"]),''] for post in random.sample(real_tweets, num_samples)]

    with open("real_tweets.csv", 'w') as f: 
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(post_list)

    
    for post in post_list_2:
         post_list.append(post)

    random.shuffle(post_list)

    with open("annotations.csv", 'w') as f: 
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(post_list)

if __name__ == "__main__":
    main()