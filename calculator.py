print("==================\n Area Calculator 📐\n==================")
print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")



while True:
    shape = input("Which shape: ")
    if shape == "1":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}")
    elif shape == "2":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area}")
    elif shape == "3":
        side = float(input("Enter the side: "))
        area = side ** 2
        print(f"The area of the square is {area}")
    elif shape == "4":
        radius = float(input("Enter the radius: "))
        area = 3.14159 * radius ** 2
        print(f"The area of the circle is {area}")
    elif shape == "5":
        break
    else:
        print("Invalid option. Please try again.")
    