'''
Global size variable and Six queue functions 
to go along with queuetester.py

By Aidan Lalonde-Novales
'''

# component 1: creates a global variable for the size of the queue (being 10)
global queue_size
queue_size = 10

# component 2: adds a value to the end of the queue (if there is room)
def enqueue(queue, value):
    if len(queue) < queue_size:
        queue.append(value)
        return True
    else:
        return False

# component 3: removes a value from the front of the queue (if there is one)
def dequeue(queue):
    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None

# component 4: returns the first value in the queue (if it exists)
def peek(queue):
    if len(queue) > 0:
        return queue[0]
    else:
        return None

# component 5: checks if the queue is empty or not
def isempty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

# component 6: adds items to queue and returns number of items added
def multienqueue(queue, items):
    count = 0
    for item in items:
        if enqueue(queue, item):
            count += 1
    return count

# component 7: removes items in the queue and returns number of items removed
def multidequeue(queue, number):
    removed_numbers = []
    for c in range(number):
        value = dequeue(queue)
        if value != None:
            removed_numbers.append(value)
    return removed_numbers
