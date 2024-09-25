import math
num = int(input("Enter the number: "))
sum=0

while num > 0:
    dig = num % 10
    sum = sum + dig
    num = math.floor(num/10)

print(sum)