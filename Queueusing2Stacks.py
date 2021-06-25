def Push(x,stack1,stack2):
    stack1.append(x)
def Pop(stack1,stack2):
    if len(stack1)==0 and len(stack2)==0:
        return -1
    elif len(stack2)==0 and len(stack1)>0:
        while(len(stack1)>0):
            stack2.append(stack1.pop())
        return stack2.pop()
    else:
        return stack2.pop()
   
