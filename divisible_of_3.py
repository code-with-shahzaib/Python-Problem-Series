"""
Task:
Take a list of integers (space-separated) from the user.
Count how many numbers are divisible by 3.
Print the list of those numbers.
Also print how many such numbers are found.
If none, show: "No numbers divisible by 3.
"""

def divisible_of_three(num_list: list) -> tuple:
    """Function to find a list of numbers from given list that are divisible by 3"""

    multiple_of_3 = [item for item in num_list if item % 3 == 0]
    # List to store multiple of number three

    return multiple_of_3, len(multiple_of_3)


if __name__ == "__main__":

    nums = list(map(int, input("Enter numbers (space-separated): ").split()))

    try:
        if nums:
            multiple_of_3, count = divisible_of_three(nums)
            
            if multiple_of_3:
                print(f"The list of numbers that are multiple of three: {multiple_of_3}")
                print(f"Count of numbers that are multiple of three: {count}")

            else:
                print("No numbers divisible by 3")
        
        else:
            print("No number entered.")
    
    except ValueError:
        print("Enter a valid input!")
    
    except Exception as e:
        print(f"An unexpected error occured!\n{e}")