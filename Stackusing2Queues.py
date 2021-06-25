def push(x):
    global queue_1
    global queue_2
    while len(queue_1)>0:
        queue_2.append(queue_1.pop(0))
    queue_1.append(x)
    while len(queue_2)>0:
        queue_1.append(queue_2.pop(0))
    
#Function to pop an element from stack using two queues.     
def pop():
    global queue_1
    global queue_2
    
    if len(queue_1)==0:
        return -1
    else:
        return queue_1.pop(0)
