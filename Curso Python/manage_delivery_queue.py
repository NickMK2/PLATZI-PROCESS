from collections import deque

def manage_delivery_queue():
    delivery_queue = deque(['delivery1', 'delivery2', 'delivery3'])
    delivery_queue.append('delivery4')
    delivery_queue.append('delivery5')
    delivery_queue.append('delivery6')
    delivery_queue.appendleft('delivery0')
    delivery_queue.pop()
    return delivery_queue
    
queue = manage_delivery_queue()
print(queue)
    
print(manage_delivery_queue())
