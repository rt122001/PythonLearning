num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 1:"))

if num1>num2:
    dividend=num1
    divisor=num2
else:
    dividend=num2
    divisor=num1

while divisor>0:
    hcf=divisor
    divisor=dividend%divisor
    dividend=hcf

print("HCF is: ",hcf)
print("LCM is: ",(num1*num2)/hcf)