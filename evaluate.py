###THIS SCRIPT IS AI GENERATED###

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import numpy as np
import language_tool_python
from spellchecker import SpellChecker
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import string
import spacy

def calculate_perplexity(model, tokenizer, text):
    """Calculate the perplexity of a given text."""
    encodings = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    input_ids = encodings.input_ids

    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss
        perplexity = torch.exp(loss)
    
    return perplexity.item()

# Load a pretrained language model (e.g., GPT-2)
#model_name = "gpt-4o-mini"
#model = AutoModelForCausalLM.from_pretrained(model_name)
#tokenizer = AutoTokenizer.from_pretrained(model_name)

def evaluate_perplexity(tweets):
    """Evaluate the average perplexity of a list of tweets."""
    perplexities = [calculate_perplexity(model, tokenizer, tweet) for tweet in tweets]
    return np.mean(perplexities)

def detect_grammar_errors(tweets):
    """Detect grammar errors using LanguageTool."""
    tool = language_tool_python.LanguageTool('en-US')
    errors = [len(tool.check(tweet)) for tweet in tweets]
    return np.mean(errors)

def calculate_typo_rate(tweets):
    """Calculate the typo rate by detecting non-dictionary words."""
    spell = SpellChecker()
    typo_counts = []
    
    for tweet in tweets:
        words = tweet.split()
        misspelled = spell.unknown(words)
        typo_counts.append(len(misspelled) / max(1, len(words)))  # Avoid division by zero
    
    return np.mean(typo_counts)

def compute_embedding_distance(real_tweets, generated_tweets):
    """Compute cosine distance between real and generated tweet embeddings."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    real_embeddings = model.encode(real_tweets, convert_to_tensor=True)
    generated_embeddings = model.encode(generated_tweets, convert_to_tensor=True)
    
    distances = [cosine(real_embeddings[i], generated_embeddings[i]) for i in range(min(len(real_tweets), len(generated_tweets)))]
    return np.mean(distances)

def compute_punctuation_density(tweets):
    """Compute the punctuation density as a ratio of punctuation marks to characters."""
    densities = []
    for tweet in tweets:
        punctuation_count = sum(1 for char in tweet if char in string.punctuation)
        total_chars = len(tweet)
        densities.append(punctuation_count / max(1, total_chars))  # Avoid division by zero
    return np.mean(densities)

def detect_sentence_fragments(tweets):
    ##Detect sentence fragments using spaCy.
    nlp = spacy.load("en_core_web_sm")
    fragment_counts = []
    
    #note: tweets with a root are tweets that have a main verb in them. Any sentance without that is most likely a fragment.
    for tweet in tweets:
        doc = nlp(tweet)
        full_sentences = sum(1 for sent in doc.sents if any(token.dep_ == "ROOT" for token in sent))
        total_sentences = len(list(doc.sents))
        fragment_ratio = 1 - (full_sentences / max(1, total_sentences))  # Proportion of sentence fragments
        fragment_counts.append(fragment_ratio)
    
    return np.mean(fragment_counts)

if __name__ == "__main__":
    # Example tweets (replace with actual datasets)
    real_tweets = ["This is a real tweet!", "Can't believe this happened..."]
    generated_tweets = ["This is an AI-generated tweet.", "The event was truly remarkable and unbelievable."]
    
    #real_perplexity = evaluate_perplexity(real_tweets)
    #generated_perplexity = evaluate_perplexity(generated_tweets)
    
    real_grammar_errors = detect_grammar_errors(real_tweets)
    generated_grammar_errors = detect_grammar_errors(generated_tweets)
    
    real_typo_rate = calculate_typo_rate(real_tweets)
    generated_typo_rate = calculate_typo_rate(generated_tweets)
    
    embedding_distance = compute_embedding_distance(real_tweets, generated_tweets)
    
    real_punctuation_density = compute_punctuation_density(real_tweets)
    generated_punctuation_density = compute_punctuation_density(generated_tweets)
    
    real_fragment_ratio = detect_sentence_fragments(real_tweets)
    generated_fragment_ratio = detect_sentence_fragments(generated_tweets)
    
    print(f"Average Perplexity - Real Tweets: {real_perplexity}")
    print(f"Average Perplexity - Generated Tweets: {generated_perplexity}")
    print(f"Average Grammar Errors - Real Tweets: {real_grammar_errors}")
    print(f"Average Grammar Errors - Generated Tweets: {generated_grammar_errors}")
    print(f"Average Typo Rate - Real Tweets: {real_typo_rate}")
    print(f"Average Typo Rate - Generated Tweets: {generated_typo_rate}")
    print(f"Average Embedding Distance - Real vs. Generated: {embedding_distance}")
    print(f"Average Punctuation Density - Real Tweets: {real_punctuation_density}")
    print(f"Average Punctuation Density - Generated Tweets: {generated_punctuation_density}")
    print(f"Average Sentence Fragment Ratio - Real Tweets: {real_fragment_ratio}")
    print(f"Average Sentence Fragment Ratio - Generated Tweets: {generated_fragment_ratio}")
