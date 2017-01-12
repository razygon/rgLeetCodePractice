'''
49. Group Anagrams   
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for str in strs:
            slist = ''.join(sorted(str))
            if slist in ans:
                ans[slist].append(str)
            else:
                ans[slist]=[str]
                
        retv=[]
        for k in ans:
            retv.append(ans[k])
        
        return retv
