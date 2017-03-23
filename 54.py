'''
Spiral Matrix Add to List
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
            
        r = len(matrix[0])
        c = len(matrix)
        re = []
        r_start = 0
        r_end   = r-1
        c_start = 0
        c_end   = c-1
        sum = 0
        length = r*c
        
        while(sum<length):
            for i in range(r_start, r_end+1):
                re.append(matrix[c_start][i])
            if len(re)==length:
                break
            for j in range(c_start+1, c_end+1):
                re.append(matrix[j][r_end])
            if len(re)==length:
                break
            for i in list(reversed(range(r_start,r_end))):
                re.append(matrix[c_end][i])
            if len(re)==length:
                break
            for j in list(reversed(range(c_start+1,c_end))):
                re.append(matrix[j][c_start])
            if len(re)==length:
                break
            sum = len(re)
        #    print re
    
            r_start = r_start+1
            r_end   = r_end-1
            c_start = c_start+1
            c_end   = c_end-1
        return re
