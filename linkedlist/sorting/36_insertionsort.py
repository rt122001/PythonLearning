#reversebubble
arr= [1,10,2,5,9,55,23,11,43,4]
count=len(arr)-1

i=0
j=count
while i<count:
    j=i#insert index
    while j>0:
        if arr[j+1]<arr[j]:
            tmp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=tmp
        j=j-1
    i=i+1

print(arr)

def insertion_sort(array, size):
   for i in range(1, size):
      key = array[i]
      j = i
      while (j > 0) and (array[j-1] > key):
         array[j] = array[j-1]
         j = j-1
      array[j] = key
      
arr = [67, 44, 82, 17, 20]
n = len(arr)
print("Array before Sorting: ")
print(arr)
insertion_sort(arr, n)
print("Array after Sorting: ")
print(arr)