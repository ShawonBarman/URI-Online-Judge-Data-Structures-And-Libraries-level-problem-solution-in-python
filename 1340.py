from collections import deque


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

while True:
    try:
        n = int(input())
        s = deque()
        q = deque()
        myQueue = PriorityQueue()
        _s = True
        _q = True
        _myQueue = True
        for i in range(n):
            x, y = map(int, input().split())
            if x == 1:
                s.append(y)
                q.append(y)
                myQueue.insert(y)
            else:
                a = s.pop()
                b = q.popleft()
                c = myQueue.delete()
                if a != y:
                    _s = False
                if b != y:
                    _q = False
                if c != y:
                    _myQueue = False

        if (_s and _q and _myQueue) or (not(_s) and _q and _myQueue) or (_s and not(_q) and _myQueue) or (_s and _q and not(_myQueue)):
            print("not sure")
        elif (_s and not(_q) and not(_myQueue)):
            print("stack")
        elif (not (_s) and _q and not(_myQueue)):
            print("queue")
        elif (not (_s) and not(_q) and _myQueue):
            print("priority queue")
        else:
            print("impossible")

    except EOFError:
        break