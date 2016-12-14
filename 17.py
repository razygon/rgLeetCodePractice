'''
17. Letter Combinations of a Phone Number 
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
class Solution(object):
    def letterCombinations1(self, digits):
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in range(0, len(chr[num])):
                if len(res):
                    for k in range(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(str(chr[num][j]))
            res = copy.copy(tmp)
        return res
        
    def letterCombinations3(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                    dfs(num+1, string+letter, res)
        
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        length = len(digits)
        if length == 0:
            return res
        dfs(0, '', res)
        return res
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        in order to reduce the time complex, the method i used didn't consider conbination.
        """
        pdict = {0:[1,' '],
                 1:[1,'*'],
                 2:[3,'abc'],
                 3:[3,'def'],
                 4:[3,'ghi'],
                 5:[3,'jkl'],    
                 6:[3,'mno'],    
                 7:[4,'pqrs'],    
                 8:[3,'tuv'],    
                 9:[4,'wxyz']}
        if len(digits) == 0:
            return []
        sum = 1
        for s in digits:
            sum*=pdict[int(s)][0]
        #print sum
        pstr = ['']*sum
        for s in digits:
            times = sum/pdict[int(s)][0]
            for i in range(0,sum):
                flag = i/times
                pstr[i] = pstr[i] + pdict[int(s)][1][flag]
        return pstr
