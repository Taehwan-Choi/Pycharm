from __future__ import annotations
import random
from typing import Any, Type

class Node:
    def __init__(self, data:Any = None, prev:node= None, next:node= None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self
        #여기서, 더미 노드를 만들 때 별도로 지정한 상황이 아니면 자기 자신을 참조하는 인스턴스 만든다!!!


class DoubleLinkedList:

    def __init__(self):
        self.head = Node()
        self.current = self.head
        self.no = 0

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.head.next == self.head

    def search(self,data):
        p=self.head.next
        #self.head는 실제 머리노드가 아니고, 더미노드이다. self.head.next가 헤드노드이고
        #self.head.next부터 0번 위치라고 할 수 있다.(더미의 존재를 의식할 것!!)
        cnt=0

        while p is not self.head:
            if p.data == data:
                self.current=p
                return cnt
            cnt+=1
            p=p.next

        return -1


    def __contains__(self,data):
        return self.search(data) >= 0


    def print_current(self):
        if self.is_empty():
            print("리스트가 비어있습니다. 주목노드는 없습니다.")
        else:
            print(self.current.data)

    def print_reverse(self):
        p = self.head.prev

        while p is not self.head:
            print(p.data, end=' ')
            p = p.prev
        print()

    def print(self, reverse=False):

        if reverse == True:
            self.print_reverse()

        else :
            p = self.head.next

            while p is not self.head:
                print(p.data, end=' ')
                p=p.next
            print()

    def next(self):
        if self.is_empty() or self.current.next == self.head:
            return False
        else:
            self.current=current.next
            return True

    def prev(self):
        if self.is_empty() or self.current.prev == self.head:
            return False
        else:
            self.current = self.current.prev
            return True

    def add(self,data):
        # 이 함수의 최고 장점!! 순환 참조가 걸려 있기 때문에 비어있는 리스트 일때의 특별 처리가 불필요하다!
        # 그렇기 때문에 오류가 날 가능성이 적다는 장점!
        new=Node(data,self.current,self.current.next)
        self.current.next.prev = new
        self.current.next = new

        self.current=new
        self.no +=1

    def add_first(self,data):
        self.current=self.head
        self.add(data)

    def add_last(self,data):
        self.current=self.head.prev
        self.add(data)

    def remove_current(self):
        #굳이 add 함수처럼 remove를 바로 하지 않고, remove_current 부터 구현하는 이유는
        #add는 current 위치가 이미 정해져 있으므로 그냥 삽입 작업만 하면 끝! 이지만
        #remove는 data를 검색해서 있는지 확인하고 그 위치를 확인해야 하므로 절차가 하나 더 많고,
        #remove_first, last 처럼 data 위치 확인 없이 그냥 위치만으로 삭제할 필요도 있기 때문에
        #노드를 삭제한다라는 절차를 따로 떼서 구현하는 것
        if self.is_empty():
            return False
        else:
            self.current.prev.next =self.current.next
            self.current.next.prev = self.current.prev

            self.current=self.current.prev
            self.no -=1

            if self.current is self.head:
                self.current = self.current.next

    def remove(self,data):
        p = self.head.next

        while p is not self.head:
            if p.data==data:
                self.current = p
                self.remove_current()
                break
            else:
                p=p.next

    def remove_first(self):
        self.current = self.head.next
        self.remove_current()

    def remove_last(self):
        self.current = self.head.prev
        self.remove_current()

    def clear(self):

        while not self.is_empty() :
            self.remove_first()
        self.no = 0

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)
    #이터레이터는 외부의 클래스이므로, head의 주소값 하나는 넘겨줘야 한다!!
    #current 와 no는 굳~이 필요없는 정보라 생략(current=head.next)
    #호출 할때마다 이터레이터 클래스의 __next__를 "자동으로 실행한다"는 느낌

    def __reversed__(self):
        return DoubleLinkedListIterator_Reversed(self.head)


class DoubleLinkedListIterator:
    def __init__(self,head):
        self.head=head
        self.current=self.head.next

    def __iter__(self):
        return self
    # 이터레이터 클래스면 그냥 위의 함수는 "무조건" 넣어준다.

    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        #이터레이션의 끝을 정해주지 않으면 계속해서 다음을 뱉어낸다!(순환 참조)

        else :
            temp=self.current.data
            self.current=self.current.next
            return temp


class DoubleLinkedListIterator_Reversed:
    def __init__(self,head):
        self.head=head
        self.current=self.head.prev

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        #이터레이션 클래스는 반드시 끝을 명시해야 한다! 안 그러면 순환 참조라 계속 다음을 뽑아낸다!!!
        else :
            temp = self.current.data
            self.current = self.current.prev
            return temp


test=DoubleLinkedList()


for k in range(30):
    test.add_last(random.randint(1,101))
