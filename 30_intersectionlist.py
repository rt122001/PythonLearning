list1=[1,2,3,4,5,6,7,8,9,10]
list2=[2,4,6,8,10,12,14,16,18,20]

setlist1= set(list1)
setlist2= set(list2)
intersectionset= setlist1.intersection(setlist2)

intersectionlist=list(intersectionset)
print(intersectionlist)
