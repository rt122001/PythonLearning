import math
num =  int(input("Enter the number: "))
initialnum=num
numarr = []

while num > 0:
    dig = num % 10
    numarr.append(dig)
    num = math.floor(num/10)

n = len(numarr)
sum=0
for i in numarr:
    sum = sum + i ** n

if sum == initialnum:
    print("Armstrong Number.")
else:
    print("Not an Armstrong Number.")
