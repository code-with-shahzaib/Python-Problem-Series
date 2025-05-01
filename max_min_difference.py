"""
Task:
Take 10 numbers from the user (space-separated).
Find the maximum and minimum number.
Calculate the difference between the maximum and minimum.
Show all three results properly.
"""

def min_max_difference(lst:list) -> str:
    
    maximum = max(lst) # Maximum number from the list
    minimum = min(lst) # Minimum number from the list
    difference = maximum - minimum # Difference between maximum and minimum

    return f"The minimum number: {minimum}\nThe maximum number: {maximum}\nDifference between maximum & minimum: {difference}"


if __name__ == "__main__":

    nums = list(map(int, input("Enter numbers (space-separated): ").split()))
    print(min_max_difference(nums))
