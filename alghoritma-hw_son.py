import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr_merge_time = []
arr_insert_time = []

for i in range(1, 1001, 1):
    arr = random.sample(range(1, 1001), i)
    
    start = time.time()
    merge_sort(arr)
    end = time.time()
    merge_time = round(end - start, 6)
    arr_merge_time.append(merge_time)

    start = time.time()
    insertion_sort(arr)
    end = time.time()
    insert_time = round(end - start, 6)
    arr_insert_time.append(insert_time)

intersection_index = next(idx for idx, (insert, merge) in enumerate(zip(arr_insert_time, arr_merge_time)) if abs(insert - merge) < 0.0001)

plt.plot(range(1, 1001, 1), arr_insert_time, color='red', label='Insertion Sort')
plt.plot(range(1, 1001, 1), arr_merge_time, color='blue', label='Merge Sort')
plt.scatter([intersection_index + 1], [arr_insert_time[intersection_index]], color='green', label='Intersection')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Merge Sort (blue) vs Insertion Sort (red) with Intersection Point')
plt.legend()
plt.show()