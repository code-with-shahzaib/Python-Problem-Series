""" 
Task:
Remove Odd Numbers:
Take a list of numbers (space-separated) from the user.
Remove all the odd numbers (numbers not divisible by 2).
Print the final list of only even numbers.
Also, print how many odd numbers were removed.
"""

def remove_odds(nums_list: list) -> tuple:
    """Removes odd numbers from the list and returns even numbers list and count of removed items."""

    even_list = [item for item in nums_list if item % 2 == 0]
    num_of_removals = len(nums_list) - len(even_list)
    
    return even_list, num_of_removals

if __name__ == "__main__":
    
    try:
        nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
        
        if nums:
            even_nums, removed_count = remove_odds(nums)
            
            if even_nums:
                print(f"The even numbers list only: {even_nums}")
    
            else:
                print("No even numbers found.")
            
            print(f"Number of odd numbers removed: {removed_count}")
    
        else:
            print("No numbers entered.")

    except ValueError:
        print("Please enter valid numbers!")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
