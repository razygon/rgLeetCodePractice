'''
31. Next Permutation   
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return
        for k in range(2,length+1):
            i = length - k
            if (nums[i]<nums[i+1]):
                nums[i+1:] = sorted(nums[i+1:])
                j = i+1
                while(j<=length-1):
                    if nums[j]>nums[i]:
                        k=nums[i]
                        nums[i]=nums[j]
                        nums[j]=k
                        return
                    j +=1
        nums.sort()   
