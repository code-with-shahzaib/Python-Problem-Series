"""
Problem 2: Lambda Filter
    Task:
        Take a list of integers from the user.
        Use a lambda function with filter() to extract all even numbers and print them.

Example:
    Input: 1 2 3 4 5 6
    Output: Even numbers: [2, 4, 6]
"""

def filter_even_numbers(numbers: list) -> list:
    """
    Filters and returns even numbers using lambda and filter.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    
    try:
        user_input = input("Enter numbers separated by space: ").strip()
        numbers = list(map(int, user_input.split()))

        even_numbers = filter_even_numbers(numbers)

        if even_numbers:
            print(f"Even numbers: {even_numbers}")
    
        else:
            print("No even numbers found.")

    except ValueError:
        print("Please enter valid integers separated by spaces.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
