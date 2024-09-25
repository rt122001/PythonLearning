import math

num=int(input("Enter the number:"))
num1=0
num2=1
fib=0
if num <= 0 or math.isnan(num):
	print("No negative numbers/strings are allowed")
elif num == 1:
	fib = num1
	print(fib)
elif num == 2:
	fib = num2
	print(fib)
else:
	for i in range(2,num):
		fib=num2+num1
		print(fib)
		num1=num2
		num2=fib

print("Fibonacci of number %d is: %d"%(num,fib))
	
	

