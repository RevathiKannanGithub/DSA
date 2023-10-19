#
# https://leetcode.com/problems/add-two-numbers/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#####################################################################################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        correct_order_1 = []
        correct_order_2 = []
        current_node_1 = l1
        current_node_2 = l2
        counter = 0
        while current_node_1 is not None or current_node_2 is not None:
            if current_node_1 is not None:
                correct_order_1.append(current_node_1.val)
                current_node_1 = current_node_1.next
            if current_node_2 is not None:
                correct_order_2.append(current_node_2.val)
                current_node_2 = current_node_2.next
        correct_order_1.reverse()
        correct_order_2.reverse()
        print(correct_order_1)
        print(correct_order_2)
        # largest_list = max(len(correct_order_1), len(correct_order_2))
        # print(f"there are {largest_list} elements in the largest list")
        # ''.join(str(x) for x in correct_order_1)
        # number_1 = int(''.join(str(x) for x in correct_order_1))
        # do the above in 1 line
        number_1 = int(''.join(str(x) for x in correct_order_1))
        print(number_1)
        number_2 = int(''.join(str(x) for x in correct_order_2))
        print(number_2)
        sum_of_numbers = number_1 + number_2 # 807
        array_of_sum = [int(x) for x in str(sum_of_numbers)] # [8,0,7]
        print(array_of_sum)
        # reverse the array
        array_of_sum.reverse()
        # Create a linked list from the sum of the numbers
        output_linked_list = None
        output_current_node = output_linked_list
        print(output_linked_list)
        for i in range(len(array_of_sum)):
            if output_linked_list is None:
                output_linked_list = ListNode(array_of_sum[i])
                output_current_node = output_linked_list
            else:
                output_current_node.next = ListNode(array_of_sum[i])
                output_current_node = output_current_node.next
        return output_linked_list
