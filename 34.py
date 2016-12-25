'''
34. Search for a Range  
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            start = nums.index(target)
        except:
            return [-1,-1]
            
        rnums = list(reversed(nums))
        length = len(nums)
        end = length - rnums.index(target) -1
        return [start,end]
