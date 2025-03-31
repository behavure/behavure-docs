#!/usr/bin/env python3
"""
Script to fix broken relative links in the documentation.
This script parses the output of a link checking tool and applies fixes to the identified broken links.
"""

import os
import re
import argparse
from pathlib import Path

def parse_broken_links(input_file):
    """Parse the broken links file and extract link information."""
    broken_links = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        # Skip empty lines and non-link lines
        if not line.strip() or not '=>' in line:
            continue
        
        # Skip lines referencing behavure.ai wiki
        if 'behavure.ai/docs/wiki/spaces/' in line:
            continue
            
        # Skip https URLs that are likely external resources
        if '=>' in line and ('https://' in line.split('=>')[1] or 'http://' in line.split('=>')[1]):
            continue
        
        # Extract file path, line number, column number, and target
        match = re.match(r'(.+?)\s+\((\d+),\s+(\d+)\)\s+=>\s+(.+)', line.strip())
        if match:
            source_file, line_num, col_num, target = match.groups()
            broken_links.append({
                'source_file': source_file,
                'line': int(line_num),
                'column': int(col_num),
                'target': target.strip()
            })
    
    return broken_links

def fix_relative_path(source_file, target_path, docs_root):
    """Fix a relative path based on the source file and target."""
    # Skip external URLs and anchors
    if target_path.startswith(('http://', 'https://', 'mailto:')):
        return target_path
    
    # Handle special cases first
    if target_path.startswith('/measure_iq/'):
        # Absolute path within the docs, make it relative
        target_path = target_path[1:]  # Remove leading slash
        source_dir = os.path.dirname(source_file)
        source_rel_path = os.path.relpath(source_dir, docs_root)
        
        # Calculate the proper relative path prefix
        rel_prefix = '../' * (len(source_rel_path.split('/')) - 1) if source_rel_path != '.' else ''
        return f"{rel_prefix}{target_path}"
        
    # Handle glossary references
    if target_path.startswith('/measure_iq/glossary/'):
        target_filename = os.path.basename(target_path)
        return f"../../../glossary/{target_filename}"
    
    if target_path.startswith('../'):
        # It's already a relative path, let's validate it
        source_dir = os.path.dirname(source_file)
        target_abs = os.path.normpath(os.path.join(source_dir, target_path))
        
        # Check if the target exists
        if os.path.exists(os.path.join(docs_root, target_abs)):
            return target_path
        
        # Try to find the correct path
        target_filename = os.path.basename(target_path)
        for root, dirs, files in os.walk(docs_root):
            if target_filename in files:
                # Found a matching file
                target_full_path = os.path.join(root, target_filename)
                target_rel_to_docs = os.path.relpath(target_full_path, docs_root)
                source_rel_to_docs = os.path.relpath(source_dir, docs_root)
                new_rel_path = os.path.relpath(target_rel_to_docs, source_rel_to_docs)
                return new_rel_path
    
    # Handle paths like "measure_iq/something"
    if target_path.startswith('measure_iq/'):
        source_dir = os.path.dirname(source_file)
        source_rel_path = os.path.relpath(source_dir, docs_root)
        
        # Calculate the proper relative path prefix
        rel_prefix = '../' * (len(source_rel_path.split('/')) - 1) if source_rel_path != '.' else ''
        return f"{rel_prefix}{target_path}"
    
    # If it starts with ./ just remove that part as it's redundant
    if target_path.startswith('./'):
        return target_path[2:]
        
    # Fix attachments references
    if 'attachments/' in target_path:
        filename = os.path.basename(target_path)
        # Construct a proper path to the attachments folder relative to the source file
        source_dir = os.path.dirname(source_file)
        attachments_dir = os.path.join(source_dir, 'attachments')
        
        # Check if the attachments directory exists
        rel_attachments_path = os.path.relpath(attachments_dir, os.path.join(docs_root, source_dir))
        if os.path.isdir(os.path.join(docs_root, source_dir, 'attachments')):
            return f"./attachments/{filename}"
        else:
            # Try to find the nearest attachments directory
            source_parts = source_file.split('/')
            for i in range(len(source_parts)-1, 0, -1):
                test_path = '/'.join(source_parts[:i]) + '/attachments'
                if os.path.isdir(os.path.join(docs_root, test_path)):
                    parent_levels = len(source_parts) - i
                    return f"{'../' * parent_levels}attachments/{filename}"
            
    # Fix cross-section references (measure-guides, measure-tutorials, etc.)
    if 'measure-guides/' in target_path:
        # Replace with the correct section path
        return target_path.replace('measure-guides/', 'measure_iq/')
        
    # Fix references to the glossary
    if '../glossary/' in target_path or '../flow' in target_path:
        target_file = os.path.basename(target_path)
        return f"../../../glossary/{target_file}"
        
    # For other cases, return the original path
    return target_path

def update_file(file_path, line_num, column, target, new_target, dry_run=False):
    """Update a specific link in a file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if 0 <= line_num - 1 < len(lines):
        line = lines[line_num - 1]
        
        # Create a pattern that matches the target link
        # Escape special regex characters in the target
        escaped_target = re.escape(target)
        
        # Check if it's in a markdown link format
        md_match = re.search(r'\[.*?\]\(([^)]*)\)', line)
        if md_match and target in md_match.group(1):
            # It's in a markdown link, replace just the URL part
            old_link = md_match.group(1)
            new_link = old_link.replace(target, new_target)
            updated_line = line.replace(old_link, new_link)
        else:
            # Try to replace the exact target
            updated_line = line.replace(target, new_target)
        
        if updated_line != line:
            if dry_run:
                print(f"Would update {file_path}:{line_num} - {target} -> {new_target}")
            else:
                lines[line_num - 1] = updated_line
                with open(file_path, 'w') as f:
                    f.writelines(lines)
                print(f"Updated {file_path}:{line_num} - {target} -> {new_target}")
            return True
    
    print(f"Warning: Could not update {file_path}:{line_num} - {target}")
    return False

def get_common_replacements():
    """Return a dictionary of common replacements for broken links."""
    replacements = {
        # Fix common path patterns
        '../../../measure-guides/': '../../../measure_iq/',
        '../../measure-guides/': '../../measure_iq/',
        '../measure-guides/': '../measure_iq/',
        './measure-guides/': './measure_iq/',
        '/measure_iq/measure-guides/': '/measure_iq/',
        '/measure_iq/measure-tutorials/': '/measure_iq/measure-tutorials/',
        '../../../measure-guides/measure-user-guides/': '../../../measure_iq/measure-user-guides/',
        '../../../measure-guides/measure-tutorials/': '../../../measure_iq/measure-tutorials/',
        '../../../measure-guides/key-concepts-and-terminology/': '../../../measure_iq/key-concepts-and-terminology/',
        '/measure_iq/glossary/pre-filters': '../pre-filters',
        '/measure_iq/glossary/flow': '../flow',
        '/measure_iq/glossary/flow-instance': '../flow-instance',
        '/measure_iq/glossary/method': '../method',
        '/measure_iq/glossary/event': '../event',
        '/measure_iq/glossary/event-property': '../event-property',
    }
    return replacements

def apply_common_replacements(target_path):
    """Apply common replacements to the target path."""
    replacements = get_common_replacements()
    
    for old, new in replacements.items():
        if old in target_path:
            return target_path.replace(old, new)
            
    return target_path

def analyze_patterns(broken_links):
    """Analyze patterns in broken links to identify common issues."""
    patterns = {
        "starts_with": {},
        "contains": {},
        "extensions": {},
        "directories": {}
    }
    
    for link in broken_links:
        target = link['target']
        
        # Analyze start patterns
        first_part = target.split('/')[0] if '/' in target else target
        patterns["starts_with"][first_part] = patterns["starts_with"].get(first_part, 0) + 1
        
        # Analyze contained patterns
        for part in ['glossary', 'measure_iq', 'measure-guides', 'attachments', '../', './']:
            if part in target:
                patterns["contains"][part] = patterns["contains"].get(part, 0) + 1
        
        # Analyze file extensions
        if '.' in os.path.basename(target):
            ext = os.path.basename(target).split('.')[-1]
            patterns["extensions"][ext] = patterns["extensions"].get(ext, 0) + 1
        
        # Analyze directories
        if '/' in target:
            dirs = [d for d in target.split('/') if d]
            for d in dirs[:-1]:  # Skip the last item which might be a file
                patterns["directories"][d] = patterns["directories"].get(d, 0) + 1
    
    return patterns

def print_pattern_analysis(patterns):
    """Print the pattern analysis in a readable format."""
    print("\n--- Pattern Analysis ---")
    
    print("\nCommon Starting Patterns:")
    for pattern, count in sorted(patterns["starts_with"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {pattern}: {count}")
    
    print("\nCommon Contained Patterns:")
    for pattern, count in sorted(patterns["contains"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {pattern}: {count}")
    
    print("\nCommon File Extensions:")
    for ext, count in sorted(patterns["extensions"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  .{ext}: {count}")
    
    print("\nCommon Directories:")
    for directory, count in sorted(patterns["directories"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {directory}: {count}")
    
    print("\n--- End of Analysis ---\n")

def main():
    parser = argparse.ArgumentParser(description='Fix broken links in documentation')
    parser.add_argument('input_file', help='File containing the broken links report')
    parser.add_argument('docs_root', help='Root directory of the documentation')
    parser.add_argument('--dry-run', action='store_true', help='Print changes without making them')
    parser.add_argument('--output', help='Write fixed links to this file')
    parser.add_argument('--analyze', action='store_true', help='Analyze patterns in broken links')
    args = parser.parse_args()
    
    broken_links = parse_broken_links(args.input_file)
    print(f"Found {len(broken_links)} broken links to fix")
    
    # Run pattern analysis if requested
    if args.analyze:
        patterns = analyze_patterns(broken_links)
        print_pattern_analysis(patterns)
        
        # If only analysis was requested, exit
        if len(broken_links) > 0 and args.dry_run and not args.output:
            print("Analysis complete. Run without --analyze to fix links.")
            return
    
    fixed_count = 0
    skipped_count = 0
    
    if args.output:
        output_file = open(args.output, 'w')
        output_file.write("Source File,Line,Column,Original Target,New Target,Status\n")
    
    for link in broken_links:
        source_path = os.path.join(args.docs_root, link['source_file'])
        if not os.path.isfile(source_path):
            print(f"Warning: Source file not found: {source_path}")
            skipped_count += 1
            continue
        
        # First try common replacements
        new_target = apply_common_replacements(link['target'])
        
        # If no common replacement worked, try the more complex logic
        if new_target == link['target']:
            new_target = fix_relative_path(link['source_file'], link['target'], args.docs_root)
        
        status = "UNCHANGED"
        if new_target != link['target']:
            success = update_file(source_path, link['line'], link['column'], link['target'], new_target, args.dry_run)
            if success:
                fixed_count += 1
                status = "FIXED"
            else:
                skipped_count += 1
                status = "FAILED"
        else:
            print(f"No change needed for {link['source_file']}:{link['line']} - {link['target']}")
            skipped_count += 1
        
        if args.output:
            output_file.write(f"{link['source_file']},{link['line']},{link['column']},\"{link['target']}\",\"{new_target}\",{status}\n")
    
    print(f"Summary: {fixed_count} links fixed, {skipped_count} links skipped")
    
    if args.output:
        output_file.close()
        print(f"Results written to {args.output}")

if __name__ == '__main__':
    main()
