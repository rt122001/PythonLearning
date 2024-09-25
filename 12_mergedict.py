def mergedict(dict1,dict2):
	for x,y in dict2.items():
		dict1.update({x:y})
	print(dict1)
	
dict1={"name":"Rohit", "age":26}
dict2={"gender":"male", "place":"gurgaon"}

mergedict(dict1,dict2)
