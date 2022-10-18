# Counting sort algorithm can be used to sort non-negative integers between a specific range. This post covers a variation of counting sort that can work on negative numbers and can sort numbers in any range. But this version doesn’t produce a stable sort, i.e., the relative order of items with equal keys is not preserved anymore and runs in O(n.log(n)) time, where n is the total number of elements in the input collection.
# The idea remains the same – iterate over the collection and construct a map storing information about the total number of times each key occurs within the input collection. Then loop over the collection again and then use those counts to determine each key value’s final positions in the collection. This takes advantage of the fact that a map is sorted according to the keys’ natural order (ascending order).
# Following is the Python implementation of count sort that takes O(n) space:

def countSort(nums):
 
    # create a dictionary to store the frequency of list elements
    freq = {}
 
    # store distinct values in the input list as keys and
    # their respective counts as values in the dictionary
    for i in nums:
        freq[i] = freq.setdefault(i, 0) + 1
 
    # traverse the dictionary (based on the sorted order of keys) and
    # overwrite the input list with sorted elements
    i = 0
    for key, value in sorted(freq.items()):
        while value > 0:
            nums[i] = key
            value = value - 1
            i = i + 1
 
 
if __name__ == '__main__':
 
    nums = [4, 2, 1, 4, 1, 4, 2, 1, 10]
 
    countSort(nums)
    print(nums)