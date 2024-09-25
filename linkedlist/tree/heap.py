#Python code for Max Heap Deletion Algorithm
class Heap:
    def __init__(self, capacity):
        self.array = [0] * capacity  #array to store heap elements
        self.capacity = capacity  #maximum capacity of the heap
        self.size = 0  #Current size of the heap
    # swap two elements in the heap
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
    # Heapify a subtree rooted at index i
    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # Check if the left child is larger than the root
        if left < self.size and self.array[left] > self.array[largest]:
            largest = left
        # Check if the right child is larger than the largest so far
        if right < self.size and self.array[right] > self.array[largest]:
            largest = right
        # If the largest is not the root, swap the root with the largest
        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)
    # insert a new element into the heap
    def insert(self, value):
        if self.size == self.capacity:
            print("Heap is full. Cannot insert more elements.")
            return
        # Insert the new element at the end
        i = self.size
        self.size += 1
        self.array[i] = value
        # Fix the heap property if it is violated
        while i != 0 and self.array[(i - 1) // 2] < self.array[i]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2
    # delete the maximum element from the heap
    def deleteMax(self):
        if self.size == 0:
            print("Heap is empty. Cannot extract maximum element.")
            return -1
        # store the root element
        max_value = self.array[0]
        # Replace the root with the last element
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        # Heapify the root
        self.heapify(0)
        return max_value
    # print the elements of the heap
    def printHeap(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()
    # deallocate memory occupied by the heap
    def destroyHeap(self):
        self.array = []
        self.size = 0
# Example usage of the heap
heap = Heap(10)
heap.insert(35)
heap.insert(33)
heap.insert(42)
heap.insert(10)
heap.insert(14)
heap.insert(19)
heap.insert(27)
heap.insert(44)
heap.insert(26)
heap.insert(31)
print("Heap elements before deletion:", end=" ")
heap.printHeap()
max_value = heap.deleteMax()
print("Maximum element:", max_value)
print("Heap elements after deletion:", end=" ")
heap.printHeap()
heap.destroyHeap()