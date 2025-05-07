"""
✅ Problem 2: Group Words by First Letter
Level: Medium
Task:
Given a list of words, group them in a dictionary where the key is the first letter, and the value is a list of words starting with that letter.

Example Input:
['apple', 'banana', 'apricot', 'blueberry', 'cherry']

Example Output:
{
  'a': ['apple', 'apricot'],
  'b': ['banana', 'blueberry'],
  'c': ['cherry']
}
"""

def group_word_by_1_letter(words: list) -> dict:
    """
    Group words by first letter and return a dictionary where
    the key is the first letter and the value is a list of words starting with that letter.
    """

    group_dict = {}

    for word in words:
        first_letter = word[0].lower()  # Ensures case insensitivity
        if first_letter not in group_dict:
            group_dict[first_letter] = [word]
        else:
            group_dict[first_letter].append(word)

    return group_dict


if __name__ == "__main__":

    try:
        words = list(map(str, input("Enter words space-separated: ").split()))

        if words:
            group_dict = group_word_by_1_letter(words)

            if group_dict:
                print(f"Group Words: {group_dict}")
            
        else:
            print("No input entered")

    except ValueError:
        print("Please enter a valid input")

    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
