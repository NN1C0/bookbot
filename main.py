import argparse

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", help="Filepath to book")

    args = argparser.parse_args()
    book_path = args.file
        
    try:
        with open(book_path) as f:
            book_content = f.read()
            print(f"--- Begin report of {book_path} ---")
            print(f"The file contains {count_words(book_content)} words")
            counted_letters = count_letters(book_content)

            for letter in dict(sorted(counted_letters.items(), reverse=True, key=lambda item: item[1])):
                print(f"{letter} was found {counted_letters[letter]} times")

            print("--- End report ---")
    except OSError as e:
        print("File doesn't exist. Try again")
    except Exception as e:
        print(e)


def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    letter_counter = {}
    for l in text:
        if l.isalpha():
            if l in letter_counter:
                letter_counter[l] += 1
            else:
                letter_counter[l] = 1

    return letter_counter

def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()