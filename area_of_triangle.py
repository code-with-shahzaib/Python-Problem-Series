# Find the area of triangle

def area_of_triangle(base:float, perp_height:float) -> float:
    return 0.5 * base * perp_height

if __name__ == "__main__":

    try:
        base = float(input("Enter the base of the triangle: "))
        perp_height = float(input("Enter the perpendicular height of the triangle: "))
        area = area_of_triangle(base, perp_height)
        print(f"The area of triangle: {area:.2f}")
    
    except ValueError as e:
        print(f"An error occured!\n{e}")
    
    except Exception as e:
        print(f"An error occured!\n{e}")


    # OR For more learning
    try:
        base_height = list(map(float, input("Enter the base and height (space-separated): ").split()))
        base, perp_height = base_height[0], base_height[1]
        area = area_of_triangle(base, perp_height)
        print(f"The area of triagnle: {area:.2f}")
    
    except ValueError as e:
        print(f"An error occured!\n{e}")
    
    except Exception as e:
        print(f"An error occured!\n{e}")