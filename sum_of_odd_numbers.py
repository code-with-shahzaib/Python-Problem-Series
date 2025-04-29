"""
Task:
Write a Python program that:
Takes a list of numbers (space-separated) from the user.
Calculates the sum of all odd numbers in the list.
If there are no odd numbers, print: "No odd numbers found."
Otherwise, print the sum of odd numbers.
"""

def sum_of_odd(nums_list: list) -> tuple:
    
    """Function to calculate sum of odd numbers. And return a tuple with sum of odd list and length of odd list"""
    odd_list = [item for item in nums_list if item % 2 != 0]
    return sum(odd_list), len(odd_list)


if __name__ == "__main__":

    try:
        nums_list = list(map(int, input("Enter numbers (space-separated): ").split()))
        
        if nums_list:
            odd_sum, odd_count = sum_of_odd(nums_list)
            
            if odd_count == 0:
                print("No odd numbers found.")
            
            else:
                print(f"Sum of odd numbers: {odd_sum:.2f}")
        
        else:
            print("No numbers entered.")
        
    except ValueError:
        print("Please enter valid numbers!")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
