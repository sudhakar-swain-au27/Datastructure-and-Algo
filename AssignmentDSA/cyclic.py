
class Solution:

    def detectCyclic(self, head):

        slow = head
        fast = head

        while (slow != None) and (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
