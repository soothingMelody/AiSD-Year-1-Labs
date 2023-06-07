import random

class Package:
    def __init__(self, weight, reward):
        self.weight = weight
        self.reward = reward

# Dynamic Programming (PD) with Memoization
def dynamic_programming(packages, capacity, memo={}):
    if capacity in memo:
        return memo[capacity]

    if len(packages) == 0 or capacity == 0:
        return []

    if packages[0].weight > capacity:
        memo[capacity] = dynamic_programming(packages[1:], capacity, memo)
        return memo[capacity]

    included = [packages[0]] + dynamic_programming(packages[1:], capacity - packages[0].weight, memo)
    not_included = dynamic_programming(packages[1:], capacity, memo)

    if sum(package.reward for package in included) > sum(package.reward for package in not_included):
        memo[capacity] = included
    else:
        memo[capacity] = not_included

    return memo[capacity]

# Heuristic GH1 with Random Selection
def heuristic_random(packages, capacity):
    selected_packages = []

    while capacity > 0 and len(packages) > 0:
        package = random.choice(packages)
        if package.weight <= capacity:
            selected_packages.append(package)
            capacity -= package.weight
        packages.remove(package)

    return selected_packages

# Heuristic GH2 with Minimum Weight Selection
def heuristic_min_weight(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.weight)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

# Heuristic GH3 with Maximum Reward Selection
def heuristic_max_reward(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.reward, reverse=True)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

# Heuristic GH4 with Maximum Weight-to-Reward Ratio Selection
def heuristic_max_ratio(packages, capacity):
    sorted_packages = sorted(packages, key=lambda p: p.weight / p.reward, reverse=True)
    selected_packages = []
    current_weight = 0

    for package in sorted_packages:
        if current_weight + package.weight <= capacity:
            selected_packages.append(package)
            current_weight += package.weight

    return selected_packages

# Measure Average Error
def measure_average_error(packages, method_pd, method_gh, b):
    pd_solution = method_pd(packages, sum(package.weight for package in packages) * b)
    gh_solution = method_gh(packages, sum(package.weight for package in packages) * b)
    error_sum = 0

    pd_reward = sum(package.reward for package in pd_solution)
    gh_reward = sum(package.reward for package in gh_solution)

    if pd_reward == 0:
        average_error = 0
    else:
        average_error = abs(pd_reward - gh_reward) / pd_reward * 100

    return average_error

# Constants and Parameters
num_measurements = 10
n = 50
b_values = [0.25, 0.5, 0.75]
min_weight = 10
max_weight = 1000
min_reward = 1
max_reward = 100

results = []

# Perform Measurements
for b in b_values:
    pd_errors = []
    gh1_errors = []
    gh2_errors = []
    gh3_errors = []
    gh4_errors = []

    for _ in range(num_measurements):
        packages = []
        for _ in range(n):
            weight = random.randint(min_weight, max_weight)
            reward = random.randint(min_reward, max_reward)
            packages.append(Package(weight, reward))

        pd_errors.append(measure_average_error(packages, dynamic_programming, heuristic_max_ratio, b))
        gh1_errors.append(measure_average_error(packages, dynamic_programming, heuristic_random, b))
        gh2_errors.append(measure_average_error(packages, dynamic_programming, heuristic_min_weight, b))
        gh3_errors.append(measure_average_error(packages, dynamic_programming, heuristic_max_reward, b))
        gh4_errors.append(measure_average_error(packages, dynamic_programming, heuristic_max_ratio, b))

    average_pd_error = sum(pd_errors) / len(pd_errors)
    average_gh1_error = sum(gh1_errors) / len(gh1_errors)
    average_gh2_error = sum(gh2_errors) / len(gh2_errors)
    average_gh3_error = sum(gh3_errors) / len(gh3_errors)
    average_gh4_error = sum(gh4_errors) / len(gh4_errors)

    results.append((b, average_pd_error, average_gh1_error, average_gh2_error, average_gh3_error, average_gh4_error))

# Print Results
print("b\t\tAverage PD Error\tAverage GH1 Error\tAverage GH2 Error\tAverage GH3 Error\tAverage GH4 Error")
print("---------------------------------------------------------------------------------------------------")

for result in results:
    b, average_pd_error, average_gh1_error, average_gh2_error, average_gh3_error, average_gh4_error = result
    print(f"{b}\t\t{average_pd_error:.6f}\t\t\t{average_gh1_error:.6f}\t\t\t{average_gh2_error:.6f}\t\t\t{average_gh3_error:.6f}\t\t\t{average_gh4_error:.6f}")
