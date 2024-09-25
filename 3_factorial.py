num=int(input("Enter the number:"))
fact=1

for i in range(1,num):
	fact = fact*i
	
print("Factorial for number {} is: {}".format(num,fact))
print("Factorial for number %d is: %d"%(num,fact))
