'''
18. 4Sum 
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        lists = []
        for i in range(0,length-3):
            fix1 = nums[i] - target   
            for j in range(i+1,length-2):
                fix = fix1 + nums[j]    
                l = j+1
                r = length -1
                
                while l<r:
                    tmp = fix + nums[l] + nums[r] 
                    if tmp == 0:
                        if (nums[i],nums[j],nums[l],nums[r]) not in lists:
                            lists.append((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                    elif tmp > 0:
                        r-=1
                    else:
                        l+=1
        return lists
