from dotenv import load_dotenv
import os
from src.data_collection import DataCollection
from src.preprocessing import Preprocessing
from src.summarization import Summarization
from src.publishing import Publishing
import datetime

# Load environment variables from .env file
load_dotenv()

def main():
    # Get environment variables
    API_KEY = os.getenv('NEWS_API_KEY')
    WP_URL = os.getenv('WORDPRESS_URL')
    WP_USER = os.getenv('WORDPRESS_USERNAME')
    WP_PASSWORD = os.getenv('WORDPRESS_PASSWORD')
    UNSPLASH_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

    if not all([API_KEY, WP_URL, WP_USER, WP_PASSWORD, UNSPLASH_KEY]):
        print("Error: Missing environment variables.")
        return

    # 1. Collect News Articles
    collector = DataCollection(API_KEY)
    today = datetime.date.today()
    articles = collector.fetch_news("technology", from_date=today, to_date=today)

    # Check if articles were fetched successfully
    if articles is None:
        print("No articles were fetched. Exiting.")
        return

    # 2. Preprocess and Summarize Articles
    preprocessor = Preprocessing()
    summarizer = Summarization()
    
    summaries = []
    for article in articles:
        title = article['title']
        content = article['content']
        if content:
            cleaned_content = preprocessor.clean_text(content)
            summary = summarizer.summarize(cleaned_content)
            summaries.append({'title': title, 'summary': summary})

    # 3. Publish Summaries to WordPress
    publisher = Publishing(WP_URL, WP_USER, WP_PASSWORD)
    for summary in summaries:
        publisher.publish_post(summary['title'], summary['summary'])

if __name__ == "__main__":
    main()
