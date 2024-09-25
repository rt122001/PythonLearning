def fact(num):
    facto = 1
    if num > 0:
        facto = num * fact(num-1)
    return facto

num = int(input("Enter the number: "))
factorial=fact(num)
print(factorial)

def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)

num = 7  # You can change this value to compute the factorial for a different number
print(recur_factorial(num))