"""
✅ Problem 2: Sort List of Tuples by Second Value Using Lambda
Level: Medium
Concepts: lambda, sorting

Task:
Given a list of tuples where each tuple contains a name and score, sort the list in descending order by score using a lambda function.

Example Input:
[("Alice", 85), ("Bob", 92), ("Charlie", 78)]

Expected Output:
[('Bob', 92), ('Alice', 85), ('Charlie', 78)]
"""

def sort_by_score(data: list) -> list:
    """
    Sort a list of (name, score) tuples in descending order based on the score using a lambda function.
    """
    return sorted(data, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    
    try:
        n = int(input("Enter number of entries: "))
        data = []

        for _ in range(n):
            entry = input("Enter name and score (e.g. John 80): ").split()
    
            if len(entry) != 2 or not entry[1].isdigit():
                print("Invalid input. Please enter in 'Name Score' format.")
                continue
            name, score = entry[0], int(entry[1])
            data.append((name, score))

        sorted_data = sort_by_score(data)
        print("\nSorted Data (by score descending):")
    
        for name, score in sorted_data:
            print(f"{name}: {score}")

    except ValueError:
        print("Please enter a valid number.") 
    
    except Exception as e:
        print(f"Unexpected error: {e}")
