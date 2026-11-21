import json
import os
import random

FLASHCARD_FILE = os.path.join(os.path.dirname(__file__), "flashcards.json")

def load_flashcards():
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, "r") as f:
            return json.load(f)
    return {}

def save_flashcards(flashcards):
    with open(FLASHCARD_FILE, "w") as f:
        json.dump(flashcards, f, indent=4)

def add_flashcard(flashcards):
    word = input("Enter a word: ").strip()
    meaning = input("Enter its meaning: ").strip()
    flashcards[word] = meaning
    print(f"Added: {word} -> {meaning}")

def review_flashcards(flashcards):
    if not flashcards:
        print("No flashcards available. Add some first!")
        return
    words = list(flashcards.keys())
    random.shuffle(words)
    for word in words:
        input(f"{word} - Press Enter to see the meaning...")
        print(f"Meaning: {flashcards[word]}\n")

def main():
    flashcards = load_flashcards()
    while True:
        print("\nFlashcard App")
        print("1. Add flashcard")
        print("2. Review flashcards")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == "2":
            review_flashcards(flashcards)
        elif choice == "3":
            save_flashcards(flashcards)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
