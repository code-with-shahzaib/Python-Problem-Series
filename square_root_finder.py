import math

# Basic method
n = 453
squar_root = n ** 0.5
print(squar_root)


# Intemediate method
n = float(input("Enter a number: "))
squar_root = n ** 0.5
print(f"The square root of {n} = {squar_root:.2f}")

# Slightly Advance method
def sqaureRoot():
    
    try:
        n = float(input("Enter a number: "))
        squar_root = n ** 0.5
        print(f"The square root of {n} = {squar_root:.2f}")
    
    except ValueError:
        print("Enter a valid number.")

sqaureRoot()


# Advance method
def sqaureRoot2():
    
    try:
        n = float(input("Enter a number: "))
        squar_root = math.sqrt(n)
        print(f"The square root of {n} = {squar_root:.2f}")
    
    except ValueError:
        print("Enter a valid number.")

sqaureRoot2()