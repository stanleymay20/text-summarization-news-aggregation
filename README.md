# AI-Based News Summarization System

This project is an AI-based news summarization system that fetches news articles, summarizes them using state-of-the-art Natural Language Processing (NLP) techniques, and publishes the summaries to a WordPress blog. The system uses both extractive and abstractive summarization techniques powered by models like T5.

## Features

- Fetches news articles from NewsAPI
- Preprocesses the text (tokenization, stopwords removal, etc.)
- Generates concise summaries using a transformer-based model (T5)
- Automatically posts the summaries to a WordPress blog
- Runs daily at 08:00 UTC using GitHub Actions

## Technologies Used

- **Python** for data collection, processing, summarization, and automation
- **Hugging Face Transformers** for abstractive summarization with the T5 model
- **Requests** for fetching news from APIs
- **NLTK** for text preprocessing
- **WordPress REST API** for automated posting
- **GitHub Actions** for scheduling daily runs and automation
- **Vercel** for deployment

## Project Structure

```plaintext
text-summarization-news-aggregation/
├── src/
│   ├── data_collection.py       # Handles fetching news articles from APIs
│   ├── preprocessing.py         # Preprocesses text (tokenization, stopwords removal)
│   ├── summarization.py         # Abstractive summarization using T5
│   ├── evaluation.py            # Evaluates summaries (optional)
│   ├── publishing.py            # Posts summaries to WordPress via REST API
│   ├── main.py                  # Orchestrates the entire workflow
├── diagrams/
│   ├── architecture_diagram.png # High-level architecture of the system
│   ├── data_flow_diagram.png    # Data flow diagram of the system
├── report/
│   ├── main.tex                 # LaTeX report file
│   ├── references.bib           # BibTeX references
├── .github/
│   └── workflows/
│       └── deploy.yml           # GitHub Actions workflow for daily automation
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (DO NOT COMMIT)
└── .gitignore                   # Ignored files and directories
