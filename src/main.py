import argparse
import sys

from scraper import scrape_article
from search import semantic_search


def run_scrape_article(url):
    scrape_article([url])


def run_semantic_search(query, collection_name="news_articles", top_k=5):
    print(f"Performing semantic search for: '{query}'\n")
    results = semantic_search(query)
    if not results:
        print("No results found.")
        return

    for doc in zip(results["documents"][0]):
        print(f"Document: {doc}")
        print("-----")


def main():
    parser = argparse.ArgumentParser(
        description="News scraping and semantic search CLI"
    )
    subparsers = parser.add_subparsers(dest='command')

    # Sub-command for scraping
    scrape_parser = subparsers.add_parser('scrape', help='Scrape a news article from URL')
    scrape_parser.add_argument('url', type=str, help='News article URL')

    # Sub-command for semantic search
    search_parser = subparsers.add_parser('search', help='Semantic search over the articles')
    search_parser.add_argument('query', type=str, help='Search query')

    args = parser.parse_args()

    if args.command == 'scrape':
        run_scrape_article(args.url)
    elif args.command == 'search':
        run_semantic_search(args.query)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
