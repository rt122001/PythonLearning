import math
bin =  int(input("Enter the binary number: "))
numarr = []
initialbin=bin

while bin > 0:
    dig = bin % 10
    numarr.append(dig)
    bin = math.floor(bin/10)

dec = 0
power = 0
for i in numarr:
    dec = dec + i * (2 ** power)
    power = power + 1

print(dec)