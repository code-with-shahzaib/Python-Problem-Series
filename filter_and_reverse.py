"""
Task:
Take a list of integers (space-separated) from the user.
Keep only numbers less than or equal to 50
Reverse the list
Print the final reversed filtered list
Also, print the count of numbers in the final list
If none match, print: "No numbers ≤ 50 found."
"""

def filter_and_reverse(numbers: list) -> tuple:
    """
    This function is for:
    - Take a list from the user
    - Return a reversed list of numbers that are less than or equall to 50 and length of this list
    """

    filtered_list = [num for num in numbers if num <= 50] # List to store numbers less than or equal to 50
    filtered_list.reverse()  # Reverse the list

    return filtered_list, len(filtered_list)


if __name__ == "__main__":

    try:

        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))

        if numbers:
            final_list, count = filter_and_reverse(numbers)

            if final_list:
                print(f"The filtered and reversed list is: {final_list}")
                print(f"Count of numbers that are less than or equal to 50: {count}")
            
            else:
                print("No numbers ≤ 50 found")
        
        else:
            print("No input entered")
    
    except ValueError:
        print("Please enter a valid number")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")