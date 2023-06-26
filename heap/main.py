import heapq

# Creating a heap
heap = []  # Empty list to store the heap

# Inserting elements into the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

print("Heap after inserting elements:", heap)

# Accessing the smallest element in the heap
smallest = heap[0]
print("Smallest element in the heap:", smallest)

# Removing and returning the smallest element from the heap
smallest = heapq.heappop(heap)
print("Removed smallest element from the heap:", smallest)
print("Heap after removing smallest element:", heap)

# Creating a heap from a list of elements
numbers = [8, 3, 6, 4, 2, 9, 1]
heapq.heapify(numbers)
print("Heap created from a list:", numbers)

# Removing an element from the heap at a specific index
index_to_remove = 2
removed_element = heapq.heappop(numbers)
print("Removed element at index", index_to_remove, "from the heap:", removed_element)
print("Heap after removing element at index", index_to_remove, ":", numbers)

# Replacing an element in the heap with a new value
index_to_replace = 1
new_value = 5
heapq.heapreplace(numbers, new_value)
print("Heap after replacing element at index", index_to_replace, "with", new_value, ":", numbers)
