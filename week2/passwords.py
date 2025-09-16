# Enhancement: Added a password history feature that warns users if they reuse a previously tested password.

# Character type lists
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
           "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<",
           ">", "?", "/", "`", "~"]

import os

def word_in_file(word, filename, case_sensitive=False):
    try:
        folder_path = os.path.dirname(__file__)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "topPasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    complexity = word_complexity(password)
    return 1 + complexity

def main():
    history = set()
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        if password in history:
            print("Warning: You've already tested this password.")
        else:
            history.add(password)
        strength = password_strength(password)
        print(f"Password strength: {strength}/5\n")

# Required for testing
if __name__ == "__main__":
    main()
