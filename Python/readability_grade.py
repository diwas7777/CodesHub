# Readability grading evaluates the ease with which a text can be comprehended. Metrics like Flesch-Kincaid
# consider factors like average sentence length and syllables per word. Assessing readability aids in tailoring
# communication for diverse audiences, ensuring accessibility and understanding across various reading levels.

# Coleman-Liau formula measures text complexity using characters, words, and sentences, providing a simplified
# readability score for effective communication.

from sys import exit


def main():
    """Get text input"""
    text = input("Text: ")
    text_len = len(text)

    # If no text provided, exit
    if text_len == 0:
        print("No text provided!")
        exit(1)

    grade = grade_calc(text, text_len)

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def grade_calc(text, text_len):
    letters, sentences = 0, 0

    """We'll check each char in text, if it is alphabet, then count as letter"""
    for index in range(text_len):
        if text[index].isalpha():
            letters += 1
        # If char is '.', then check if next value is also one of 3 '.', '!', '?',
        # if yes then skip, if not then count as sentence
        elif text[index] in (".", "!", "?"):
            if text[(index + 1) % text_len] in (".", "!", "?"):
                continue
            sentences += 1

    words = len(text.split())
    sentences = 1 if sentences == 0 and words > 2 else sentences

    # Coleman-Liau grading formula: 0.0588 * L(Letters per 100 words) - 0.296 * S(Sentences per 100 words) - 15.8
    grade_index_C_and_L = (
        0.0588 * ((letters / words) * 100) - 0.296 * ((sentences / words) * 100) - 15.8
    )

    return round(grade_index_C_and_L)


if __name__ == "__main__":
    main()
