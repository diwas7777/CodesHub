import os
import json
import subprocess

def get_language_data():
    """
    Scans the root directory of the repository for language directories,
    and then lists the top-level contents of each language directory.
    Excludes common non-language directories and files, as well as
    common build/dependency folders within each language directory.
    """
    script_dir = os.path.dirname(__file__)
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    
    # Exclusions for top-level (repo root) items
    top_level_excluded_items = {'.git', '.github', 'docs', 'README.md', 'LICENSE'}
    
    # Exclusions for items within each language directory
    inner_excluded_items = {'__pycache__', 'node_modules', 'target', 'build', 'dist', '.DS_Store'}

    languages_data = []
    
    try:
        # First, identify the main language directories
        for item_name in os.listdir(repo_root):
            item_path = os.path.join(repo_root, item_name)
            if os.path.isdir(item_path) and \
               not item_name.startswith('.') and \
               not item_name.startswith('_') and \
               item_name not in top_level_excluded_items:
                
                # Now, scan the contents of this language directory
                language_dir_path = item_path # This is already the absolute path
                current_language_files = []
                try:
                    for sub_item_name in os.listdir(language_dir_path):
                        if not sub_item_name.startswith('.') and \
                           sub_item_name not in inner_excluded_items:
                            current_language_files.append(sub_item_name)
                    
                    if current_language_files: # Only add if there are files/subdirs to list
                        languages_data.append({
                            "name": item_name,
                            "files": sorted(current_language_files)
                        })
                    else:
                        # Optionally, still add the language if it's empty but detected
                        languages_data.append({
                            "name": item_name,
                            "files": []
                        })

                except OSError as e:
                    print(f"Error scanning language directory {language_dir_path}: {e}")
                    # Add language with empty files list if scanning fails for some reason
                    languages_data.append({
                        "name": item_name,
                        "files": []
                    })

    except OSError as e:
        print(f"Error listing repository root: {e}")
        return [] # Return empty if repo root scan fails

    return sorted(languages_data, key=lambda x: x['name'])


def get_recent_commits():
    """
    Fetches the last 10 commit messages from the git log.
    """
    script_dir = os.path.dirname(__file__)
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    try:
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%h - %an, %ar : %s', '-n', '10'],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_root
        )
        commits = result.stdout.strip().split('\n')
        commits = [commit for commit in commits if commit] # Filter out empty strings
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error executing git log: {e}")
        print(f"Stderr: {e.stderr}")
        return []
    except FileNotFoundError:
        print("Error: git command not found. Please ensure git is installed and in PATH.")
        return []

if __name__ == "__main__":
    language_details = get_language_data()
    recent_commits = get_recent_commits()

    site_data = {
        "languages": language_details,
        "commits": recent_commits
    }

    script_dir = os.path.dirname(__file__)
    output_path = os.path.abspath(os.path.join(script_dir, "..", "site_data.json"))

    try:
        with open(output_path, 'w') as f:
            json.dump(site_data, f, indent=4)
        print(f"Site data generated successfully at {output_path}")
    except IOError as e:
        print(f"Error writing site data to JSON file: {e}")

    # For debugging, you can uncomment these lines:
    # print("\n--- Debugging Info ---")
    # print(f"Script location: {__file__}")
    # print(f"Script directory: {script_dir}")
    # print(f"Calculated repo root: {os.path.abspath(os.path.join(script_dir, '..', '..'))}")
    # print(f"Output path for JSON: {output_path}")
    # print("Generated site_data content:")
    # print(json.dumps(site_data, indent=4))
    # print("--- End Debugging Info ---")
