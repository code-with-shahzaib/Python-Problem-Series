"""
Task:
Take a sentence from the user.
Count how many words start with a vowel (a, e, i, o, u -- case insensitive).
Print the list of those words.
Also show the total count.
If none, show: "No words starting with a vowel."
"""

def count_words(sentence: str) -> tuple:
    """
    Takes a sentence and returns:
    - A list of words starting with a vowel (case-insensitive)
    - The count of such words
    """
    vowels = {'a', 'e', 'i', 'o', 'u'} # Set of vowels
    words = sentence.split() # Split sentence into words
    final_list = [word for word in words if word[0].lower() in vowels] # List comprehension to store those words that starting with vowel
    return final_list, len(final_list)


if __name__ == "__main__":

    try:
        sentence = input("Enter a sentence: ").strip()

        if sentence:
            final_list, count = count_words(sentence)
            
            if final_list:
                print(f"Words that start with a vowel: {final_list}")
                print(f"Count of words that start with a vowel: {count}")
            
            else:
                print("No words starting with a vowel.")
        
        else:
            print("No sentence entered.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
