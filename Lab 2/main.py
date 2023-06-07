import time
import random
import bisect
from tabulate import tabulate

# Generowanie tablicy A
def generate_array(n):
    A = []
    numbers = set()

    while len(A) < n:
        num = random.randint(1, 2*n)  # Zakres losowanych liczb
        if num not in numbers:
            A.append(num)
            numbers.add(num)
    return A


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Wyszukiwanie w tablicy A (statycznej implementacji listy)
def search_array(A, B):
    start_time = time.time()
    for x in B:
        if x in A:
            found = True
        else:
            found = False
    end_time = time.time()
    search_time = end_time - start_time
    return search_time

# Wyszukiwanie binarne w posortowanej tablicy B
def binary_search_array(B, A):
    start_time = time.time()
    for x in A:
        index = bisect.bisect_left(B, x)
        if index != len(B) and B[index] == x:
            found = True
        else:
            found = False
    end_time = time.time()
    search_time = end_time - start_time
    return search_time

# Implementacja drzewa BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and value < root.left.value:
        return rotate_right(root)
    if balance < -1 and value > root.right.value:
        return rotate_left(root)
    if balance > 1 and value > root.left.value:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and value < root.right.value:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

def create_bst(A):
    root = None
    for value in A:
        root = insert(root, value)
    return root

def get_height(root):
    if root is None:
        return 0
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1

def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def rotate_left(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def rotate_right(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def measure_search_time(A, root):
    start_time = time.time()
    for value in A:
        search(root, value)
    end_time = time.time()
    search_time = end_time - start_time
    return search_time

# Testowanie zależności
num_elements = [1000, 3000, 5000, 7000, 10000, 12000, 15000, 18000, 20000]

table_data = []

for n in num_elements:
    # Generowanie tablicy A
    A = generate_array(n)

    # Tworzenie kopii i sortowanie tablicy B
    start_time = time.time()
    B = quicksort(A.copy())
    cb_time = time.time() - start_time

    # Tworzenie drzewa BST z elementami tablicy A
    start_time1 = time.time()
    TA = create_bst(A)
    CTA = time.time() - start_time

    # Tworzenie drzewa BST z elementami tablicy B
    start_time2 = time.time()
    TB = create_bst(B)
    CTB = time.time() - start_time2

    # Obliczanie wysokości drzewa TA
    hTA = get_height(TA)

    # Obliczanie wysokości drzewa TB
    hTB = get_height(TB)

    # Wyszukiwanie w tablicy A
    SA = search_array(A, B)

    # Wyszukiwanie binarne w tablicy B
    SB = binary_search_array(B, A)

    #Wyszukiwanie w drzewie
    STA = measure_search_time(A, TA)

    #Wyszukiwanie w drzewie
    STB = measure_search_time(A, TB)

    # Zapisywanie danych w tabeli
    table_data.append([n, cb_time, CTA, CTB, hTA, hTB, SA, SB, STA, STB])

# Tworzenie tabeli
table_headers = ['Liczba elementów (n)', 'CB', 'CTA', 'CTB', 'hTA', 'hTB', 'SA', 'SB', 'STA', 'STB']
table = tabulate(table_data, headers=table_headers)
print(table)
