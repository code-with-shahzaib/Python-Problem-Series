"""
Task:
Find and Print Perfect Squares
🔹 Write a Python program that:
Takes a list of numbers (space-separated) from the user.
Finds all numbers that are perfect squares (like 1, 4, 9, 16, 25, etc.).
Prints the list of perfect squares found.
Also prints the count of perfect squares.
"""
import math


def find_perfect_squares(num_list: list) -> list:
   
    """Function to find perfect square numbers"""
    perfect_square_list = []
    
    for item in num_list:
        
        if item >= 0:  # Only positive numbers and zero (0) can have real square roots
            root = math.sqrt(item)
            
            if root.is_integer():  # Check if the square root is a whole number
                perfect_square_list.append(item)
    
    return perfect_square_list

if __name__ == "__main__":
    
    try:
        nums = list(map(int, input("Enter numbers (space-separated): ").split()))
        
        if nums:
            perfect_squares = find_perfect_squares(nums)
            
            if perfect_squares:
                print(f"Perfect squares found: {perfect_squares}")
                print(f"Count of perfect squares: {len(perfect_squares)}")
            
            else:
                print("No perfect squares found.")
        
        else:
            print("No numbers entered.")

    except ValueError:
        print("Please enter valid numbers!")

    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
