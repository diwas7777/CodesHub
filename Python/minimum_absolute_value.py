def minimum_abs_value(arr: list[int]) -> list[int]:
#===================================================================================================#
#    This function return the number of ordered combination that return the smallest number in the array.
#    
#    :type arr: List[int]
#    :rtype: List[List[int]]
#===================================================================================================#
    
    arr.sort() # sort the array first, so we'll always have the smalles number at index 0
    abs_lowest = [] # plachoder to store the array combination
    min_diff = float('inf') # set default minimum number 
    
    for i in range(len(arr)-1): # looping entire array values  
        curr_dif = arr[i+1] - arr[i]  # get the current index 0 and 1 combination minus
        
        if curr_dif < min_diff: # if within the iteration we found the smaller number than min_diff
              min_diff = curr_dif # set the min_diff value to the curr_dif
              abs_lowest = [[arr[i], arr[i+1]]] # then create the pair value combination
              
        elif curr_dif == min_diff: # check if the curr_diff of iteration match the min_diff value
            abs_lowest.append([arr[i], arr[i+1]]) # if match, append the [a,b] to abs_lowest
    
    return abs_lowest
        
if __name__ == '__main__':
    print(minimum_abs_value([3,8,-10,23,19,-4,-14,27]))
    print(minimum_abs_value([1,3,6,10,15]))
    print(minimum_abs_value([40,11,26,27,-20]))