"""
Problem 1: Indexed Filter
Task:
Take a list of strings from the user.
Use enumerate() to print only the even-indexed words.

Example:
    Input: apple banana cherry mango kiwi
    Output: Index 0: apple
            Index 2: cherry
            Index 4: kiwi
"""

def print_even_indexed_words(sentence: str):
    """
    This function prints words at even indexes using enumerate.
    """
    words = sentence.split()
    
    for index, word in enumerate(words):
        if index % 2 == 0:
            print(f"Index {index}: {word}")


if __name__ == "__main__":
   
    try:
        user_input = input("Enter a sentence: ").strip()
        
        if user_input:
            print_even_indexed_words(user_input)
        
        else:
            print("No input provided.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
