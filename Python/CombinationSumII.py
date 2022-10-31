# Problem Statement:
# Given a collection/list of conadidate numbers(candidates) and a target number(target) find all unique
# combinations in candidates where the sum of candidate numbers in equal to target.
# Each number from the candidates may be used only once in one combination.

# Sample Input:
# candidates = [2,5,2,1,2], target = 5

# Sample Output:
# [ [1,2,2],[ 5 ] ]
]
# In the solution I have taken a sample input. You can choose any input.
class Solution:
  def combinationSum2(self, candidates, target):
    candidates.sort()
    res=set()
    self.findcombination(candidates,target,[],res)
    return [list(i) for i in res]
 
  def findcombination(self,candidates,target,ls,res):
    if target==0:
      res.add(tuple(ls))
      return
    if target<0:
      return
    for i in range(len(candidates)):
      if target<candidates[i]: return
      self.findcombination(candidates[i+1:],target-candidates[i],ls+[candidates[i]],res)
 
test=Solution()
print(test.combinationSum2([10,1,2,7,6,1,5],8))