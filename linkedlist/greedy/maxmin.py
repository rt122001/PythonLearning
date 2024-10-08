def max_min_divide_conquer(arr, low, high):
    # Structure to store both maximum and minimum elements
    class Pair:
        def __init__(self):
            self.max = 0
            self.min = 0
    result = Pair()
    # If only one element in the array
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result
    # If there are two elements in the array
    if high == low + 1:
        if arr[low] < arr[high]:
            result.min = arr[low]
            result.max = arr[high]
        else:
            result.min = arr[high]
            result.max = arr[low]
        return result
    # If there are more than two elements in the array
    mid = (low + high) // 2
    left = max_min_divide_conquer(arr, low, mid)
    right = max_min_divide_conquer(arr, mid + 1, high)
    # Compare and get the maximum of both parts
    result.max = max(left.max, right.max)
    # Compare and get the minimum of both parts
    result.min = min(left.min, right.min)
    return result
arr = [6, 4, 26, 14, 33, 64, 46]
result = max_min_divide_conquer(arr, 0, len(arr) - 1)
print("Maximum element is:", result.max)
print("Minimum element is:", result.min)