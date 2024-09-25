

def common(list1,list2,commonel):
	for x in list1:
		for y in list2:
			if x==y:
				commonel.append(x)
	
	for x in commonel:
		print(x)

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[2,4,6,8,10,12,14,16,18,20]
commonel=[]

common(list1,list2,commonel)

