def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (last - first) // 2 + first
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def testing(target):
    if target is not None:
        print("Target found index :", target+1)
    else:
        print("Target not found")


test_1 = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
test_2 = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 11)
testing(test_1)
testing(test_2)
