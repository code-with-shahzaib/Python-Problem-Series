"""
Task:
Take a list of integers (space-separated) from the user.
Create a new list where:
Even numbers are doubled.
Odd numbers remain unchanged.
Print the final modified list.
Also show the count of even numbers that were doubled.
"""

def double_even_numbers(numbers:list) -> tuple:
    """
    Takes a list of numbers and returns a tuple:
    - A new list where even numbers are doubled.
    - The count of even numbers doubled.
    """

    formated_list = [] # List to store changed even numbers and unchanged odd numbers
    count = 0 # Count of even numbers in list
    
    for num in numbers: # Loop to iterate over elements of actuall list
        
        if num % 2 == 0: # Conditon to check even number if then double it and update count by 1
            formated_list.append(num * 2)
            count += 1

        else: # If not then only append element in new list
            formated_list.append(num)
        
    return formated_list, count


if __name__ == "__main__":

    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))

        if numbers:
            formated_list, count = double_even_numbers(numbers)
            
            if formated_list:
                print(f"The formated list: {formated_list}")
                print(f"Count of even numbers: {count}")

            else:
                print("No even number found.")
        
        else:
            print("No input entered.")
    
    except ValueError:
        print("Please enter a valid number.")
    
    except Exception as e:
        print(f"An unexpected error occured!\n{e}")


