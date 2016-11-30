3. Longest Substring Without Repeating Characters 
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        ss = []
        for ch in s:
            if ch not in ss:
                ss.append(ch)
            else:
                if flag < len(ss):
                    flag = len(ss)
                id = ss.index(ch)
                ss = ss[id+1:]
                ss.append(ch)
        if flag < len(ss):
            flag = len(ss)
        return flag
