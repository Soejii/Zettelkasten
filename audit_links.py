import os
import re
from collections import defaultdict

def get_files(root_dir):
    md_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                name = os.path.splitext(file)[0]
                path = os.path.join(root, file)
                md_files[name] = path
    return md_files

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Wiki-links: [[Link Name]] or [[Link Name|Display Name]]
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    return links, content

def audit(root_dir):
    md_files = get_files(root_dir)
    file_names = set(md_files.keys())
    
    outgoing_links = defaultdict(list)
    incoming_links = defaultdict(list)
    broken_links = defaultdict(list)
    word_counts = {}
    
    for name, path in md_files.items():
        links, content = extract_links(path)
        word_counts[name] = len(content.split())
        for link in links:
            outgoing_links[name].append(link)
            if link in file_names:
                incoming_links[link].append(name)
            else:
                broken_links[name].append(link)
                
    orphans = [name for name in file_names if not incoming_links[name] and "MOC" not in name]
    
    print("--- BROKEN LINKS ---")
    for source, targets in broken_links.items():
        for target in targets:
            print(f"{source} -> [[{target}]] (NOT FOUND)")
            
    print("\n--- ORPHANED NOTES (No incoming links, excluding MOCs) ---")
    for orphan in sorted(orphans):
        print(f"{orphan} ({md_files[orphan]})")
        
    print("\n--- THIN PERMANENT NOTES (< 100 words) ---")
    perm_dir = os.path.join(root_dir, "Permanent Notes")
    for name, path in md_files.items():
        if perm_dir in path and word_counts[name] < 100:
            print(f"{name}: {word_counts[name]} words")

if __name__ == "__main__":
    audit("College 101/Zettelkasten")
