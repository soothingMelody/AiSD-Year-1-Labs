import random
import time


def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]


def generate_sorted_array(n):
    return [i for i in range(1, n + 1)]


def quicksort_pivot_first(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[low]
            i = low + 1
            j = high
            while i <= j:
                if arr[i] > pivot and arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                if arr[i] <= pivot:
                    i += 1
                if arr[j] >= pivot:
                    j -= 1
            arr[low], arr[j] = arr[j], arr[low]
            stack.append((low, j - 1))
            stack.append((j + 1, high))
    return arr


def quicksort_pivot_middle(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            mid = (low + high) // 2
            pivot = arr[mid]
            i = low
            j = high
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            stack.append((low, j))
            stack.append((i, high))
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


def measure_time_sorting(n, random_data=True):
    if random_data:
        data = generate_random_array(n)
    else:
        data = generate_sorted_array(n)

    start_time = time.time()
    sorted_data_qs_first = quicksort_pivot_first(data.copy())
    elapsed_time_qs_first = time.time() - start_time

    start_time = time.time()
    sorted_data_qs_middle = quicksort_pivot_middle(data.copy())
    elapsed_time_qs_middle = time.time() - start_time

    start_time = time.time()
    sorted_data_insertion = insertion_sort(data.copy())
    elapsed_time_insertion = time.time() - start_time

    return elapsed_time_qs_first, elapsed_time_qs_middle, elapsed_time_insertion


def generate_table(n_values, random_data=True):
    print("Tabela: Porównanie czasu obliczeń dla różnych metod sortowania")
    print(
        "| Liczba elementów (n) | QS (skrajny element) | QS (środkowy element) | Insertion Sort |")
    print(
        "|---------------------|------------------------------|-------------------------------|-------------------------|")

    for n in n_values:
        elapsed_time_qs_first, elapsed_time_qs_middle, elapsed_time_insertion = measure_time_sorting(n, random_data)

        row = "|{:>10d}".format(n) + " |{:>28.3f} s".format(elapsed_time_qs_first) + " |{:>29.3f} s".format(
            elapsed_time_qs_middle) + " |{:>23.3f} s".format(elapsed_time_insertion) + " |"
        print(row)


# Przykładowe użycie:
n_values = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]
generate_table(n_values, random_data=False)