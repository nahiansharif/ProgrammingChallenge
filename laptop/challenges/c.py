#Given a sorted linked list, delete all duplicates such that each element appear only once.

def removeDuplicates(self, head):
    if not head: 
        return None
    def iterative(head):
        current = head
        while current: 
            if current.next and current.val == current.next.val:
                current.next == current.next.next
            else: 
                current = current.next
        return head

    


    return iterative(head)

removeDuplicates(6)