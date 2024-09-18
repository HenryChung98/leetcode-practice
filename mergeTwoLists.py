from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 더미 노드를 사용하여 새 리스트의 시작을 추적
        dummy = ListNode()
        tail = dummy

        # 두 리스트가 모두 끝날 때까지 반복
        while list1 and list2:
            # list1의 현재 값이 list2보다 작으면 list1의 노드를 선택
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # 새 리스트의 끝을 업데이트

        # 남은 노드를 모두 추가 (list1 또는 list2)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # dummy.next는 새로 병합된 리스트의 시작점
        return dummy.next


# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4
sol = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = sol.mergeTwoLists(list1, list2)

# 병합된 리스트 출력: 1 -> 1 -> 2 -> 3 -> 4 -> 4
current = merged_list
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
