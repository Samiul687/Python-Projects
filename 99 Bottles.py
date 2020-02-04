def bottleno(n):
    if n == 0:
        return "No more bottles "
    elif n == 1:
        return str(n) + " bottle "                                        # Need to convert to string to add n to a string
    else:                                                                 #bottleno(n) s a variable it changes depending on the value of n. Check line 11 and 13
        return str(n) + " bottles "                                       # def stands for define. This is to define what bottleno(n) is


def printsong(n=99):
    if (n == 0):
        return bottleno(n) + "of beer on the wall, " + bottleno(
            n) + "of beer.\nGo to the store and buy some more," + bottleno(n) + " bottles of beer on the wall"
    else:
        return bottleno(n) + "of beer on the wall," + bottleno(
            n) + "of beer.\nTake one down and pass it around," + bottleno(n - 1) + "of beer on the wall.\n\n" + printsong(n-1)


print(printsong(99))
