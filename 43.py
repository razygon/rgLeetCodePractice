'''
43. Multiply Strings   
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        arr = [0 for i in range(0,len(num1)+len(num2))]
        ans = []
        for i in range(0,len(num1)):
            for j in range(0,len(num2)):
                arr[i+j]+=int(num1[i])*int(num2[j])
        i=0
        while(i<len(arr)):
            digit = arr[i]%10
            carry = arr[i]/10
            if i+1<len(arr):
                arr[i+1]+=carry
            ans.insert(0,str(digit))
            i = i+1
        while(ans[0]=='0' and len(ans)>1):
            del(ans[0])
        return ''.join(ans)
