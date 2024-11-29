from collections import OrderedDict

def main():
    book_location = "books/frankenstein.txt"
    report_printer(book_location)

def get_book_text(location):
    with open(location) as f:
        return f.read()

def word_counter(text):
    return len(text.split())

def count_characters(text):
    each_character_amount = {}
    for letter in text.lower():
        if letter in each_character_amount:
            each_character_amount[letter] +=1
        else:
            each_character_amount[letter] = 1
    return each_character_amount

def report_printer(book_location):
   
    book_text = get_book_text(book_location)
    characters = count_characters(book_text)

    print(f"--- Begin report of {book_location} ---")
    print(f"{word_counter(book_text)} words found in the document")
    print()
    ordered_characters = OrderedDict(sorted(characters.items(), key=lambda index: index[1], reverse=True))
    for character, number in ordered_characters.items():
        if character.isalpha():
            print(f"The '{character}' character was found {number} times")
    print("--- End report ---")

main()