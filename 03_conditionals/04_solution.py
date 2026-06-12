fruit = "banana"

color = input("What the color:")

if fruit == "banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    elif color == "Red":
        print("This is not a banana")
    else:
        print("I am only familiar with bananas")