"""
✅ Problem 2: Merge Two Dictionaries
Level: Medium
Concepts: Dictionary, Loops

Task:
Write a function that merges two dictionaries. If a key exists in both, add their values. If it exists in one, just copy it.

Example Input:
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 50}

Expected Output:
{'a': 10, 'b': 35, 'c': 35, 'd': 50}
"""

def merge_two_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries. If a key exists in both, add the values. 
    Otherwise, just copy the key and its value.
    """
    merged_dict = {}

    # Loop through the first dictionary
    for key in dict1:
        merged_dict[key] = dict1[key]

    # Loop through the second dictionary
    for key in dict2:
       
        if key in merged_dict:
            merged_dict[key] += dict2[key]  # Add values if key already exists
       
        else:
            merged_dict[key] = dict2[key]   # Else, copy the new key-value pair

    return merged_dict


if __name__ == "__main__":

    dict1 = {'a': 10, 'b': 20, 'c': 30}
    dict2 = {'b': 15, 'c': 5, 'd': 50}

    result = merge_two_dicts(dict1, dict2)
    print(result)  # {'a': 10, 'b': 35, 'c': 35, 'd': 50}