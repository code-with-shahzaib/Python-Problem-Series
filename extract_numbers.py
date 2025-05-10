"""
✅ Problem 1: Extract Digits from a Sentence
Level: Easy
Task:
Write a program that takes a sentence from the user and extracts all numeric digits from it.

Example Input:
"My phone number is 0341 and I have 2 SIMs."

Expected Output:
Extracted digits: ['0', '3', '4', '1', '2']
"""
import string as str

def extract_digits(sentence: str) -> tuple:
    """Functon that takes a sentence from user and extracts all numeric digits from it and return a list of numbers and their count"""

    digits = [char for char in sentence if char.isdigit()] # List to store digits from the sentence
    
    return digits, len(digits)


if __name__ == "__main__":

    try:
        sentence = input("Enter a sentence: ")

        if sentence:
            digits, count = extract_digits(sentence)
        
            if digits:
                print(f"The digits in the sentence are: {digits}")
                print(f"The count of such numbers is: {count}")
            
            else:
                print("No digits found.")
        
        else:
            print("No sentence entered!")
    
    except ValueError:
        print("Please enter a valid input.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
        