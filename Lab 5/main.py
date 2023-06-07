import random
import time
class Package:
    def __init__(self, weight, reward):
        self.weight = weight
        self.reward = reward

def dynamic_programming(packages, capacity):
    n = len(packages)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if packages[i - 1].weight <= j:
                dp[i][j] = max(dp[i - 1][j], packages[i - 1].reward + dp[i - 1][j - packages[i - 1].weight])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_packages = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_packages.append(packages[i - 1])
            j -= packages[i - 1].weight

    return selected_packages[::-1]

def brute_force(packages, capacity, eliminate_invalid=False):
    n = len(packages)
    max_profit = 0
    selected_packages = []

    for i in range(1, 2**n):
        current_weight = 0
        current_profit = 0
        current_packages = []

        for j in range(n):
            if (i >> j) & 1:
                current_weight += packages[j].weight
                current_profit += packages[j].reward
                current_packages.append(packages[j])

        if current_weight <= capacity and current_profit > max_profit:
            if eliminate_invalid:
                max_profit = current_profit
                selected_packages = current_packages
            else:
                max_profit = current_profit
                selected_packages = current_packages

    return selected_packages

def heuristic_random(packages, capacity):
    random.shuffle(packages)
    selected_packages = []
    current_weight = 0

    for package in packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

def heuristic_min_weight(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.weight)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

def heuristic_max_reward(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.reward, reverse=True)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

def heuristic_max_ratio(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.reward / p.weight, reverse=True)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages


def measure_execution_time(packages, method):
    start_time = time.time()

    if method == "PD":
        capacity = sum(package.weight for package in packages) // 2
        dynamic_programming(packages, capacity)
    elif method == "BF1":
        capacity = sum(package.weight for package in packages) // 2
        brute_force(packages, capacity)
    elif method == "BF2":
        capacity = sum(package.weight for package in packages) // 2
        brute_force(packages, capacity, eliminate_invalid=True)
    elif method == "GH4":
        capacity = sum(package.weight for package in packages) // 2
        heuristic_max_ratio(packages, capacity)

    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Generowanie danych wejściowych
#n = 20   # Liczba paczek
num_measurements = 1
n_values = [5, 8, 10, 13, 15, 18, 20, 22, 25, 28]
min_weight = 10
max_weight = 1000
min_reward = 100
max_reward = 10000

results = {
    "PD": [],
    "BF1": [],
    "BF2": [],
    "GH4": []
}

#capacity = random.randint(n * min_weight, n * max_weight)  # Dopuszczalna ładowność samochodu

# # Wybór paczek przy użyciu różnych strategii
# selected_packages_dp = dynamic_programming(packages, capacity)
# selected_packages_bf1 = brute_force(packages, capacity)
# selected_packages_bf2 = brute_force(packages, capacity, eliminate_invalid=True)
# selected_packages_gh1 = heuristic_random(packages, capacity)
# selected_packages_gh2 = heuristic_min_weight(packages, capacity)
# selected_packages_gh3 = heuristic_max_reward(packages, capacity)
# selected_packages_gh4 = heuristic_max_ratio(packages, capacity)
#
# # Wyświetlanie wyników
# print("Paczki (programowanie dynamiczne):")
# for package in selected_packages_dp:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (pełny przegląd - BF1):")
# for package in selected_packages_bf1:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (pełny przegląd - BF2):")
# for package in selected_packages_bf2:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (heurystyka - losowa):")
# for package in selected_packages_gh1:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (heurystyka - min{s(ai)}):")
# for package in selected_packages_gh2:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (heurystyka - max{w(ai)}):")
# for package in selected_packages_gh3:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")
# print()
#
# print("Paczki (heurystyka - max{w(ai)/s(ai)}):")
# for package in selected_packages_gh4:
#     print(f"Waga: {package.weight}, Wynagrodzenie: {package.reward}")

# Pomiar czasu dla poszczególnych metod
for n in n_values:
    packages = []
    for _ in range(n):
        weight = random.randint(min_weight, max_weight)
        reward = random.randint(min_reward, max_reward)
        packages.append(Package(weight, reward))

    pd_times = []
    bf1_times = []
    bf2_times = []
    gh4_times = []

    for _ in range(num_measurements):
        pd_time = measure_execution_time(packages, "PD")
        pd_times.append(pd_time)

        bf1_time = measure_execution_time(packages, "BF1")
        bf1_times.append(bf1_time)

        bf2_time = measure_execution_time(packages, "BF2")
        bf2_times.append(bf2_time)

        gh4_time = measure_execution_time(packages, "GH4")
        gh4_times.append(gh4_time)

    results["PD"].append(sum(pd_times) / num_measurements)
    results["BF1"].append(sum(bf1_times) / num_measurements)
    results["BF2"].append(sum(bf2_times) / num_measurements)
    results["GH4"].append(sum(gh4_times) / num_measurements)

# Wyświetlanie tabeli wyników czasowych
print("Liczba paczek\tPD\tBF1\tBF2\tGH4")
print("--------------------------------")
for i in range(len(n_values)):
    n = n_values[i]
    pd_time = results["PD"][i]
    bf1_time = results["BF1"][i]
    bf2_time = results["BF2"][i]
    gh4_time = results["GH4"][i]
    print(f"{n}\t\t{pd_time:.6f}\t{bf1_time:.6f}\t{bf2_time:.6f}\t{gh4_time:.6f}")