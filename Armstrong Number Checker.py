def is_armstrong(number):                                          # Function to test numbers
    digits = (int(x) for x in str(number))                         # Generator expression to separate digits
    if sum(i ** len(number) for i in digits) == int(number):       # Finding total of all digits to the power of length, comparing to input
        return True                                                # Function will output true
    else:
        return False                                               # Function will output false


number = input("Please input any number:\n")
if is_armstrong(number):                                           # if Function returns true
    print("Yes,", number, "is an Armstrong Number")
else:
    print('This is not an Armstrong Number')                       # if Function returns false
