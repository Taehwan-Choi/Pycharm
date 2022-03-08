from typing import Any

## collections 모듈을 이용한 컨데이너 덱(deque)을 이용해서 고정스택을 구현하는 방법(아래)
from collections import deque


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        #굳이 Exception을 상속받는 이유는, raise에 응답하기 위해서이다. 아니면 TypeError 발생
        pass

    def __init__(self, capacity:int=256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr<=0

    def is_full(self):
        return self.ptr>=self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr]=value
        self.ptr +=1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self):
        self.ptr=0

    def find(self,value:Any):
        temp=self.ptr-1
        while temp>=0:
            if self.stk[temp]==value:
                return temp
            temp-=1
        return -1

    def count(self, value:Any):
        temp=0
        for k in range(self.ptr):
            if self.stk[k]==value:
                temp+=1
        return temp

    def __contains__(self,value:Any):
        return self.count(value) > 0

    def dump(self):
        if self.is_empty():
            print("스택이 비어 있습니다.")
        else :
            for k in range(self.ptr):
                print(self.stk[k], end=' ')
            print('')

aa=FixedStack(100)





class Collection_Stack:

    def __init__(self, maxlen:int=256):
        self.capacity = maxlen
        self.__stk = deque([],maxlen)

    def __len__(self):
        return len(self.__stk)

    def is_empty(self):
        return not self.__stk

    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value:Any):
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()

    def peek(self):
        return self.__stk[-1]

    def clear(self):
        self.__stk.clear()

    def find(self, value:Any):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value:Any):
        return self.__stk.count(value)

    def __contains__(self, value:Any):
        return self.__stk.count(value) > 0

    def dump(self):
        print(list(self.__stk))

