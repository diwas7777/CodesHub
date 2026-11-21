import os
from dotenv import load_dotenv
from google import genai


# Load environment variables (make sure you set GOOGLE_API_KEY in .env)
load_dotenv()
client = genai.Client()

def read_task(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def summarize_text(tasks):
    prompt = f"""
    You are a smart task planning agent.
    Given the following list of tasks, categorize them into 3 categories:
    - High
    - Medium
    - Low

    Tasks:
    {tasks}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # The SDK doesn’t return `choices` like OpenAI
    return response.text

if __name__ == "__main__":
    task_text = read_task("task.txt")
    summary = summarize_text(task_text)
    print("********")
    print(summary)
