num =  int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i ** 2

print("Sum of Squares till number {} is {}".format(num,sum))

