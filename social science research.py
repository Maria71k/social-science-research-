def count_word_occurrences(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word = word.lower()
        word = word.strip(",.?!")  # Remove punctuation
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

def main():
    # Sample text data (could be replaced with actual text data)
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    word_counts = count_word_occurrences(text)
    print("Word Occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
