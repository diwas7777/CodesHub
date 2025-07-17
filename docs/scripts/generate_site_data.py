#!/usr/bin/env python3
import os
import json
import subprocess
from datetime import datetime
from collections import defaultdict

def get_git_history():
    """Get real Git commit history for recent activity"""
    try:
        cmd = ['git', 'log', '--pretty=format:%an|%s|%cd', '--date=short', '-n', '5']
        result = subprocess.run(cmd, capture_output=True, text=True)
        activity = []
        
        for line in result.stdout.split('\n'):
            if not line.strip():
                continue
            try:
                author, message, date = line.split('|', 2)
                activity.append({
                    "author": author,
                    "message": message,
                    "date": date
                })
            except ValueError:
                continue
        
        return activity
    except Exception as e:
        print(f"Error getting Git history: {e}")
        # Fallback to mock data
        return get_mock_activity()

def get_mock_activity():
    """Fallback mock activity data"""
    authors = ["diwas777777", "octocat", "devuser1", "coder123"]
    actions = [
        "Added new examples for",
        "Updated documentation for",
        "Fixed bugs in",
        "Refactored code for",
        "Improved performance of"
    ]
    
    recent_activity = []
    for i in range(5):
        recent_activity.append({
            "author": authors[i % len(authors)],
            "message": f"{actions[i % len(actions)]} {['Python', 'JavaScript', 'C++'][i % 3]}",
            "date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        })
    
    return recent_activity

def count_file_lines(filepath):
    """Count lines in a file efficiently"""
    try:
        with open(filepath, 'r') as f:
            return sum(1 for _ in f)
    except:
        return 0

def get_file_info(root, filename):
    """Get detailed information about a code file"""
    filepath = os.path.join(root, filename)
    return {
        "name": filename,
        "size": os.path.getsize(filepath),
        "lines": count_file_lines(filepath),
        "last_modified": datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
    }

def scan_code_examples(base_dir):
    """Scan the base directory for language directories and return structured data"""
    languages = []
    excluded_dirs = ['.git', 'docs', '.github', 'site_data_files']

    for item_name in sorted(os.listdir(base_dir)):
        item_path = os.path.join(base_dir, item_name)
        if os.path.isdir(item_path) and \
           not item_name.startswith('.') and \
           item_name not in excluded_dirs:
            lang_dir = item_name
            lang_path = item_path

            lang_files = []
            supported_extensions = ('.py', '.js', '.java', '.c', '.cpp', '.cs', 
                                  '.go', '.rs', '.php', '.html', '.ts', '.sh')

            for root, _, files in os.walk(lang_path):
                for filename in sorted(files):
                    if filename.endswith(supported_extensions):
                        try:
                            file_info = get_file_info(root, filename)
                            lang_files.append(file_info)
                        except Exception as e:
                            print(f"Error processing {filename}: {e}")
                            continue

            # NEW: List all top-level files and folders (not just code files)
            items = []
            for entry in sorted(os.listdir(lang_path)):
                if entry.startswith('.'):
                    continue
                items.append(entry)

            if lang_files or items:
                languages.append({
                    "name": lang_dir.capitalize(),
                    "icon": get_language_icon(lang_dir),
                    "files": lang_files,  # detailed info for future use
                    "items": items,       # simple list for frontend
                    "total_size": sum(f["size"] for f in lang_files),
                    "total_lines": sum(f["lines"] for f in lang_files)
                })
    
    return languages

def get_language_icon(lang_name):
    """Get appropriate icon for each language"""
    icons = {
        'python': '🐍',
        'javascript': 'JS',
        'java': '☕',
        'c': 'C',
        'cpp': 'C++',
        'csharp': 'C#',
        'go': 'Go',
        'rust': '🦀',
        'php': 'PHP',
        'html': 'HTML',
        'typescript': 'TS',
        'bash': '💻'
    }
    return icons.get(lang_name.lower(), lang_name.upper()[:2])

def generate_site_data():
    """Generate the complete site data structure"""
    base_dir = "../../"  # Point to the repository root

    languages = scan_code_examples(base_dir)
    # Use 'commits' instead of 'recent_activity' for frontend compatibility
    return {
        "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "languages": languages,
        "commits": get_git_history(),
        "stats": {
            "total_languages": len(languages),
            "total_files": sum(len(lang["files"]) for lang in languages),
            "total_lines": sum(lang["total_lines"] for lang in languages)
        }
    }

def main():
    try:
        print("Generating site data...")
        data = generate_site_data()
        
        # Calculate statistics
        data["stats"]["total_languages"] = len(data["languages"])
        data["stats"]["total_files"] = sum(len(lang["files"]) for lang in data["languages"])
        data["stats"]["total_lines"] = sum(lang["total_lines"] for lang in data["languages"])
        
        # Write to site_data.json
        output_dir = "docs"
        output_path = os.path.join(output_dir, "site_data.json")
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Successfully generated {output_path}")
        print(f"Stats: {data['stats']['total_languages']} languages, "
              f"{data['stats']['total_files']} files, "
              f"{data['stats']['total_lines']} lines of code")
        
    except Exception as e:
        print(f"Error generating site data: {e}")
        raise

if __name__ == "__main__":
    from datetime import timedelta 
    main()