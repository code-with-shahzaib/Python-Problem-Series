"""
Task:
Take numbers from the user (space-separated).
Find and keep only the even numbers (divisible by 2).
Print the final list of even numbers.
Also print how many even numbers were entered.
If no even numbers are found, display:
"No even numbers found."
"""

def even_number_finder(nums:list) -> list: # Function to find even numbers from a list
    even_list = [item for item in nums if (item % 2 == 0)] # List to store even numbers
    return even_list

def even_number_counter(even_nums:list) -> int: # Function to count even numbers from a list
    even_count = even_number_finder(even_nums) # Variable to store even numbers count
    return len(even_count)

if __name__ == "__main__":
    
    try:
        nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
        even_nums = even_number_finder(nums)
        print(f"Even numbers from the given list: {even_nums}")

        even_count = even_number_counter(even_nums)
        if even_count == 0:
            print("No even numbers found.")
        
        else:
            print(f"Total even numbers in given list: {even_count}")
    
    except ValueError:
        print("Please enter a valid input!")
    
    except Exception as e:
        print(f"An unexpected error occured!\n{e}")