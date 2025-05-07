"""
✅ Problem 1: Find Prime Numbers in a Range
Level: Easy
Task:
Write a program that takes a start and end number from the user and prints all prime numbers in that range.
Example Input:
Start = 10, End = 30

Example Output:
[11, 13, 17, 19, 23, 29]
"""

def find_prime_numbers(start: int, end: int) -> list:
    """
    Count the prime numbers in the given range and return the list of these numbers.
    """
    prime_nums = []
    
    for i in range(start, end + 1):
        if i <= 1:
            continue
        
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
        
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_nums.append(i)
    
    return prime_nums


if __name__ == "__main__":

    try:
        range_nums = list(map(int, input("Enter start and end number of range to check prime numbers (space-separated): ").split()))   

        if range_nums:
            start, end = range_nums[0], range_nums[1]
            prime_nums = find_prime_numbers(start, end)

            if prime_nums:
                print(f"Prime numbers in given range: {prime_nums}")

            else:
                print("No prime number found.")
        
        else:
            print("No number entered!")

    except ValueError:
        print("Please enter a valid number.")
    
    except Exception as e:
        print(f"An unexpected error occurred!\n{e}")