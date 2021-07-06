"""
Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.



Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4



Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.


"""


class MyCircularQueue:

    def __init__(self, k: int):
        self._items = [-1] * k
        self._head = -1
        self._tail = -1
        self._queue_len = k
        self._size = 0

    def enQueue(self, value: int) -> bool:
        print(f'current queue: {self._items}, trying to enqueue: {value}, {self._size=}')
        if self.isFull():
            return False

        if self._tail == -1:
            self._head += 1
            self._tail += 1
        elif self._tail == self._queue_len - 1:
            self._tail = 0
        else:
            self._tail += 1

        self._items[self._tail] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        print(f'current queue: {self._items}, trying to dequeue: {self._head} element, {self._size=}')
        if self.isEmpty():
            return False

        if self._head == -1:
            return False
        elif self._head == self._queue_len - 1:
            self._items[self._head] = -1
            self._head = 0
        else:
            self._items[self._head] = -1
            self._head += 1

        self._size -= 1
        return True

    def Front(self) -> int:
        return self._items[self._head]

    def Rear(self) -> int:
        return self._items[self._tail]

    def isEmpty(self) -> bool:
        # return self._head == self._tail and (self._items[self._head] == -1 and self._items[self._tail] == -1)
        return self._size == 0

    def isFull(self) -> bool:
        # return self._head == self._tail and (self._items[self._head] != -1 and self._items[self._tail] != -1)
        return self._size == self._queue_len


if __name__ == '__main__':

    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(2)
    obj.enQueue(2)
    print(obj._items)
    obj.deQueue()
    print(obj._items)
    obj.enQueue(2)
    print(obj._items)
