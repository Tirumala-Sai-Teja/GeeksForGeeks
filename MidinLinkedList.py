# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node
    n=head
    c=[]
    while n is not None:
        c.append(n.data)
        n=n.next
 
    return c[len(c)//2]
def findMid(head):
    if head is None:
        return None
    slow=head
    fast=head
    
    while(fast is not None and fast.next is not None):
        slow=slow.next # this pointer moves 1 nodes ahead everytime loop is run
        fast=fast.next.next

        # this pointer moves 2 nodes ahead everytime loop is run
        
    return slow.data
