# Python program for Recursion Data Structure
def factorial(n):
    #Base Case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply n with factorial of (n-1)
    return n * factorial(n - 1)
#Case 1:
number = 6;
print("Number is: ", number);
#Case 2:
if number < 0:
    print("Error: Factorial is undefined for negative numbers.")
else:
    result = factorial(number)
    # print the output
    print("Factorial of", number, "is: ", result)