import re
import math


def solver(equation):
    try:
        equation = list(equation)

        i = 0
        while i < len(equation):
            if equation[i] == "x":
                if i == 0:
                    equation.insert(0, "1")
                elif equation[i - 1].isnumeric() is False:
                    equation.insert(i, "1")
                i += 1
            i += 1

        equation = re.split("=|\^2|x", "".join(equation))

        while "" in equation:
            equation.remove("")

        equation = list(map(int, equation))
        if len(equation) == 4:
            del equation[-1]
        if len(equation) == 2:
            equation.append(0)

        a, b, c = equation

        try:
            positive = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            negative = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

            if positive == negative:
                print(f"There is one real root: {positive}\n")
            else:
                print(f"\nThe roots are {{{positive}, {negative}}}\n")

        except:
            print("This has complex roots, please try again\n")
            start()


    except:
        print(
            "\nSomething went wrong. Please try again.\n")
        start()


def start():
    user = input("Please input the equation in the following format: \nax^2+bx+c=0\nor enter \"q\" to quit: \n").lower()
    if user == "q":
        print("\nThank you, exiting now")
        exit()
    else:
        solver(user)


while True:
    start()
