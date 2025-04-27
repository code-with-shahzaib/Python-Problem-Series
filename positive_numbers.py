"""
Task:
Take numbers from the user (space-separated).
Only keep positive numbers (ignore zero and negative numbers).
Print the final list of positive numbers.
"""

def positive_numbers(lst: list) -> list:
    
    positive_list = [item for item in lst if item > 0]
    return positive_list

if __name__ == "__main__":
    
    try:
        nums = list(map(int, input("Enter numbers (semicolon-separated): ").split(";")))

        if not nums:
            print("No numbers entered. Exiting.")
    
        else:
            result = positive_numbers(nums)
            print(f"The positive numbers list: {result}")

    except ValueError:
        print("Invalid input! Please enter only integers separated by semicolons.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")
