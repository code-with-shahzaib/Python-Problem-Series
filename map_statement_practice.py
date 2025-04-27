""" Exercise # 1
Take names from the user (space-separated) and print them in a list."""

lst = list(map(str, input("Enter your friends name (space-separated): ").split()))

print(lst)

""" Exercise # 2
Take 5 numbers from user (space-separated), convert them into integers, and find their sum"""

num = tuple(map(int, input("Enter 5 (comma-separated) numbers which sum you want to calculate: ").split(",")))

sum_of_five = sum(num)
print(f"The sum of entered five numbers = {sum_of_five}")

""" Exercise # 3
Take any words, and count how many words user typed."""

words = list(map(str, input("Enter any words (space-separated): ").split()))
num_of_words = len(words)
print(f"You have entered {num_of_words} words.")