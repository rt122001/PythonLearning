import random

list1=[]
for x in range(0,10):
	num=random.randint(0,50)
	list1.append(num)

print("List1:",list1)
list1.sort()
print("Sorted List:",list1)
