'''
55. Jump Game 
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = 0
        pos = 0
        for mem in nums[:-1]:
            ans = max(ans,pos+mem)
            if ans<=pos:
                return False
            pos+=1
        return True
