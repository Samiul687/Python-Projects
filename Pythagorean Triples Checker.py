exit_not_chosen = True

while exit_not_chosen:
    sides = input(
        "\nPlease type the lengths of your Triangles sides separated by commas or 'exit' to quit the programme\n").lower()

    if sides == "exit":
        exit_not_chosen = False
    else:
        sides = sides.split(",")                              # Splits input based on where commas are
        sides = list(map(int, sides))                         # Converts input from string to integer
        sides.sort()                                          # Sorts list in order of lowest to highest

        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            print("Yes, this is a Pythagorean Triple")
        else:
            print("Sorry, these are not Pythagorean Triples")
