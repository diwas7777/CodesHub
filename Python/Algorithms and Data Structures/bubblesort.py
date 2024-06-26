def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by detecting if any swaps were made
        swapped = False
        
        # Last i elements are already in place, so we don't need to compare them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                swapped = True  # Set the swapped flag to True
        
        # If no two elements were swapped in the inner loop, the list is sorted
        # and we can break out of the outer loop early
        if not swapped:
            break


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
