'''
 3Sum 
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''

class Solution(object):
    def sort(self,a,b,c):
        ma = max(a,b,c)
        mi = min(a,b,c)
        li = [a,b,c]
        li.remove(ma)
        li.remove(mi)
        return [mi,li[0],ma]
        
    def delduplicated(self, nums):
        orignums = nums
        for n in orignums:
            no = orignums.count(n)
            while(no > 2):
                nums.remove(n)
                no = no - 1
        return nums
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lists = []
        if nums.count(0) > 2:
            lists.append([0,0,0])
            nums.remove(0)
        orignums = self.delduplicated(nums)
        nums = list(orignums)
        for a in orignums:
            nums.remove(a)
            oldnums = list(nums)
            for b in oldnums:
                c = 0-a-b
                nums.remove(b)
                if c in nums:
                    zlist = self.sort(a,b,c)
                    if zlist not in lists:
                        lists.append(zlist)
            nums = list(oldnums)
          #  print nums
            
        return lists
       
'''
 def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
'''
