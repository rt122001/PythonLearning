inputstring=input("Enter the string:")
print(inputstring)

arraymax=len(inputstring)-1
for i in range(0,len(inputstring)):
	if inputstring[i] != inputstring[arraymax-i]:
		print("Not a palindrome!!")
		exit()
print("Palindrome!!")


	
	
