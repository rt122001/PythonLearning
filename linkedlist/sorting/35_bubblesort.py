arr= [1,10,2,5,9,55,23,11,43,4]

i=len(arr)
j=0

while (i>0):
    while j<i-1:
        if arr[j+1] < arr[j]:
            tmp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=tmp
        j=j+1
    j=0
    i=i-1

print(arr)