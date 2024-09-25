def countsort(a, pos):
   n = len(a)
   output = [0] * n
   count = [0] * 10
   for i in range(0, n):
      idx = a[i] // pos
      count[idx % 10] += 1
   for i in range(1, 10):
      count[i] += count[i - 1]
   i = n - 1
   while i >= 0:
      idx = a[i] // pos
      output[count[idx % 10] - 1] = a[i]
      count[idx % 10] -= 1
      i -= 1
   for i in range(0, n):
      a[i] = output[i]

def radixsort(a):
   maximum = max(a)
   pos = 1
   while maximum // pos > 0:
      countsort(a, pos)
      pos *= 10
      
a = [236, 15, 333, 27, 9, 108, 76, 498]
print("Before sorting array elements are: ")
print (a)
radixsort(a)
print("After sorting array elements are: ")
print (a)