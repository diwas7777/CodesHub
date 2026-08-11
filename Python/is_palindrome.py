class Solution(object):
    def isPalindrome(self, x): #? is there different approach such not converting the int first to speed up the runtime ?
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)  # change input type to string
        reversed = x[::-1] # reverse the string
        
        return (True if reversed == x else False)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))