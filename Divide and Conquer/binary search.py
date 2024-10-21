arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
target = 10

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(f"Element {target} found at index {mid}")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"Element {target} not found in the array")
