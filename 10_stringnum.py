import string
inputstring=input("Enter the string:")
liststring=list(inputstring)
strings=[]
numbers=[]

for i in range(0,len(liststring)):
	if liststring[i] in string.ascii_letters:
		strings.append(liststring[i])
	elif liststring[i] in string.digits:
		numbers.append(liststring[i])
	else:
		continue

print(strings)
print(numbers)
