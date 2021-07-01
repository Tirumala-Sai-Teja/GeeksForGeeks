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
