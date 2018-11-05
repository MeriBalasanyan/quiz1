class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def main():

    x = Queue()
    x.enqueue(1)
    x.enqueue(2)
    x.enqueue(3)
    x.enqueue(4)
    x.enqueue(5)
    x.dequeue()
    print x.size()


main()