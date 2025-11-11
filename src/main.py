import argparse
import sys

from scraper import scrape_article
from search import semantic_search


def run_find(query, limit):
    print(f"Performing semantic search for: '{query}'\n")
    results = semantic_search(query, n_results=limit)
    if not results:
        print("No results found.")
        return
    for index, ids in enumerate(results["ids"][0]):
        metadatas = results["metadatas"][0][index]
        documents = results["documents"][0][index]
        url = metadatas["url"]
        topics = metadatas["topics"]
        summary = metadatas["summary"]
        print(f"URL: {url}")
        print(f"Topics: {topics}")
        print(f"Summary: {summary}")
        print("-----")


def run_load(urls):
    scrape_article(urls)
    pass


def main():
    parser = argparse.ArgumentParser(
        description="News scraping and semantic search CLI"
    )
    subparsers = parser.add_subparsers(dest='command')

    # Sub-command for loading articles
    load_parser = subparsers.add_parser('load', help='Load one or more news articles from URLs')
    load_parser.add_argument(
        'urls',
        nargs='+',
        type=str,
        help='One or more news article URLs (separated by space)'
    )

    # Sub-command for semantic search, now with --limit option
    find_parser = subparsers.add_parser('find', help='Semantic search over the articles')
    find_parser.add_argument('query', type=str, help='Search query')
    find_parser.add_argument('--limit', type=int, default=5, help='Number of top results to return (default: 5)')

    args = parser.parse_args()

    if args.command == 'load':
        run_load(args.urls)
    elif args.command == 'find':
        run_find(args.query, args.limit)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
