arr = [64, 34, 25, 12, 22, 11, 90]
target = 22

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {target} not found in the array")
