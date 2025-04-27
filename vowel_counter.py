"""
Task:
Write a Python program that:
Takes a sentence from the user.
Counts how many vowels (a, e, i, o, u) are in the sentence.
Ignores capital/small case (so A and a both are vowels).
Prints the total number of vowels.
"""

def vowel_counter(sentence:str) -> int:
    
    vowel_list = ['a', 'e', 'i', 'o', 'u'] # List of vowels
    vowel_count = 0 # vowel count in sentence initialy it's 0

    for char in sentence: # Loop to iterate over the sentece characters
        if char in vowel_list: # Conditon that check the membership of char in vowel list
            vowel_count += 1 # If yes then increase vowel count by 1
    
    return vowel_count


if __name__ == "__main__":

    try:
        sentence = input("Enter a sentence: ").lower().strip()
        vowel_count = vowel_counter(sentence)
        print(f"The total number of vowels in sentence: {vowel_count}")
    
    except ValueError:
        print("Enter a valid input!")
    
    except Exception as e:
        print(f"An unexpected error occured!\n{e}")