import random
import time

def count_sort(arr, min_val, max_val):
    min_val = min(arr)
    max_val = max(arr)

    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

def measure_time(arr, sort_func, low, high):
    start_time = time.time()
    sort_func(arr, low, high)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def generate_random_array(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

def run_experiment(n_values):
    print("n\t\tTime CS [1, 100*n]\tTime QS [1, 100*n]\tTime CS [1, 0.01*n]\tTime QS [1, 0.01*n]")
    print("-" * 85)
    for n in n_values:
        arr_a = [random.randint(1, 100 * n) for _ in range(n)]
        arr_b = [random.randint(1, int(0.01 * n)) for _ in range(n)]

        time_cs_a = measure_time(arr_a.copy(), count_sort, 0, n - 1)
        time_qs_a = measure_time(arr_a.copy(), quicksort, 0, n - 1)
        time_cs_b = measure_time(arr_b.copy(), count_sort, 0, n - 1)
        time_qs_b = measure_time(arr_b.copy(), quicksort, 0, n - 1)

        print(f"{n}\t\t{time_cs_a:.3f} s\t\t\t{time_qs_a:.3f} s\t\t\t{time_cs_b:.3f} s\t\t\t{time_qs_b:.3f} s")

# Example usage
n_values = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]

run_experiment(n_values)

