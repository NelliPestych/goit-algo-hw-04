import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Wrapper for Timsort (Python's built-in sorted function)
def timsort(arr):
    return sorted(arr)

# Function to generate random arrays
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Function to test sorting algorithms
def test_sorting_algorithm(algorithm, data):
    return timeit.timeit(lambda: algorithm(data.copy()), number=1)

# Test arrays of different sizes
sizes = [1000, 5000, 10000]
results = []

for size in sizes:
    random_array = generate_random_array(size)
    reverse_sorted_array = sorted(random_array, reverse=True)
    sorted_array = sorted(random_array)

    for array_type, array in [("random", random_array), ("sorted", sorted_array), ("reverse sorted", reverse_sorted_array)]:
        result = {
            "size": size,
            "type": array_type,
            "merge_sort": test_sorting_algorithm(merge_sort, array),
            "insertion_sort": test_sorting_algorithm(insertion_sort, array),
            "timsort": test_sorting_algorithm(timsort, array)
        }
        results.append(result)

for result in results:
    print(result)
