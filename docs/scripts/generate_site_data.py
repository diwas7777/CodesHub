import os
import json
import subprocess

def get_language_directories():
    """
    Scans the root directory of the repository for language directories.
    Excludes common non-language directories and files.
    """
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    excluded_items = {'.git', '.github', 'docs', 'README.md', 'LICENSE'}
    language_dirs = []
    try:
        for item in os.listdir(repo_root):
            item_path = os.path.join(repo_root, item)
            if os.path.isdir(item_path) and \
               not item.startswith('.') and \
               not item.startswith('_') and \
               item not in excluded_items:
                language_dirs.append(item)
    except OSError as e:
        print(f"Error listing repository root: {e}")
        return []
    return sorted(language_dirs)

def get_recent_commits():
    """
    Fetches the last 10 commit messages from the git log.
    """
    try:
        # Ensure we are in the repository root for the git command
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%h - %an, %ar : %s', '-n', '10'],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_root  # Run the command from the repository root
        )
        commits = result.stdout.strip().split('\n')
        # Filter out empty strings if any
        commits = [commit for commit in commits if commit]
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error executing git log: {e}")
        print(f"Stderr: {e.stderr}")
        return []
    except FileNotFoundError:
        print("Error: git command not found. Please ensure git is installed and in PATH.")
        return []

if __name__ == "__main__":
    languages = get_language_directories()
    commits = get_recent_commits()

    site_data = {
        "languages": languages,
        "commits": commits
    }

    # Determine the output path for site_data.json, which is docs/site_data.json
    # The script is in docs/scripts/generate_site_data.py
    # So the output path is ../site_data.json relative to the script
    script_dir = os.path.dirname(__file__)
    output_path = os.path.abspath(os.path.join(script_dir, "..", "site_data.json"))

    try:
        with open(output_path, 'w') as f:
            json.dump(site_data, f, indent=4)
        print(f"Site data generated successfully at {output_path}")
    except IOError as e:
        print(f"Error writing site data to JSON file: {e}")

    # As a fallback, print to stdout if file writing fails or for debugging
    # print(json.dumps(site_data, indent=4))
    # print(f"Languages found: {languages}")
    # print(f"Commits found: {commits}")
    # print(f"Script location: {__file__}")
    # print(f"Script directory: {script_dir}")
    # print(f"Output path: {output_path}")
    # print(f"Repository root (estimated for lang scan): {os.path.abspath(os.path.join(script_dir, '..', '..'))}")
    # print(f"Repository root (estimated for git log): {os.path.abspath(os.path.join(script_dir, '..', '..'))}")

    # For testing purposes, let's list the files in the repo root
    # repo_root_test = os.path.abspath(os.path.join(script_dir, "..", ".."))
    # print(f"Contents of repo root ({repo_root_test}): {os.listdir(repo_root_test)}")
    # print(f"Current working directory for script: {os.getcwd()}")
