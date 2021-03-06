2. Add Two Numbers  
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getValueAndMoveNext(self, L):
        if L != None:
            value = L.val
            L = L.next
            return value
        else:
            return 0
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(0)
        head = l3
        while(l1 or l2 ):
            if l1!=None:
                v1 = l1.val
                l1=l1.next
            else:
                v1 = 0
                
            if l2!=None:
                v2 = l2.val
                l2=l2.next
            else:
                v2 = 0
                
            v = (v1+v2+carry)%10
            carry = (v1+v2+carry)/10
            l3.next = ListNode(v)
            l3 = l3.next
        if carry >0:
            l3.next = ListNode(carry)
        return head.next
