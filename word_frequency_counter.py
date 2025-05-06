"""
Word Frequency Counter
Level: Easy
Goal: Count word frequency from a paragraph in descending order, case-insensitive.
"""

from collections import Counter

def word_frequency_counter(text: str) -> list:
    """
    Counts the frequency of each word in a paragraph, ignoring case.
    Returns a sorted list of tuples (word, count) in descending order.
    """
    words = text.lower().split()
    cleaned_words = [word.strip(".,!?;:") for word in words]  # Remove punctuation
    counter = Counter(cleaned_words)
    return counter.most_common()  # returns list of (word, count)

if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ").strip()
    
    if paragraph:
        frequencies = word_frequency_counter(paragraph)
        for word, count in frequencies:
            print(f"{word}: {count}")
    else:
        print("No input provided.")
