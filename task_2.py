def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = "No upper bound found"

    return (iterations, upper_bound)


# Examples

print("Example 1:")
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 3.3
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}") # Виведе: Iterations: 1, Upper bound: 3.3

print("\nExample 2:")
arr = [10.0, 20.0, 30.0, 40.0, 50.0]
target = 35.0
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}") # Виведе: Iterations: 2, Upper bound: 40.0

print("\nExample 3:")
arr = [-10.0, -5.0, 0.0, 5.0, 10.0]
target = -7.0
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}") # Виведе: Iterations: 3, Upper bound: -5.0