
# reverseList.py
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next # 获取现在next 
            curr.next = prev # 修改当前的Next, 绑定为最初的空
            prev = curr # 设置下一轮的prev
            curr = next # 将最初的Next 绑定为当前的头部
        return prev 