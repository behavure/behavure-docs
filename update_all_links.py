#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Mapping of LEXICON page IDs to glossary terms
LEXICON_TO_GLOSSARY = {
    '1302233328': 'explore',  # Explore
    '1302233361': 'flow-property',  # flow property
    '1302233848': 'time-scrubber',  # time scrubber
    '1302266125': 'event-property',  # properties
    '1302266337': 'navigation-bar',  # pin
    '1302266661': 'user-roles',  # role definition
    '1302331425': 'journey-actor-user',  # actor
    '1302332083': 'trailing-window',  # trailing window
    '1302364771': 'query-builder',  # Query Builder
    '1302429994': 'distribution-view',  # Distribution View
    '1302430081': 'flow',  # flow, flows
    '1302430120': 'flow-instance',  # flow instance, flow instances
    '1302430148': 'pre-filters',  # Pre-Filters
    '1302430635': 'streaming-ingest',  # Streaming ingest
    '1302462471': 'journey-actor-user',  # actor property
    '1302462996': 'split-by',  # split-by
    '1302495656': 'method',  # method, methods
}

# Mapping of GLOSSARY page IDs to glossary terms
GLOSSARY_TO_GLOSSARY = {
    '2160230470': 'journey-actor-user',  # actor, actors
    '2160230498': 'journey-actor-user',  # actor properties
    '2160230841': 'cluster',  # cluster
    '2160231107': 'event',  # event
    '2160231142': 'event-property',  # calculation of a property
    '2160231259': 'flow',  # flow
    '2160231301': 'flow-property',  # flow property
    '2160231434': 'knowledge-object-knob',  # knob, knowledge objects
    '2160231516': 'merge-server',  # merge server
    '2160231530': 'method',  # method, methods
    '2160231796': 'pre-filters',  # pre-filter
    '2160232532': 'trailing-window',  # trailing window
}

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all LEXICON and GLOSSARY links
    lexicon_pattern = r'\[([^\]]+)\]\(https://scuba\.atlassian\.net/wiki/spaces/LEXICON/pages/(\d+)(?:/[^)\s]+)?(?:\+[^)]*)?\)'
    glossary_pattern = r'\[([^\]]+)\]\(https://scuba\.atlassian\.net/wiki/spaces/GLOSSARY/pages/(\d+)(?:/[^)\s]+)?(?:\+[^)]*)?\)'
    
    lexicon_matches = list(re.finditer(lexicon_pattern, content))
    glossary_matches = list(re.finditer(glossary_pattern, content))
    
    if not lexicon_matches and not glossary_matches:
        return False
    
    print(f"\nUpdating links in {file_path}")
    
    # Replace each match with the corresponding glossary link
    new_content = content
    
    # Update LEXICON links
    for match in lexicon_matches:
        term = match.group(1)
        page_id = match.group(2)
        if page_id in LEXICON_TO_GLOSSARY:
            old_link = match.group(0)
            new_link = f'[{term}](/measure_iq/glossary/{LEXICON_TO_GLOSSARY[page_id]})'
            print(f"  {old_link} -> {new_link}")
            new_content = new_content.replace(old_link, new_link)
        else:
            print(f"  Warning: No mapping found for LEXICON page ID {page_id} ({term})")
    
    # Update GLOSSARY links
    for match in glossary_matches:
        term = match.group(1)
        page_id = match.group(2)
        if page_id in GLOSSARY_TO_GLOSSARY:
            old_link = match.group(0)
            new_link = f'[{term}](/measure_iq/glossary/{GLOSSARY_TO_GLOSSARY[page_id]})'
            print(f"  {old_link} -> {new_link}")
            new_content = new_content.replace(old_link, new_link)
        else:
            print(f"  Warning: No mapping found for GLOSSARY page ID {page_id} ({term})")
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    docs_dir = Path('src/content/docs')
    files_updated = 0
    
    # Walk through all markdown files
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                if update_file(file_path):
                    files_updated += 1
    
    print(f"\nUpdated {files_updated} files")

if __name__ == '__main__':
    main() 