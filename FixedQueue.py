from typing import Any


class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity:int = 100):
        self.no=0
        self.front=0
        self.rear=0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enque(self, x):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear +=1
        self.no+=1
        if self.rear == self.capacity:
            self.rear=0
        #배열의 처음으로 돌아가서 링버퍼를 구현할 수 있도록 주의할 것

    def deque(self):
        if self.is_empty(self):
            raise FixedQueue.Empty
        x=self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front=0
        return x

    def peek(self):
        if self.is_empty(self):
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value:Any):
        for k in range(self.no):
            idx=(k + self.front)%self.capacity
            if self.que[idx]==value:
                return idx
        return -1

    def count(self,value):
        temp=0
        for k in range(self.no):
            idx=(k+self.front) % self.capacity
            if self.que[idx] == value:
                temp +=1
        return temp

    def __contains__(self,value):
        return self.count(value) > 0

    def clear(self):
        self.no=0
        self.front=0
        self.rear=0

    def dump(self):
        if self.is_empty():
            print("큐가 비어 있습니다.")
        else:
            for k in range(self.no):
                idx = (k + self.front) % self.capacity
                print(self.que[idx], end=' ')
            print('')

