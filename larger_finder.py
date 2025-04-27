"""
Task:
Find Numbers Greater than 50:
Take a list of numbers (space-separated) from the user.
Keep only those numbers which are greater than 50.
Print the final list.
Also print the count of numbers greater than 50.
"""

def numbers_greater_than_50(lst: list) -> tuple:
    """Returns a list of numbers greater than 50 and the count of numbers removed."""
   
    greater_than_50 = [item for item in lst if item > 50]
    removed_count = len(lst) - len(greater_than_50)
   
    return greater_than_50, removed_count

if __name__ == "__main__":
    
    try:
        nums = list(map(int, input("Enter numbers (space-separated): ").split()))
        
        if nums:
            greater_nums, removed_count = numbers_greater_than_50(nums)
            
            if greater_nums:
                print(f"Numbers greater than 50: {greater_nums}")
    
            else:
                print("No numbers greater than 50 found.")
            
            print(f"Numbers removed (not greater than 50): {removed_count}")
    
        else:
            print("No numbers entered.")

    except ValueError:
        print("Please enter valid numbers!")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")

