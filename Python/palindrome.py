#!/usr/bin/env python3
def isPalindrome(word: str) -> bool:
        return True if word.lower() == ''.join(list(reversed(word.lower().split()))) else False


def constructAnswer(word: str, isPalindromic: bool) -> None:
    sentence: str = f'The word, {word}, is '
    return sentence + 'palindromic.' if isPalindromic else sentence + 'not palindromic.'


if __name__ == '__main__':
    word: str = input('Please enter a word:\n>>>')
    print(constructAnswer(word, isPalindrome(word)))
    