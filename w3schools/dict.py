thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)
if "model" in thisdict:
	print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict.update({"year": 2020})
print(thisdict)
thisdict["color"] = "red"
thisdict.update({"color2": "red"})
print(thisdict)

#remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#loop
for x in thisdict:
	print(x)
for x in thisdict:
	print(thisdict[x])
for x in thisdict:
	print(thisdict[x])
for x in thisdict.keys():
	print(x)
for x, y in thisdict.items():
	print(x, y)

mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)
