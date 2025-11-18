# Bot or Not: Human-Like Tweet Generation & Bot Evasion

This project explores how far large language models (LLMs) can be pushed to generate **highly human-like tweets** while **evading machine-learning–based bot detectors**.  
It examines prompt engineering, post-processing, and fine-tuning strategies to create a bot capable of passing as a real user in competitive detection environments.

---

## 🚀 Features

- **Human-like Tweet Generation**
  - Informal tone, slang, sentiment, and stylistic mimicry
  - JSON-structured inner monologue prompting
  - Dataset-aware stylistic adaptation

- **Bot Evasion**
  - Designed to reduce detection confidence across multiple ML detectors
  - Behavioral variation (links, mentions, typos, timestamps)

- **Evaluation Framework**
  - Tweet-level linguistic metrics (length, lexical diversity, TF-IDF, readability)
  - Detector-based bot performance graphs
  - Side-by-side human vs. bot comparisons

---

## 🧠 Technologies & Techniques

### **LLMs & NLP**
- **GPT-4o** for tweet generation and metadata synthesis  
- **Fine-Tuning** (OpenAI API) to internalize human tweet style  
- **Prompt Engineering**
  - Few-shot prompting
  - Inner monologue prompting
  - Structured JSON response schemas  
- **SpaCy** for linguistic feature extraction  
- **TF-IDF**, lexical diversity scoring, readability metrics

### **Post-Processing Pipeline**
- **Typo Library** for realistic spelling/grammar imperfections  
- Randomized:
  - Typos
  - Character drops
  - Case variation
  - Link & mention injection  
- Timestamp randomization per subsession

### **Data Processing**
- Python-based data prep and analysis  
- Content moderation pipeline (OpenAI Moderation API)  
- Training/validation dataset construction (JSONL)

---

## 📊 Results (Summary)

- Fine-tuned model evaded **100% of detectors** in the final session.
- Generated tweets displayed:
  - More expressive sentiment
  - Higher slang usage
  - Better stylistic alignment with human datasets
- Prompt-engineered models gradually degraded as detectors improved.
- Fine-tuned models showed limitations:
  - Topic bias (sports overrepresented)
  - Occasional hallucinations and fragmentation

---
