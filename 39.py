'''
39. Combination Sum   
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = list(set(candidates))
        candidates.sort()
        self.res = []
        self.length = len(candidates)
        self.dfs(target,candidates,0,[])
        
        return self.res
        
    def dfs(self,target,candidates,start,comlist):
        if target == 0:
            self.res.append(comlist)
            return 
        for j in range(start,self.length):
            #print "can:", candidates
            if target < candidates[j]:
                return
            self.dfs(target - candidates[j],candidates, j, comlist + [candidates[j]])
