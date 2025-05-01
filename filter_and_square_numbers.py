"""
Task:
Take a list of integers (space-separated) from the user.
Keep only the numbers that are greater than 10.
Square each of those numbers.
Print the final list.
Also, print how many numbers were squared.
If no number is greater than 10, show: "No numbers greater than 10."
"""

def filter_and_square(numbers: list) -> tuple:
    """
    Take a list and returns:
    - A list of numbers
    - Square greater numbers than 10 
    - The list and count of list
    """

    formated_list = [(num ** 2) for num in numbers if (num > 10)]  # List to store numbers that are greater than 10

    return formated_list, len(formated_list)


if __name__ == "__main__":

    try:
        numbers_list = list(map(int, input("Enter numbers (space-separated): ").strip().split()))

        if numbers_list:
            formated_list, count = filter_and_square(numbers_list)

            if formated_list:
                print(f"The list of square of numbers that are greater than 10: {formated_list}")
                print(f"Count of such numbers: {count}")

            else:
                print("No number greater than 10 found.")

        else:
            print("No number entered.")
        
    except ValueError:
        print("Enter a valid number!")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}.")
