# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# def mergeTwoLists(list1, list2): 
#     result = []
#     while len(list1) > 0 and len(list2) > 0:
#         curr1 = list1.pop(0)
#         curr2 = list2.pop(0)
#         if curr1 <= curr2:
#             result.append(curr1)
#             result.append(curr2)
#         else:
#             result.append(curr2)
#             result.append(curr1)
    
#     if len(list1) > 0 and len(list2) == 0:
#         for i in list1:
#             result.append(i)
#     if len(list2) > 0 and len(list1) == 0:
#         for i in list2:
#             result.append(i)
    
#     return result
# recursion version
# base case, either list goes to the end

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: #base case1
            return list2
        elif list2 is None: #base case2 
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2) #go to the head of the list find the smaller value, append the merged remaining list to the smaller head
            return list1
        else:
            list2.next = self.mergeTwoLists(list2, list2.next)
            return list2


# print(mergeTwoLists([1,2,4],[1,3,4]))
# print(mergeTwoLists([],[]))
# print(mergeTwoLists([],[0]))

