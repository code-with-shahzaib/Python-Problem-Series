"""
Remove Duplicates While Preserving Order
Level: Medium
Write a function that removes duplicates from a list but keeps the original order.

Example Input:
    [1, 3, 2, 1, 3, 4, 2, 5]
Expected Output:
    [1, 3, 2, 4, 5]
"""

def remove_duplicates_ordered(items: list) -> list:
    """
    Removes duplicates from a list while maintaining the original order.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":

    try:
        input_list = list(map(int, input("Enter numbers separated by space: ").split()))
        
        if input_list:
            final_result = remove_duplicates_ordered(input_list)
            
            if final_result:
                print("Final list without duplicates:", final_result)
                
            else:
                print("No duplicates found.")
        else:
            print("No input entered.")
            
    except ValueError:
        print("Invalid input! Please enter integers only.")
