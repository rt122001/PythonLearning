import math
dec =  int(input("Enter the Decimal number: "))
numarr = []
initialdec=dec

while dec > 0:
    dig = dec % 2
    numarr.append(dig)
    dec = math.floor(dec/2)

num = 0
power = 0
for i in numarr:
    num = num + i * (10 ** power)
    power = power + 1

print(num)