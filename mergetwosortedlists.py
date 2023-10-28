class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1, l2):
    dummy=ListNode(0)
    current=dummy
    while l1 and l2:
        if l1.val<l2.val:
            current.next,l1=l1,l1.next
        else:
            current.next,l2=l2,l2.next
            
        current=current.next
        
    current.next=l1 or l2
    return dummy.next
        
    
# # Test Case 1: Merging two empty lists should result in an empty list
# l1 = None
# l2 = None
# result = mergeTwoLists(l1, l2)
# # Expected Output: None
# print(result)

# # Test Case 2: Merging an empty list with a non-empty list should return the non-empty list
# l1 = None
# l2 = ListNode(1)
# result = mergeTwoLists(l1, l2)
# # Expected Output: 1 -> None
# while result:
#     print(result.val, end=" -> ")
#     result = result.next

# Test Case 3: Merging two sorted lists
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(4, ListNode(6, ListNode(7)))
result = mergeTwoLists(l1, l2)
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 4: Merging two sorted lists of different lengths
# l1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
# l2 = ListNode(2, ListNode(4, ListNode(6)))
# result = mergeTwoLists(l1, l2)
# # Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
# while result:
#     print(result.val, end=" -> ")
#     result = result.next
# print(l2.val)
