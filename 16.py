'''
16. 3Sum Closest   
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        flag = nums[length-1] + nums[length-2] + nums[length-3] - target
        # or just set a very big value 99999
        if flag>0:
            s = 1
        else:
            flag = abs(flag)
            s = -1
        for i in range(0,length-2):
            fix = nums[i]
            l = i+1
            r = length -1
            
            #print flag,s
            while l<r:
                tmp = fix + nums[l] + nums[r] - target
                if abs(tmp) < flag:
                    flag = abs(tmp)
                    if tmp > 0: s = 1
                    else: s = -1
                    if flag == 0:
                        return target
                if tmp >0:
                    r-=1
                else:
                    l+=1
        #print flag,s,target
        return flag*s + target
