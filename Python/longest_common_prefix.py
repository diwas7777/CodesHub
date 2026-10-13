def longestCommonPrefix(strs: list[str]):
#=======================================================================#
#   This function return the longsest common prefix within an array of string
#
#    :type strs: List[str]
#    :rtype: str
#=======================================================================#
    prefix = "" # create empty var for return string
    for char in zip(*strs): # open each word in the list -> ['f' , 'f', 'f'] for the first iteration 
        if len(set(char)) > 1: # set is only returning the total of unique value of that string, so this will act as validator
            break # if there a list that contains more than 1 unique value within the list, stop the loop
        prefix += char[0] # store the first value of each list combination that pass the validation test
    return ("" if not strs else prefix)

if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["a"]))