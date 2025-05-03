"""
Task:
Take a list of integers (space-separated) from the user.
Remove any duplicate numbers.
Sort the list in ascending order.
Print the final list and the count of unique numbers.
"""

def remove_duplicate_and_sort(numbers:list) -> list:
    """
    Function that is used for removing duplicates and sort the list:
    - Takes list of numbers
    - Removes duplicates and sort it
    - Return the final formated list
    """

    final_list = list(set(numbers)) # List with no duplicate elements
    final_list.sort()

    return final_list


if __name__ == "__main__":

    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))

        if numbers:
            final_list = remove_duplicate_and_sort(numbers)

            if final_list:
                print(f"The formatted final list is: {final_list}")
                print(f"Count of unique numbers: {len(final_list)}")

            
            else:
                print("No duplicate number found.")
        
        else:
            print("No input entered")
        
    except ValueError:
        print("Please enter a valid input.")

    except Exception as e:
        print(f"An unexpected error occured!\n{e}")