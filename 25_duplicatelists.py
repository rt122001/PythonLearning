list1= [1,2,3,4,1,2,5,6]
duplicate= []

for i in range(len(list1)):
    for j in range(i):
        if list1[i]==list1[j]:
            duplicate.append(list1[i])

print(duplicate)