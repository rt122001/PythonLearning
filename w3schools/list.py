list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]

print(list1)

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
	print("Yes, apple is in thislist")
#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)

#traverse
thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print(x)

thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
	print(thislist[x])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
	print(thislist[i])
	i = i + 1

#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#append
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

