def partition(arr, low, high):
   i = low - 1
   print(i,low,high)
   pivot = arr[high]  # pivot element
   for j in range(low, high):
      if arr[j] <= pivot:
         # increment
         i = i + 1
         arr[i], arr[j] = arr[j], arr[i]
         print (i,j)
   arr[i + 1], arr[high] = arr[high], arr[i + 1]
   return i + 1

def quickSort(arr, low, high):
   if low < high:
      pi = partition(arr, low, high)
      quickSort(arr, low, pi - 1)
      quickSort(arr, pi + 1, high)

arr = [2, 5, 3, 8, 9, 6, 5, 4, 7]
n = len(arr)
print("Contents of the array: ")
for i in range(n):
   print(arr[i], end=" ")
quickSort(arr, 0, n - 1)
print("\nContents of the array after sorting: ")
for i in range(n):
   print(arr[i], end=" ")