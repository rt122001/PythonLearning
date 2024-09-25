output = []
def counting_sort(a, n):
    output = [0] * n
    c = [0] * 100
    for i in range(100):
        c[i] = 0
    for j in range(n):
        c[a[j]] += 1
    for i in range(1, 99):
        c[i] += c[i-1]
    for j in range(n-1, -1, -1):
        output[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1
    print("After sorting array elements are: ")
    print(output)
a = [12, 32, 44, 8, 16]
n = len(a)
print("Before sorting array elements are: ")
print (a)
counting_sort(a, n)