import random
import time


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        pivot_idx = partition(arr, low, high)

        if pivot_idx - 1 > low:
            stack.append((low, pivot_idx - 1))
        if pivot_idx + 1 < high:
            stack.append((pivot_idx + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


def generate_random_array(n):
    return [random.randint(1, n) for _ in range(n)]


def generate_increasing_array(n):
    return [i + 1 for i in range(n)]


def run_tests():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    random_time_ss = []
    random_time_is = []
    random_time_bs = []
    random_time_hs = []
    random_time_ms = []
    random_time_qs = []
    counting_time_cs_large = []
    counting_time_cs_small = []

    for n in sizes:
        arr = generate_random_array(n)

        # Sortowanie przez proste wybieranie
        random_time_ss.append(measure_time(selection_sort, arr.copy()))

        # Sortowanie przez proste wstawianie
        random_time_is.append(measure_time(insertion_sort, arr.copy()))

        # Sortowanie bąbelkowe
        random_time_bs.append(measure_time(bubble_sort, arr.copy()))

        # Sortowanie stogowe
        random_time_hs.append(measure_time(heap_sort, arr.copy()))

        # Sortowanie przez scalanie
        random_time_ms.append(measure_time(merge_sort, arr.copy()))

        # Sortowanie szybkie (wersja iteracyjna)
        random_time_qs.append(measure_time(quicksort, arr.copy()))

        # Sortowanie przez zliczanie (duży zakres)
        counting_time_cs_large.append(measure_time(counting_sort, arr.copy()))

        # Sortowanie przez zliczanie (mały zakres)
        counting_time_cs_small.append(measure_time(counting_sort, arr.copy()))

    print("Wyniki sortowania przez proste wybieranie:")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_ss[i]}")

    print("\nWyniki sortowania przez proste wstawianie:")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_is[i]}")

    print("\nWyniki sortowania bąbelkowego:")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_bs[i]}")

    print("\nWyniki sortowania stogowego:")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_hs[i]}")

    print("\nWyniki sortowania przez scalanie:")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_ms[i]}")

    print("\nWyniki sortowania szybkiego (wersja iteracyjna):")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{random_time_qs[i]}")

    print("\nWyniki sortowania przez zliczanie (duży zakres):")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{counting_time_cs_large[i]}")

    print("\nWyniki sortowania przez zliczanie (mały zakres):")
    print("n\tCzas")
    for i, n in enumerate(sizes):
        print(f"{n}\t{counting_time_cs_small[i]}")

run_tests()