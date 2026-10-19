# Student Information
LAST_NAME = "Magtalas"
STUDENT_ID = "TUPM-26-3606"
SEED_DIGIT = int(STUDENT_ID[-1])  # 6
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())

print("=== EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH ===")
# Generate unique sorted incident records, then rotate using SEED_DIGIT
original_records = [i * 10 for i in range(1, 11)]  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
rotation_point = SEED_DIGIT % len(original_records)
rotated_records = original_records[rotation_point:] + original_records[:rotation_point]

print(f"Original Records: {original_records}")
print(f"Rotated Records: {rotated_records}")

# Target incident generation
target_incident = rotated_ressed = ID_SUM + 10  # Example target
print(f"Target Incident: {target_incident}")

# Search in Rotated Array (Modified Binary Search) & count comparisons
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1, comparisons

pos, comp_rotated = search_rotated(rotated_records, target_incident)
# Linear search comparison
comp_linear = 0
lin_pos = -1
for i, val in enumerate(rotated_records):
    comp_linear += 1
    if val == target_incident:
        lin_pos = i
        break

print(f"Rotated Search Result -> Index: {pos}, Comparisons: {comp_rotated}")
print(f"Linear Search Comparisons: {comp_linear}")


print("\n=== EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS ===")
# Dataset A and Dataset B (sorted lists)
dataset_a = [i * 3 for i in range(1, 6)]  # [3, 6, 9, 12, 15]
dataset_b = [i * 4 for i in range(1, 6)]  # [4, 8, 12, 16, 20]

print(f"Dataset A: {dataset_a}")
print(f"Dataset B: {dataset_b}")

# Merge two sorted lists (Two-pointer approach)
def merge_sorted_lists(list1, list2):
    i = j = 0
    merged = []
    comparisons = 0
    while i < len(list1) and j < len(list2):
        comparisons += 1
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged, comparisons

consolidated_dataset, merge_comps = merge_sorted_lists(dataset_a, dataset_b)
print(f"Consolidated Dataset: {consolidated_dataset}")
print(f"Comparison Count: {merge_comps}")


print("\n=== EXERCISE 3: E-COMMERCE ORDER PROCESSING ===")
import time

sample_orders = [45, 12, 78, 23, 56, 89, 34]

def bubble_sort(arr):
    data = arr.copy()
    comps, swaps = 0, 0
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
    return data, comps, swaps

sorted_res, b_comps, b_swaps = bubble_sort(sample_orders)
print(f"Bubble Sort - Comparisons: {b_comps}, Swaps/Movements: {b_swaps}")
print(f"Sorted Orders Result: {sorted_res}")