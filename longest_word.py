"""
Task:
Take a sentence input from the user.
Identify the longest word(s) in the sentence.
If multiple words have the same maximum length, show them all.
Print the list of longest words and their length.
"""

def find_longest_words(sentence: str) -> tuple:
    """
    Takes a sentence and returns:
    - A list of longest word(s)
    - The length of those words
    """
    words = sentence.split()
    max_length = 0
    longest_words = []

    for word in words:
        length = len(word)
        
        if length > max_length:
            max_length = length
            longest_words = [word]
        
        elif length == max_length:
            longest_words.append(word)

    return longest_words, max_length


if __name__ == "__main__":
    try:
        sentence = input("Enter a sentence: ").strip()

        if sentence:
            words, length = find_longest_words(sentence)
            
            if words:
                print(f"The longest word(s): {words}")
                print(f"Length of the longest word(s): {length}")
            
            else:
                print("No words found.")
        
        else:
            print("No input entered!")

    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
