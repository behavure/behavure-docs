#!/usr/bin/env python3

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_glossary_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all GLOSSARY links and their context
    pattern = r'\[([^\]]+)\]\(https://scuba\.atlassian\.net/wiki/spaces/GLOSSARY/pages/(\d+)/([^)\s]+)(?:\+[^)]*)?\)'
    matches = list(re.finditer(pattern, content))
    
    if matches:
        print(f"\nFound {len(matches)} matches in {file_path}")
        for match in matches:
            print(f"  Term: {match.group(1)}, Page ID: {match.group(2)}, Path: {match.group(3)}")
    
    mappings = defaultdict(set)
    for match in matches:
        term = match.group(1)
        page_id = match.group(2)
        path = match.group(3)
        # Store both the linked text and the path part
        mappings[page_id].add((term, path))
    
    return mappings

def main():
    docs_dir = Path('src/content/docs')
    all_mappings = defaultdict(set)
    
    # Walk through all markdown files
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                mappings = extract_glossary_links(file_path)
                for page_id, terms in mappings.items():
                    all_mappings[page_id].update(terms)
    
    # Print the mappings in a format suitable for the update script
    print("\nFinal mappings:")
    print("GLOSSARY_TO_GLOSSARY = {")
    for page_id, terms in sorted(all_mappings.items()):
        # Group all terms for this page ID
        terms_list = sorted(terms)
        # Use the path part if available, otherwise use the cleaned term
        glossary_term = terms_list[0][1].lower().replace('+', '-')  # Use the first path we found
        print(f"    '{page_id}': '{glossary_term}',  # Terms: {', '.join(t[0] for t in terms_list)}")
    print("}")

if __name__ == '__main__':
    main() 