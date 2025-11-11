import argparse
import sys

from scraper import scrape_article
from search import semantic_search

COLLECTION_NAME = "news_articles"
TOP_K = 5

def run_load_articles(urls):
        article = scrape_article(urls)

def run_find(query):
    print(f"Performing semantic search for: '{query}'\n")
    results = semantic_search(query)
    if not results:
        print("No results found.")
        return
    for doc in results["documents"]:
        print(f"Document: {doc}")
        print("-----")

def main():
    parser = argparse.ArgumentParser(
        description="News scraping and semantic search CLI"
    )
    subparsers = parser.add_subparsers(dest='command')

    # Sub-command for loading articles (accept one or more URLs)
    load_parser = subparsers.add_parser('load', help='Load one or more news articles from URLs')
    load_parser.add_argument(
        'urls',
        nargs='+',
        type=str,
        help='One or more news article URLs (separated by space)'
    )

    # Sub-command for find (semantic search)
    find_parser = subparsers.add_parser('find', help='Find articles by semantic search')
    find_parser.add_argument('query', type=str, help='Search query')

    args = parser.parse_args()

    if args.command == 'load':
        run_load_articles(args.urls)
    elif args.command == 'find':
        run_find(args.query)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
