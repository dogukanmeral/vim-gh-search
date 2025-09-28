#!/usr/bin/python3

import argparse
from urllib.parse import quote
import webbrowser

def main(external_args = ''):
    parser = argparse.ArgumentParser(prog="Gh-search", description="Search code parts in GitHub")

    parser.add_argument('text', help="Code part to search",nargs='+' , type=str)
    parser.add_argument('--user', help="Filter by user", type=str)
    parser.add_argument('--org', help="Filter by organization", type=str)
    parser.add_argument('--repo', help="Filter by repository", type=str)
    parser.add_argument('--lang', help="Filter by language", type=str)
    parser.add_argument('--path', help="Filter by path", type=str)
    parser.add_argument('--symbol', help="Filter by symbol", type=str)

    parser.add_argument('--archived', help="Search in archived repositories", action="store_true")
    parser.add_argument('--vendored', help="Search in vendored repositories", action="store_true")
    parser.add_argument('--generated', help="Search in generated repositories", action="store_true")

    if external_args == '':
        args = parser.parse_args()
    else:
        args = parser.parse_args(external_args.split()) 

    base_url = 'https://github.com/search?type=code&q='

    query_elements = []

    if args.text:
        merged_text = ' '.join(args.text)
        query_elements.append(merged_text)
    if args.user:
        query_elements.append(f"user:{args.user}")
    if args.org:
        query_elements.append(f"org:{args.org}")
    if args.repo:
        query_elements.append(f"repo:{args.repo}")
    if args.lang:
        query_elements.append(f"language:{args.lang}")
    if args.path:
        query_elements.append(f"path:{args.path}")
    if args.symbol:
        query_elements.append(f"symbol:{args.symbol}")

    if args.archived:
        query_elements.append(f"is:archived")
    if args.vendored:
        query_elements.append(f"is:vendored")
    if args.generated:
        query_elements.append(f"is:generated")

    search_url = base_url + quote(' '.join(query_elements))
    webbrowser.open(search_url)

if __name__ == '__main__':
    main()
