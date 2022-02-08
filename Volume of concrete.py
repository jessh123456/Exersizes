Quit = "N"
depth = 0
volume = 0
total = 0
while Quit != "X":
    Building_type = input("what is the building type? press [R] for "
                          "residential or press [C] for commercial"
                          ".\n:").upper()
    Length = int(input("What is the length of the building? (In meters)\n:"))
    Width = int(input("What is the width of the building? (In meters)\n:"))
    if Building_type == "R":
        depth = 0.25
        int(depth)
    elif Building_type == "C":
        depth = 0.5
        int(depth)
    volume = Length * Width * depth
    print(f"The volume of concrete required for a slab with a length of "
          f"{Length}m, and a width of {Width}, and depth of {depth}m, is "
          f"{volume} cubic meters.")
    total += volume
    Quit = input("Press enter to continue or [X] to quit.").upper()


print(f"The total volume of concrete needed today is {total} cubic meters.")
