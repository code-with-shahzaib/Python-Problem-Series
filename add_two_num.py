# Very basic method
a = 43
b = 34
addition = a + b
print(addition)


# Intermediate method
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
addition = a + b
print(f"The sum of {a} + {b} = {addition:.2f}")


# Slightly advance method
def addition():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    sum = a + b
    return f"Sum of {a} + {b} = {sum}"


# Advance method
def addition2():
    try:
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))
        sum = a + b
        return f"Sum of {a} + {b} = {sum}"

    except ValueError:
        print("Please enter a valid number!")


while True:
    choice = input("What you want to do (add, exit): ").lower().strip()

    match choice:
    
        case 'add' : 
            print(addition2())
        
        case 'exit': 
            print("Thanks for using!")
            break

        case _ :
            print("Please enter a valid choice (add, eixt)")