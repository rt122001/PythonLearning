n=int(input("Enter the number of items in the list:"))
inputlist=[]
listsum=0

for i in range(0,n):
	element=int(input("Enter the elements of the list:"))
	inputlist.append(element)


listmin=inputlist[0]
listmax=inputlist[0]

for i in range(0,n):
	listsum = listsum + inputlist[i]
	if inputlist[i] < listmin:
		listmin=inputlist[i]
	if inputlist[i] > listmax:
		listmax=inputlist[i]
	
	
	
print(listsum)
avg=listsum/n
print(avg)
print(listmin)
print(listmax)


