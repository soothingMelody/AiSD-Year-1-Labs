import random
import time

class Package:
    def __init__(self, weight, reward):
        self.weight = weight
        self.reward = reward

# Dynamic Programming (PD) with Memoization
def dynamic_programming(packages, capacity, memo={}):
    if capacity in memo:
        return memo[capacity]

    if len(packages) == 0 or capacity == 0:
        return 0

    if packages[0].weight > capacity:
        memo[capacity] = dynamic_programming(packages[1:], capacity, memo)
        return memo[capacity]

    included = packages[0].reward + dynamic_programming(packages[1:], capacity - packages[0].weight, memo)
    not_included = dynamic_programming(packages[1:], capacity, memo)
    memo[capacity] = max(included, not_included)
    return memo[capacity]

# Brute Force (BF1) with Pruning Techniques
def brute_force(packages, capacity):
    def explore_combinations(index, current_weight, current_reward):
        nonlocal max_reward

        if current_weight > capacity:
            return

        if current_reward > max_reward:
            max_reward = current_reward

        if index >= len(packages):
            return

        package = packages[index]
        explore_combinations(index + 1, current_weight + package.weight, current_reward + package.reward)
        explore_combinations(index + 1, current_weight, current_reward)

    max_reward = 0
    explore_combinations(0, 0, 0)
    return max_reward

# Brute Force with Elimination (BF2) with Preprocessing
def brute_force_elimination(packages, capacity):
    def explore_combinations(index, current_weight, current_reward):
        nonlocal max_reward

        if current_weight > capacity:
            return

        if current_reward > max_reward:
            max_reward = current_reward

        if index >= len(valid_packages):
            return

        package = valid_packages[index]
        explore_combinations(index + 1, current_weight + package.weight, current_reward + package.reward)
        explore_combinations(index + 1, current_weight, current_reward)

    valid_packages = [package for package in packages if package.weight <= capacity]
    max_reward = 0
    explore_combinations(0, 0, 0)
    return max_reward

# Heuristic GH4 with Sorting
def heuristic_max_ratio(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.reward / p.weight, reverse=True)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

# Measure Execution Time
def measure_execution_time(packages, method):
    start_time = time.time()
    capacity = sum(package.weight for package in packages) * 0.25
    if method == "PD":
        dynamic_programming(packages, capacity)
    elif method == "BF1":
        brute_force(packages, capacity)
    elif method == "BF2":
        brute_force_elimination(packages, capacity)
    elif method == "GH4":
        heuristic_max_ratio(packages, capacity)

    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Constants and Parameters
num_measurements = 1
n_values = [10, 13, 15, 16, 18, 20, 21, 22, 24, 25]
min_weight = 10
max_weight = 1000
min_reward = 100
max_reward = 10000

# Perform Measurements
results = {
    "PD": [],
    "BF1": [],
    "BF2": [],
    "GH4": []
}

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

# Display Results
print("Liczba paczek\tPD\tBF1\tBF2\tGH4")
print("--------------------------------")
for i in range(len(n_values)):
    n = n_values[i]
    pd_time = results["PD"][i]
    bf1_time = results["BF1"][i]
    bf2_time = results["BF2"][i]
    gh4_time = results["GH4"][i]
    print(f"{n}\t\t{pd_time:.9f}\t{bf1_time:.9f}\t{bf2_time:.9f}\t{gh4_time:.9f}")
