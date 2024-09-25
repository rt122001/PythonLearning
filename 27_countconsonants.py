inputstring=input("Enter the string:")
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

count = 0

for i in range(0,len(inputstring)):
	for j in range(0,len(consonants)):
		if inputstring[i] == consonants[j]:
			count = count + 1

print(count)
