inputstring=input("Enter the string:")
reversestring = ''
liststring =  list(reversestring) # new

for i in range(0,len(inputstring)):
	liststring.append(inputstring[len(inputstring)-1-i]) #new

reversestring = ''.join(liststring) #new
print(reversestring)
