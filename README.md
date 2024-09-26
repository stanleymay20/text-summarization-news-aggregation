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
88text-summarization-news-aggregation/
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

```

### Setup Instructions
**1. Clone the Repository**
```bash
git clone https://github.com/stanleymay20/text-summarization-news-aggregation.git
cd text-summarization-news-aggregation
```
**2. Install Dependencies**
```bash
pip install -r requirements.txt
```
**3. Set Environment Variables**
Create a .env file in the root directory and add the following environment variables:
```ini
NEWS_API_KEY=your_news_api_key_here
WORDPRESS_URL=your_wordpress_url_here
WORDPRESS_USERNAME=your_wordpress_username_here
WORDPRESS_PASSWORD=your_wordpress_password_here
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
```
**4. Run the Script**
```python src/main.py
```
This will fetch news, generate summaries, and publish them to WordPress.

### Automation with GitHub Actions
This project uses GitHub Actions to run daily at 08:00 UTC. The workflow is defined in .github/workflows/deploy.yml.

### Setting Up GitHub Secrets
Add the following secrets in your GitHub repository's Settings > Secrets and variables > Actions:
```
NEWS_API_KEY
WORDPRESS_URL
WORDPRESS_USERNAME
WORDPRESS_PASSWORD
UNSPLASH_ACCESS_KEY
```
GitHub Actions will use these secrets to automate the summarization process daily.

### Deployment on Vercel
To deploy this project on Vercel:

1. Connect your GitHub repository to Vercel.
2. Set the environment variables in Project Settings > Environment Variables.
3. Vercel will automatically build and deploy the project.

### Diagrams
![freecompress-Copy of Data Flow Diagram for News Summarizer Application](https://github.com/user-attachments/assets/6ac5777b-718d-4f17-9acd-0c3e7ad736cc)
![Copy of Data Flow Diagram for News Summarizer Application (1)](https://github.com/user-attachments/assets/664a5ea5-7703-44d7-84c5-e0ee603ee386)
![Copy of Copy of Architecture Diagram for News Summarizer](https://github.com/user-attachments/assets/7c41a494-4059-49ce-a278-dd7a07cbb518)
