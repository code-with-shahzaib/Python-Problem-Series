"""
Task:
Take a sentence input from the user.
Count how many words are 3 characters or shorter.
Print those short words in a list.
Also, print the count.
If none are found, print: "No short words found."
"""

def count_shorter_words(sentence: str) -> tuple:
    """
    Function for filtering shorter words than 3 characters:
    - Takes a sentence
    - Returns the list of such words and their count
    """

    words = sentence.split()

    # Filter words that have length less than or equal to 3
    shorter_words = [word for word in words if len(word) <= 3]

    return shorter_words, len(shorter_words)


if __name__ == "__main__":

    try:
        sentence = input("Enter a sentence: ").strip()

        if sentence:
            formated_list, count = count_shorter_words(sentence)

            
            if formated_list:
                print(f"The list that contains shorter words: {formated_list}")
                print(f"The count of shorter words: {count}")
            
            else:
                print("No short words found.")
        
        else:
            print("No input entered.")
        
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
