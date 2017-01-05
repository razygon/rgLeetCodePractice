'''
48. Rotate Image   
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        ans = [[] for i in range(0,length) ]
        if length == 1:
            return
        for i in range(0,length):
            ans[i] = [matrix[length -j -1][i] for j in range(0,length) ]
        for i in range(0,length):
            matrix[i] = ans[i]
