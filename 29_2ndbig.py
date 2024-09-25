list1= [1,2,3,5,7,9,10,11]

max1=list1[0]
max2=list1[0]

for item in list1:
    if item > max1:
        max1= item

for item in list1:
    if item > max2 and item!=max1:
        max2= item

print(max2)