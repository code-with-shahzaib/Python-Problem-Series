"""
✅ Problem 1: Find Index of Longest Word
Level: Easy
Concepts: enumerate, len
Task:
Write a function that takes a list of words and returns the index and value of the longest word using enumerate().

Example Input:
["python", "data", "science", "AI"]

Expected Output:
(2, 'science')  # Index 2, word = 'science'
"""


def find_index_of_longest(words: list) -> tuple:
    """
    Function that takes list of words and finds the longest word and returns it with its index
    """
    max_length = 0
    max_index = -1
    max_word = ""

    for index, word in enumerate(words):
        if len(word) > max_length:
            max_length = len(word)
            max_index = index
            max_word = word

    return max_index, max_word


if __name__ == "__main__":
    
    try:
        words = list(map(str, input("Enter words space-separated: ").split()))
    
        if words:
            longest_word = find_index_of_longest(words)
            print(f"The longest word and its index: {longest_word}")
    
        else:
            print("No input entered.")
    
    except ValueError:
        print("Please enter a valid input.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")