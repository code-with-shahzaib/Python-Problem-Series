"""
✅ Problem 1: Filter Names Starting with Vowels
Level: Easy
Concepts: Strings, Loops, Conditions

Task:
Write a function that takes a list of names and returns a new list containing only the names that start with a vowel (A, E, I, O, U), case-insensitive.

Example Input:
["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]

Expected Output:
["Alice", "Eve", "Oscar", "Uma"]
"""

def filter_names_by_vowels(names: list) -> list:
    """
    Filters and returns names that start with a vowel (A, E, I, O, U) case-insensitively.
    """
    vowels = {"a", "e", "i", "o", "u"}
    return [name for name in names if name[0].lower() in vowels]
    


if __name__ == "__main__":

    try:
        names = list(map(str, input("Enter names space-separated: ").split()))
        
        if names:
            names_with_vowels = filter_names_by_vowels(names)

            if names_with_vowels:
                print(f"The names that are startswith vowel: {names_with_vowels}")
                print(f"Count of such words: {len(names_with_vowels)}")
            
            else:
                print("No such names found.")
        
        else:
            print("No input entered!")

    except ValueError:
        print("Please enter a valid input")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
        