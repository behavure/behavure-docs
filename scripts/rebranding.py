#!/usr/bin/env python3
import re
import os
import argparse
from pathlib import Path
import shutil
from datetime import datetime

def get_new_filename(old_filename):
    """Convert a filename from Scuba to Measure IQ format."""
    # Don't modify non-markdown files
    if not old_filename.endswith('.md'):
        return old_filename
    
    # Replace variations of Scuba in filename
    new_name = old_filename
    replacements = [
        ('scuba', 'measure-iq'),
        ('Scuba', 'measure-iq'),
        ('SCUBA', 'measure-iq')
    ]
    
    for old, new in replacements:
        new_name = new_name.replace(old, new)
    
    return new_name

def should_use_an(next_word):
    """Determine if 'an' should be used based on the following word's pronunciation."""
    # List of words that start with consonants but are pronounced with vowel sounds
    vowel_sound_exceptions = {'hour', 'honest', 'honor'}
    
    # Convert to lowercase for checking
    word = next_word.lower()
    
    # Check if word starts with a vowel sound
    if word in vowel_sound_exceptions:
        return True
    
    return word[0] in 'aeiou'

def fix_article(match):
    """Fix 'a' vs 'an' based on what follows."""
    article = match.group(1)
    space = match.group(2)
    
    # If the next word starts with a vowel sound, use 'an'
    if should_use_an('Measure'):
        return 'an' + space
    return 'a' + space

def process_line(line):
    """Process a single line of text with grammar-aware replacements."""
    # Technical terms that should be preserved or handled specially
    technical_terms = {
        r"Scuba cluster": "Measure IQ cluster",
        r"Scuba metadata": "Measure IQ metadata",
        r"Scuba SQL": "Measure IQ SQL",
        r"Scuba Analytics": "Behavure AI",
        r"Scuba tutorial": "Measure IQ tutorial",
        r"Scuba guides": "Measure IQ guides",
        r"Scuba concepts": "Measure IQ concepts",
        r"Scuba deployment": "Measure IQ deployment",
        r"Scuba implementation": "Measure IQ implementation",
        r"Scuba representative": "Measure IQ representative",
        r"Scuba rep": "Measure IQ rep",
        r"Scuba team": "Measure IQ team",
        r"Scuba Admin": "Measure IQ Admin",
        r"Scuba application": "Measure IQ application",
        r"Scuba instance": "Measure IQ instance",
        r"Scuba Query Signals": "Measure IQ Query Signals",
        r"Scuba Signals": "Measure IQ Signals",
        r"Scuba's API": "Measure IQ's API",
        r"Scuba data": "Measure IQ data",
        r"Scuba table": "Measure IQ table",
        r"Scuba import": "Measure IQ import",
        r"Scuba ingest": "Measure IQ ingest",
        r"Scuba stack": "Measure IQ stack",
        r"Scuba UI": "Measure IQ UI",
        r"Scuba Help": "Measure IQ Help",
        r"Scuba database": "Measure IQ database",
        r"Scuba host": "Measure IQ host",
        r"Scuba cluster": "Measure IQ cluster",
        r"Scuba technical customer success manager": "Measure IQ technical customer success manager",
        r"Scuba TCSM": "Measure IQ TCSM",
        r"Scuba implementation team": "Measure IQ implementation team"
    }
    
    # Special phrases that need careful handling
    special_phrases = {
        r"How Scuba works": "How Measure IQ works",
        r"How Scuba Performs": "How Measure IQ Performs",
        r"How does Scuba perform": "How does Measure IQ perform",
        r"About Scuba Privacy": "About Measure IQ Privacy",
        r"Understanding Scuba": "Understanding Measure IQ",
        r"into Scuba": "into Measure IQ",
        r"in Scuba": "in Measure IQ",
        r"to Scuba": "to Measure IQ",
        r"from Scuba": "from Measure IQ",
        r"by Scuba": "by Measure IQ",
        r"with Scuba": "with Measure IQ",
        r"your Scuba": "your Measure IQ",
        r"the Scuba": "the Measure IQ",
        r"a Scuba": "a Measure IQ"
    }
    
    # Domain and email replacements
    domain_replacements = {
        r"@scuba\.io": "@behavure.ai",
        r"@measure-iq\.io": "@behavure.ai",
        r"support\.scuba\.io": "support.behavure.ai",
        r"support\.measure-iq\.io": "support.behavure.ai",
        r"help@scuba\.io": "help@behavure.ai",
        r"help@measure-iq\.io": "help@behavure.ai",
        r"scuba\.atlassian\.net": "behavure.ai/docs",
        r"interana\.atlassian\.net": "behavure.ai/docs",
        r"measure-iq\.io": "behavure.ai",
        r"scuba\.io": "behavure.ai",
        r"scuba\.engineering": "behavure.ai",
        r"yourcompany\.scuba\.io": "yourcompany.behavure.ai",
        r"my_cluster\.scuba\.io": "my_cluster.behavure.ai",
        r"test\.scuba\.engineering": "test.behavure.ai"
    }
    
    # Handle technical terms first (case-sensitive)
    for pattern, replacement in technical_terms.items():
        line = re.sub(r'\b' + pattern + r'\b', replacement, line)
    
    # Handle special phrases (case-insensitive)
    for pattern, replacement in special_phrases.items():
        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
    
    # Handle domain replacements
    for pattern, replacement in domain_replacements.items():
        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
    
    # Handle possessive forms
    line = re.sub(r"Scuba's|SCUBA's", "Measure IQ's", line)
    
    # Handle basic replacements, excluding special cases
    # Updated pattern to better catch standalone instances while preserving technical terms
    scuba_pattern = r"(?<![\w/])(?:Scuba|SCUBA)(?!\s*(?:Analytics|Query|Signals|Help|rep|Admin|metadata|cluster|application|UI|table|import|ingest|stack|data|instance|deployment|implementation|representative|team|tutorial|guides|concepts))"
    line = re.sub(scuba_pattern, "Measure IQ", line)
    
    # Fix articles (a/an) before "Measure IQ"
    line = re.sub(r'\b(a|an)(\s+)Measure IQ\b', fix_article, line)
    
    # Handle directory paths in markdown links
    line = re.sub(r'\]\(([^)]+)/scuba-([^)]+)\)', lambda m: f']({m.group(1)}/measure-iq-{m.group(2)})', line)
    line = re.sub(r'\]\(([^)]+)/scuba([^)]+)\)', lambda m: f']({m.group(1)}/measure-iq{m.group(2)})', line)
    
    return line

def update_internal_links(content, file_mapping):
    """Update internal links to reflect renamed files."""
    def replace_link(match):
        full_link = match.group(0)
        link_text = match.group(1)
        url = match.group(2)
        
        # Process the link text
        new_link_text = process_line(link_text)
        
        # Update internal links based on file mapping
        new_url = url
        for old_path, new_path in file_mapping.items():
            if old_path in url:
                new_url = url.replace(old_path, new_path)
                break
        
        # Handle directory paths in URLs
        new_url = re.sub(r'/scuba-([^)]+)', r'/measure-iq-\1', new_url)
        new_url = re.sub(r'/scuba([^)]+)', r'/measure-iq\1', new_url)
        
        return f"[{new_link_text}]({new_url})"
    
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)

def process_markdown_links(content):
    """Process markdown links separately to ensure proper handling."""
    def replace_in_link(match):
        full_link = match.group(0)
        link_text = match.group(1)
        url = match.group(2)
        
        # Process the link text
        new_link_text = process_line(link_text)
        
        # Process the URL
        new_url = url
        domain_replacements = {
            'scuba.io': 'behavure.ai',
            'measure-iq.io': 'behavure.ai',
            'scuba.atlassian.net': 'behavure.ai/docs',
            'interana.atlassian.net': 'behavure.ai/docs',
            'measure-iq.atlassian.net': 'behavure.ai/docs',
            'scuba.engineering': 'behavure.ai',
            'test.scuba.engineering': 'test.behavure.ai'
        }
        
        for old_domain, new_domain in domain_replacements.items():
            if old_domain in url:
                new_url = url.replace(old_domain, new_domain)
                break
        
        # Handle directory paths in URLs
        new_url = re.sub(r'/scuba-([^)]+)', r'/measure-iq-\1', new_url)
        new_url = re.sub(r'/scuba([^)]+)', r'/measure-iq\1', new_url)
        
        return f"[{new_link_text}]({new_url})"
    
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_in_link, content)

def process_yaml_frontmatter(frontmatter):
    """Process YAML frontmatter while preserving structure."""
    lines = frontmatter.split('\n')
    processed_lines = []
    
    for line in lines:
        # Only process values, not keys
        if ':' in line:
            key, value = line.split(':', 1)
            processed_value = process_line(value)
            processed_lines.append(f"{key}:{processed_value}")
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def build_file_mapping(docs_dir):
    """Build a mapping of old to new filenames."""
    file_mapping = {}
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if 'scuba' in file.lower() or 'SCUBA' in file:
                old_path = os.path.join(root, file)
                new_name = get_new_filename(file)
                new_path = os.path.join(root, new_name)
                rel_old_path = os.path.relpath(old_path, docs_dir)
                rel_new_path = os.path.relpath(new_path, docs_dir)
                file_mapping[rel_old_path] = rel_new_path
    return file_mapping

def process_file(file_path, dry_run=False, file_mapping=None):
    """Process a markdown file, including YAML frontmatter and links."""
    if not file_path.endswith('.md'):
        return
    
    print(f"Processing {file_path}")
    
    # Create backup if not dry run
    if not dry_run:
        backup_path = f"{file_path}.bak"
        shutil.copy2(file_path, backup_path)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into YAML frontmatter and main content
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = process_yaml_frontmatter(parts[1])
        main_content = parts[2]
        new_content = f"---{frontmatter}---{main_content}"
    else:
        new_content = content
    
    # Process markdown links first
    new_content = process_markdown_links(new_content)
    
    # Update internal links if file_mapping is provided
    if file_mapping:
        new_content = update_internal_links(new_content, file_mapping)
    
    # Process the remaining content
    scuba_pattern = r"(?<![\w/])(?:Scuba|SCUBA)(?!\s*(?:Analytics|Query|Signals|Help|rep|Admin|metadata|cluster|application|UI|table|import|ingest|stack|data|instance|deployment|implementation|representative|team|tutorial|guides|concepts))"
    new_content = re.sub(scuba_pattern, lambda m: process_line(m.group(0)), new_content)
    
    if dry_run:
        if new_content != content:
            print(f"\nChanges for {file_path}:")
            for old, new in zip(content.splitlines(), new_content.splitlines()):
                if old != new:
                    print(f"- {old}")
                    print(f"+ {new}\n")
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

def rename_files(docs_dir, file_mapping, dry_run=False):
    """Rename files according to the mapping."""
    for old_path, new_path in file_mapping.items():
        full_old_path = os.path.join(docs_dir, old_path)
        full_new_path = os.path.join(docs_dir, new_path)
        if dry_run:
            print(f"Would rename: {full_old_path} -> {full_new_path}")
        else:
            os.makedirs(os.path.dirname(full_new_path), exist_ok=True)
            shutil.move(full_old_path, full_new_path)
            print(f"Renamed: {full_old_path} -> {full_new_path}")

def cleanup_backups(directory):
    """Remove all .bak files in the directory tree."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md.bak'):
                backup_path = os.path.join(root, file)
                os.remove(backup_path)
                print(f"Removed backup file: {backup_path}")

def main():
    parser = argparse.ArgumentParser(description='Rebrand Scuba to Measure IQ in documentation')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying them')
    parser.add_argument('--restore', action='store_true', help='Restore from backup files')
    parser.add_argument('--cleanup', action='store_true', help='Remove all backup files')
    args = parser.parse_args()
    
    docs_dir = Path('src/content/docs')
    
    if args.cleanup:
        cleanup_backups(docs_dir)
        return
    
    if args.restore:
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md.bak'):
                    original = file[:-4]
                    backup_path = os.path.join(root, file)
                    original_path = os.path.join(root, original)
                    shutil.move(backup_path, original_path)
                    print(f"Restored {original_path} from backup")
        return
    
    # Build file mapping first
    file_mapping = build_file_mapping(docs_dir)
    
    if args.dry_run:
        print("\nFiles to be renamed:")
        for old, new in file_mapping.items():
            print(f"{old} -> {new}")
        print()
    
    # Process all files first
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path, args.dry_run, file_mapping)
    
    # Rename files after processing content
    if not args.dry_run:
        rename_files(docs_dir, file_mapping)
        cleanup_backups(docs_dir)

if __name__ == "__main__":
    main() 