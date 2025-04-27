"""
Task:
Take a list of numbers from the user (space-separated).
Remove all duplicate numbers.
Sort the unique numbers in ascending order.
Print the final list.
"""

def unique_sorted_list(lst : list) -> str:
    unique_list = list(set(lst))
    unique_list.sort()

    return f"Unique and Sorted list: {unique_list}"

    
if __name__ == "__main__":
    
    lst = []
    length = int(input("How many elements do you want to store in list: "))
    
    for i in range(1, length + 1):
        item = int(input(f"Enter element no. {i}: "))
        lst.append(item)

    print(unique_sorted_list(lst))