def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read()
        
        words = file_contents.split()

        word_count = len(words)

        to_lower = file_contents.lower()

        character_counts = char_counts(to_lower)

        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document\n\n")
        for char, count in character_counts.items():
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")


def char_counts(text):
    character_counts = {}
    for char in text:
        if char.isalpha():
            character_counts[char] = character_counts.get(char, 0) + 1
    return character_counts

if __name__ == "__main__":
    main()