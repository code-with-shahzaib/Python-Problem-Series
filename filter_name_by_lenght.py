"""
Task:
Take a list of names (space-separated) from the user.
Filter and print only the names that have more than 5 characters.
Also show the total count of such names.
If no name is found, print: "No long names found.
"""

def filter_by_length(names: list) -> tuple:
    """Function to filtre names that have length more than 5. It takes a list of names space separated and return the tuple of names with larger lenghts and the count of this list"""
    larger_length_names = [item for item in names if (len(item) > 5)]
    return larger_length_names, len(larger_length_names)


if __name__ == "__main__":

    names = list(map(str, input("Enter names (space-separated): ").split()))

    try:
        if names:
            larger_names, count = filter_by_length(names)
        
            if larger_names:
                print("Long Names:")
                
                for i in larger_names: # Loop to iterate over long names and print them
                    print(i, end=", ")

                # print(f"The list of larger names: {larger_names}")
                print(f"\nThe count of larger length names: {count}")
            
            else:
                print("No long names found.")
            
        else:
            print("No names entered.")
    
    except ValueError:
        print("Enter a valid input!")
    
    except Exception as e:
        print(f"An unexpected error occured!\n{e}")
