number = input("Please input any number:\n")               # Asking for User to input a value to be checked
digits = [int(x) for x in str(number)]                     # Converting the input into a list
length = len(digits)                                       # Assigning constant "length" number of elements in the list.
total = 0                                                  # Variables must be defined
n = length                                                 # Similar to constant "length" but variable

if length == 1:
    print("All 1 digit numbers are Armstrong Numbers")
elif length == 2:
    print("No 2 digit numbers are Armstrong Numbers")
else:
    while n != 0:                                          # While loop for when n is not zero
        first = (digits[n - 1] ** length)                  # Working out each Exponent
        total += first                                     # Adding each exponent to the total
        n -= 1                                             # Subtracting from n moves to the next element in the list

    if total == int(number):
        print("Yes,", number, "is an Armstrong Number")
    else:
        print("This is not an Armstrong Number")
