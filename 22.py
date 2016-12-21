'''
22. Generate Parentheses 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
                
        def dfs(num, strs, sum, res):
            if num == length and sum == 0:
                res.append(strs)
                return
            if sum < 0 or sum > length/2 or num > length:
                return
            for letter in [1,-1]:
                dfs(num+1, strs+dict[letter], sum+letter, res)
        
        dict = { 1:'(',
                -1:')'}
        res = []
        length = n*2
        if length == 0:
            return res
        
        dfs(0, '', 0, res)
        return res
