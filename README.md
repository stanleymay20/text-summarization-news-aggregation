# AI-Based News Summarization System

> **Canonical academic successor / not production-verified.** This is the structured successor to the earlier [`news-summarizer`](https://github.com/stanleymay20/news-summarizer) prototype. See [LINEAGE.md](LINEAGE.md) for the controlled family decision and the experimental capabilities intentionally preserved in the predecessor.

This project is a modular Python news-summarization pipeline that fetches articles from NewsAPI, preprocesses article text, generates abstractive summaries with T5, and can publish summaries to WordPress.

## Current Status

**Portfolio status:** CANONICAL ACADEMIC SUCCESSOR / LINEAGE RESOLVED / NOT PRODUCTION-VERIFIED.

The current default-branch source implements the modular NewsAPI → preprocessing → T5 → WordPress path. It should not yet be described as a live scheduled production service.

Important boundaries:

- current `src/summarization.py` implements **abstractive T5 summarization**, not the predecessor's TF-IDF extractive summarizer;
- the older prototype preserves unique Reuters scraping, extractive summarization, and Flask trigger experiments;
- `UNSPLASH_ACCESS_KEY` is checked by `src/main.py`, but no image-fetching implementation is present in the current `src/` path;
- the workflow reference currently lives at `github/workflows/deploy.yml`, not `.github/workflows/deploy.yml`, so it is **not active GitHub Actions automation**;
- that historical workflow reference also pushes to `master`, while the repository default branch is `main`.

External publishing/scheduling should not be activated until the workflow, credentials model, dependency baseline and WordPress side effects are deliberately reviewed.

## Features Implemented in the Current Modular Source

- Fetches news articles from NewsAPI.
- Preprocesses article text.
- Generates concise abstractive summaries with T5.
- Publishes summaries to WordPress through the publishing module.
- Includes an evaluation scaffold plus academic report/diagram artifacts.

## Technologies Used

- **Python** for collection, processing and orchestration.
- **Hugging Face Transformers** for T5 abstractive summarization.
- **Requests** for NewsAPI and WordPress HTTP calls.
- **NLTK** for preprocessing support.
- **WordPress REST-style HTTP publishing** through `requests.post`.

## Project Structure

```plaintext
text-summarization-news-aggregation/
├── src/
│   ├── data_collection.py       # NewsAPI ingestion
│   ├── preprocessing.py         # Text preprocessing
│   ├── summarization.py         # T5 abstractive summarization
│   ├── evaluation.py            # Evaluation scaffold
│   ├── publishing.py            # WordPress publishing
│   └── main.py                  # Workflow orchestration
├── diagrams/                    # Architecture/data-flow evidence
├── report/
│   ├── main.tex                 # Academic report
│   └── references.bib           # References
├── github/workflows/deploy.yml  # Historical/inactive workflow reference
├── LINEAGE.md                   # Project-family lineage decision
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/stanleymay20/text-summarization-news-aggregation.git
cd text-summarization-news-aggregation
```

### 2. Create a fresh environment and install dependencies

```bash
python -m venv .venv
pip install -r requirements.txt
```

### 3. Configure environment variables

Use a local `.env` file only for development and never commit real credentials.

```ini
NEWS_API_KEY=your_news_api_key_here
WORDPRESS_URL=your_wordpress_url_here
WORDPRESS_USERNAME=your_wordpress_username_here
WORDPRESS_PASSWORD=your_wordpress_password_here
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
```

`UNSPLASH_ACCESS_KEY` is currently required by `src/main.py` even though image fetching is not implemented. That requirement should be removed or a deliberate image module should be implemented before production hardening.

### 4. Run manually

```bash
python src/main.py
```

**Warning:** the current script can publish to the configured WordPress endpoint. Use development/test credentials when reproducing the project.

## Automation

There is **no active GitHub Actions workflow on the current default branch**. `github/workflows/deploy.yml` is retained as historical workflow evidence only. It must be reviewed and deliberately migrated to `.github/workflows/` before automation is enabled.

## Project Lineage

The predecessor `news-summarizer` ended active development on 2024-09-18. This structured repository began on 2024-09-26. The predecessor remains valuable historical evidence because some experiments were not carried forward. See [LINEAGE.md](LINEAGE.md).

## Diagrams

![freecompress-Copy of Data Flow Diagram for News Summarizer Application](https://github.com/user-attachments/assets/6ac5777b-718d-4f17-9acd-0c3e7ad736cc)
![Copy of Data Flow Diagram for News Summarizer Application (1)](https://github.com/user-attachments/assets/664a5ea5-7703-44d7-84c5-e0ee603ee386)
![Copy of Copy of Architecture Diagram for News Summarizer](https://github.com/user-attachments/assets/7c41a494-4059-49ce-a278-dd7a07cbb518)
