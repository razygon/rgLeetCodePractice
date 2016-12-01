
class Solution(object):
'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.'''
# def checkPalindrome(self, s):
#     slen = len(s)
#     for i in range(0,slen/2):
#         if s[i] == s[slen-i-1]:
#             continue
#         else:
#             return -1
#     return 1        
# def longestPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     flag = 0
#     start = 0
#     end = 0
#     cid = -1
#     if len(s)>1000:
#         return None
#     if len(s) == 1 or 1 == self.checkPalindrome(s):
#         return s
#     for ch in s:
#         cid = cid + s[cid+1:].index(ch) +1
#         ccid = cid
#         while(ch in s[ccid+1:]):
#             ccid = ccid + s[ccid+1:].index(ch) +1
#             #  print cid,ccid
#             #   print s[cid:ccid+1]
#             if 1 == self.checkPalindrome(s[cid:ccid+1]) and flag <= (ccid-cid):
#                 flag = ccid-cid
#                 #check whether it's a word
#                 start = cid
#                 end = ccid+1
#     if flag == 0:
#         return s[0]
#     return s[start:end]

    def expandAroundCenter(self, s,  c1,  c2):
        l = c1
        r = c2
        n = len(s)
        while (l >= 0 and r <= n-1 and s[l] == s[r]):
            l = l-1
            r = r+1
        return s[l+1:r]

 
    def longestPalindrome(slef, s):
        n = len(s)
        if (n == 0): 
            return ""
        longest = s[0:1]
        for i in range(0,n-1):
            p1 = slef.expandAroundCenter(s, i, i)
            if (len(p1) > len(longest)):
                longest = p1
 
            p2 = slef.expandAroundCenter(s, i, i+1);
            if (len(p2) > len(longest)):
                longest = p2
        return longest
        
'''o(N) in space and time complexity'''
#// Transform S into T.
# // For example, S = "abba", T = "^#a#b#b#a#$".
# // ^ and $ signs are sentinels appended to each end to avoid bounds checking
# string preProcess(string s) {
#   int n = s.length();
#   if (n == 0) return "^$";
#   string ret = "^";
#   for (int i = 0; i < n; i++)
#     ret += "#" + s.substr(i, 1);
 
#   ret += "#$";
#   return ret;
# }
 
# string longestPalindrome(string s) {
#   string T = preProcess(s);
#   int n = T.length();
#   int *P = new int[n];
#   int C = 0, R = 0;
#   for (int i = 1; i < n-1; i++) {
#     int i_mirror = 2*C-i; // equals to i' = C - (i-C)
    
#     P[i] = (R > i) ? min(R-i, P[i_mirror]) : 0;
    
#     // Attempt to expand palindrome centered at i
#     while (T[i + 1 + P[i]] == T[i - 1 - P[i]])
#       P[i]++;
 
#     // If palindrome centered at i expand past R,
#     // adjust center based on expanded palindrome.
#     if (i + P[i] > R) {
#       C = i;
#       R = i + P[i];
#     }
#   }
 
#   // Find the maximum element in P.
#   int maxLen = 0;
#   int centerIndex = 0;
#   for (int i = 1; i < n-1; i++) {
#     if (P[i] > maxLen) {
#       maxLen = P[i];
#       centerIndex = i;
#     }
#   }
#   delete[] P;
  
#   return s.substr((centerIndex - 1 - maxLen)/2, maxLen);
# }
