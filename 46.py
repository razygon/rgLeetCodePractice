'''
46. Permutations 
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.length = len(nums)
        if self.length == 0:
            return res
        self.dfs(nums, [], res)
        return res
        
    def dfs(self,nnums, per, res):
       # print per
        if len(per) == self.length:
            res.append(per)
            return
       # print nnums
        for item in nnums:
            nnnums = list(nnums)
            nnnums.remove(item)
            self.dfs(nnnums, per+[item], res)
        
        
