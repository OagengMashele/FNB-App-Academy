def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)


length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

rectangle_area = area(length, width)
rectangle_perimeter = perimeter(length, width)

print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")