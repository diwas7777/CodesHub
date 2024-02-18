import time
import random


def decorated_function(func):
    """Function to time the sorting algorithms"""
    def wrapper_function(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__} is {end - begin}")
        return result
    return wrapper_function


@decorated_function
def selection_sort(arr):
    for idx in range(len(arr) - 1):
        jdx = idx + 1

        while jdx < len(arr):
            if arr[idx] > arr[jdx]:
                arr[idx], arr[jdx] = arr[jdx], arr[idx]
            jdx += 1
    return arr


@decorated_function
def bubble_sort(arr):
    for first in range(len(arr) - 1):
        swapped = False
        for second in range(0, len(arr) - first - 1):
            if arr[second] > arr[second + 1]:
                arr[second], arr[second + 1] = arr[second + 1], arr[second]
                swapped = True

        if not swapped:
            return arr
        

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def quick_sort(arr, low, high):
    if low < high:
        pivot = quicksort_partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def quicksort_partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j


@decorated_function
def time_merge_sort(arr):
    """Times the merge sort algorithm"""
    return merge_sort(arr)


@decorated_function
def time_quick_sort(arr, low, high):
    """Times the quick sort algorithm"""
    return quick_sort(arr, low, high)


@decorated_function
def time_default_sorted(arr):
    """Times default sorting algorithm"""
    arr = sorted(arr)


array = [random.randint(-5000, 5000) for _ in range(10000)]
bubble_sort(array)
selection_sort(array)
time_merge_sort(array)
time_quick_sort(array, 0, len(array) - 1)
time_default_sorted(array)
