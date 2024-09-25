def bucketsort(a, n):
    max_val = max(a)
    b = [0] * (max_val + 1)
    for i in range(n):
        b[a[i]] += 1
    j = 0
    for i in range(max_val + 1):
        while b[i] > 0:
            a[j] = i
            j += 1
            b[i] -= 1
a = [12, 45, 33, 87, 56, 9, 11, 7, 67]
n = len(a)
print("Before sorting array elements are: ")
print(a)
bucketsort(a, n)
print("\nAfter sorting array elements are: ")
print(a)