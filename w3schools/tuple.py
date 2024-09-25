thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
	print("Yes, 'apple' is in the fruits tuple")

#change tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)  

#add values
thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist.append("orange")
thistuple = tuple(thislist)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#unpack
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print(fruits)

#loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
	print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
	print(thistuple[i])
	
	
#join
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
