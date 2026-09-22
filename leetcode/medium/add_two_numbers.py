# Link : https://leetcode.com/problems/add-two-numbers/description/


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]  / 리스트에서 거꾸로 뽑아내서 처음*1, 두번째*2 세번째*3
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.



# Definition for singly-linked list.

# +++++++++풀이++++++++
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





# ///// #


# # gpt-5.6 이 제시한 정답
# class Solution_ai(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: Optional[ListNode]
#         :type l2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         dummy = ListNode(0)
#         current = dummy

#         carry = 0

#         while l1 or l2 or carry:

#             # 현재 자리 숫자 가져오기
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             # 두 숫자 + 이전 자리에서 올라온 carry
#             total = val1 + val2 + carry

#             # 현재 자리에 저장할 숫자
#             digit = total % 10

#             # 다음 자리로 넘길 숫자
#             carry = total // 10

#             # 새로운 노드 생성
#             current.next = ListNode(digit)
#             current = current.next

#             # 다음 노드로 이동
#             if l1:
#                 l1 = l1.next

#             if l2:
#                 l2 = l2.next

#         return dummy.next
        
        

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    

def make_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    # 테스트 케이스
    l1 = make_linked_list([2, 4, 3])
    l2 = make_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print_linked_list(result)  # 출력: 7 -> 0 -> 8 -> None


if __name__ == "__main__":
    main()
