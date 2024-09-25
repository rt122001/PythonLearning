inputstring=input("Enter the string:")
vowels=['a','e','i','o','u']

count = 0

for i in range(0,len(inputstring)):
	for j in range(0,len(vowels)):
		if inputstring[i] == vowels[j]:
			count = count + 1

print(count)
