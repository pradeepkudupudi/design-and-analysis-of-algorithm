arr = [38, 27, 43, 3, 9, 82, 10]

stack = [(0, len(arr) - 1)]

while stack:
    low, high = stack.pop()
    if low < high:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stack.append((low, i))
        stack.append((i + 2, high))

print(f"Sorted array: {arr}")
