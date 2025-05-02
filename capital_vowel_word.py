"""
Task:
Take a sentence input from the user.
Find all words that start with a vowel (a, e, i, o, u — case insensitive)
Convert them to uppercase
Print the final list
Also, print the total count
If no such word found, print: "No vowel-starting words found.
"""

def capital_vowel_words(sentence: str) -> tuple:
    """
    Function that is used for:
    - Take a sentence, find words that are starting from vowels
    - Convert these words into uppercase
    - Return the list that contains these words and the count of such words in sentence
    """

    vowels = {'a', 'e', 'i', 'o', 'u'} # Set of vowels
    words = sentence.split() # Split sentence into words
    final_list = [word.upper() for word in words if word[0].lower() in vowels] # List comprehension to store those words that starting with vowel
    return final_list, len(final_list)


if __name__ == "__main__":

    try:
        sentence = input("Enter a sentence: ").strip()

        if sentence:
            final_list, count = capital_vowel_words(sentence)
            
            if final_list:
                print("Words that start with a vowel:", ", ".join(final_list))
                print(f"Count of words that start with a vowel: {count}")
            
            else:
                print("No words starting with a vowel.")
        
        else:
            print("No sentence entered.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
