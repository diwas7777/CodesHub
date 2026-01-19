class Solution:
    def selectionSort(self, arr):
        """
        Performs Selection Sort on the given list.

        Selection Sort works by repeatedly finding the minimum element
        from the unsorted part of the list and placing it at the beginning.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        n = len(arr)

        # Traverse through the array except the last element
        for i in range(n - 1):
            # Assume the current index has the minimum element
            min_idx = i

            # Find the minimum element in the remaining unsorted array
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # Swap the found minimum element with the first element
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr
