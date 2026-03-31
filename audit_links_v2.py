import os
import re
from collections import defaultdict

def get_all_files(root_dir):
    all_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            name = file # full name with extension for assets
            path = os.path.join(root, file)
            all_files[name] = path
            # Also store name without extension for md files
            if file.endswith(".md"):
                name_no_ext = os.path.splitext(file)[0]
                all_files[name_no_ext] = path
    return all_files

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Wiki-links: [[Link Name]] or [[Link Name|Display Name]]
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    return links, content

def audit(vault_root):
    all_files = get_all_files(vault_root)
    md_files = {k: v for k, v in all_files.items() if v.endswith(".md") and not k.endswith(".md")}
    
    file_names = set(all_files.keys())
    
    outgoing_links = defaultdict(list)
    incoming_links = defaultdict(list)
    broken_md_links = defaultdict(list)
    broken_asset_links = defaultdict(list)
    word_counts = {}
    
    for name, path in md_files.items():
        links, content = extract_links(path)
        word_counts[name] = len(content.split())
        for link in links:
            outgoing_links[name].append(link)
            if link in file_names:
                incoming_links[link].append(name)
            else:
                if any(link.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.drawio']):
                    broken_asset_links[name].append(link)
                else:
                    broken_md_links[name].append(link)
                
    orphans = [name for name in md_files if not incoming_links[name] and "MOC" not in name]
    
    print("--- BROKEN INTERNAL LINKS (.md) ---")
    for source, targets in broken_md_links.items():
        for target in targets:
            print(f"{source} -> [[{target}]]")
            
    print("\n--- BROKEN ASSET LINKS (Images, etc.) ---")
    for source, targets in broken_asset_links.items():
        for target in targets:
            print(f"{source} -> [[{target}]]")
            
    print("\n--- ORPHANED NOTES ---")
    for orphan in sorted(orphans):
        print(f"{orphan} ({md_files[orphan]})")
        
    print("\n--- THIN PERMANENT NOTES (< 100 words) ---")
    perm_dir = "Permanent Notes"
    for name, path in md_files.items():
        if perm_dir in path and word_counts[name] < 100:
            print(f"{name}: {word_counts[name]} words")

    # Potential Missing Permanent Notes (Simplified)
    # Count occurrences of words in Literature Notes that are not yet Permanent Notes
    # This is very noisy, so I'll just look for multi-word phrases or specific interesting terms
    print("\n--- RECURRING TERMS (Potential Permanent Notes) ---")
    interesting_terms = ["Growth Mindset", "Resiliensi Akademik", "Culture Shock", "Classical Conditioning", "Pengondisian Klasik", "Big Five", "Neurosis", "Object Relations", "Anima", "Animus", "Shadow"]
    term_counts = defaultdict(int)
    for name, path in md_files.items():
        if "Literature Notes" in path:
            _, content = extract_links(path)
            for term in interesting_terms:
                if term.lower() in content.lower():
                    term_counts[term] += 1
    
    for term, count in sorted(term_counts.items(), key=lambda x: x[1], reverse=True):
        if term not in md_files:
            print(f"{term}: {count} occurrences")

if __name__ == "__main__":
    # The root is College 101, but assets are in Assets/ and notes in Zettelkasten/
    # So I should run it from College 101 or pass College 101 as root.
    audit("College 101")
