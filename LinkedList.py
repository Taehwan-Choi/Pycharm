from __future__ import annotations
import random
from typing import Any, Type


# 포인터를 이용한 연결 리스트의 장단점
# 데이터를 추가 삭제할 때마다 이동할 필요가 없다 / 하지만 메모리에 인스턴스를 생성, 소멸하는데 자원이 소모된다!


# 커서(배열 인덱스)를 이용한 연결 리스트의 장단점   -> ArrayLinkedList를 참고할 것
# 데이터의 개수가 크게 변하지 않거나 예측가능할 때는 메모리를 미리 크게 할당해놔서 수시로 인스턴스 생성, 삭제하는 비용을 없앤다.

class Node:

    def __init__(self,data:Any =None,next =None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.no=0
        self.head=None
        self.current=None

    def __len__(self):
        return self.no

    def search(self,data):
        cnt = 0
        ptr=self.head

        while ptr is not None:
            if ptr.data == data:
                self.current=ptr
                return cnt
            cnt+=1
            ptr=ptr.next
        return -1

    def __contains__(self,data):
        return self.search(data) >=0

    def add_first(self,data:Any):
        temp=self.head
        self.head=Node(data,temp)
        self.current=self.head
        self.no +=1

    def add_last(self,data:Any):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
            self.no +=1
        else :
            p=self.head
            while p.next is not None:
                p=p.next
            p.next = self.current =Node(data)
            self.no +=1

    def remove_first(self):
        if self.head is None:
            print("머리 노드가 비어 있어서 삭제할 수 없습니다.")
            return -1
        else:
            self.head=self.current = self.head.next
            self.no -=1

    def remove_last(self):
        if self.no==0:
            print("비어 있는 연결리스트 입니다.")

        if self.no==1:
            self.remove_first()

        else :
            p=self.head
            
            while p.next.next is not None:
                p=p.next
            p.next=None

            self.current=p
            self.no -= 1

    def remove(self,p):
        if self.head is None:
            print("비어 있는 연결리스트 입니다.")
            return False

        if p==self.head:
            self.remove_first()

        else:
            ptr = self.head

            while ptr.next is not p:
                ptr=ptr.next
                if ptr.next is None:
                    print("해당 값은 존재하지 않습니다.")
                    return

            ptr.next = p.next
            self.no -=1
            self.current = ptr

    def remove_currentnode(self):
        self.remove(self.current)

    def clear(self):
        if self.head is None:
            print("비어 있는 연결리스트 입니다.")
            return False

        else :

            while self.head is not None:
                self.remove_first()

            self.current=None
            self.no = 0

    def next(self):
        if self.current == None or self.current.next == None:
            print("주목 노드를 옮기는데 실패하였습니다.(None값)")
            return False
        else:
            self.current = self.current.next
            return True

    def print_current(self):
        if self.current == None:
            print("주목 노드가 없습니다.")
            return False
        else :
            print(f"주목 노드의 값 : {self.current.data}")
            return True

    def print(self):
        if self.head is None:
            print("비어 있는 연결리스트 입니다.")
            return False

        ptr=self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

        return True

    def __iter__(self):
        return LinkedListIterator(self.head)
    # __iter__ 이것은 이터레이터를 반환한다. 즉 하나씩 꺼내면서 다음 원소를 뱉어내는 자료 구조를 구현하는 것


class LinkedListIterator:
    def __init__(self,head):
        self.ptr=head

    def __iter__(self):
        return self
    # 위 기능은, 다시 한번 이터레이터를 호출하면 자기자신의 구조를 부른다는 뜻이다!! (잘 이해할 것)

    def __next__(self):
        if self.ptr is None:
            raise StopIteration
        else:
            data=self.ptr.data
            self.ptr=self.ptr.next
            return data



test=LinkedList()

test.add_first(0)

for k in range(1,10):
    test.add_last(k)



