#Priority Queue - Lowest item with higest priority

class PriorityQueue:
    def __init__(self):
        self.queue= []

    def enqueue(self, item):
        if self.isEmpty():
            self.queue.append(item)
        else:
            self.queue.append(item)
            self.queue.sort()

   
    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)

        return None
#extend it later

q = PriorityQueue()

#Test whetehr the queue is empty

if q.isEmpty():
    print("The Queue is Empty")
else:
    print("The Queue is not empty")

#Performing the enqueue operation
q.enqueue(50)
q.enqueue(60)
print("Queue after inserting 50 and 60", q.queue)

q.enqueue(1)
q.enqueue(11)
q.enqueue(5)
print("Queue after inserting 1,11 and 5", q.queue)

#test whether the queue is empty
if q.isEmpty():
    print("The Queue is Empty")
else:
    print("The Queue is not empty")
#Dequeue operation on Queue
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())