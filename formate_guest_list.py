"""
Task:
Write a Python program that:
Takes a list of guest names (space-separated) from the user.
Formats them into a single string where:
Each name is capitalized.
Names are separated by " | ".
Prints the final guest list string.
"""


def name_formation(names: list) -> str:
    # Capitalize each name and then join them with " | "
    formatted_names = [name.capitalize() for name in names]
    final_string = " | ".join(formatted_names)
    return final_string

if __name__ == "__main__":
    
    try:
        names_input = input("Enter guest names (space-separated): ").split()
    
        if names_input:
            result = name_formation(names_input)
            print(f"Formatted Guest List:\n{result}")
    
        else:
            print("No names entered.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
