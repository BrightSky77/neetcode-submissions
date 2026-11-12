# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # 1. 중간 지점 찾기
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 뒷부분 반으로 자르고 뒤집기
        curr = slow.next
        prev = slow.next = None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next

        # 3. 앞부분(first)과 뒤집힌 뒷부분(second) 교차로 합치기
        first, second = head, prev
        while second:
            first.next,first = second, first.next
            second.next,second = first, second.next

    