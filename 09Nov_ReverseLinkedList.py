#
# https://leetcode.com/problems/reverse-linked-list/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
# 
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
###################################################################### APPROACH 1 ###################################################################
      
        if head is None:
            return head

        currentNode = None

        while head:
            if currentNode:
                currentNode = ListNode(head.val, currentNode)
            else:
                currentNode = ListNode(head.val, None)

            head = head.next

        return currentNode

###################################################################### APPROACH 2 ###################################################################
      
        if head is None:
            return head

        prev = None

        while head:
            
            nxt = head.next
            
            head.next = prev

            prev = head

            head = nxt
        
        return prev
