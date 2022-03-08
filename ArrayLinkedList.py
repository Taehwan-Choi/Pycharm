from __future__ import annotations
import random

#########################################################################
# 이하 아래는 배열 인덱스를 활용한 연결 리스트 방법
# (인덱스로 나타낸 포인터를 커서라고 한다!!!!)
# 삭제된 노드 관리가 위의 포인터 연결리스트와 다르게 특별 관리가 필요하다.  free list



Null = -1



class Node:
    def __init__(self, data= Null, next= Null, dnext=Null):
        self.data = data
        self.next = next
        self.dnext = dnext    # deleted 노드의 next란 의미


class ArrayLinkedList:

    def __init__(self, capacity:int):
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0
        # deleted는 개수를 셀 필요가 없다! 어차피 머리만 떼거나 붙일 것이기 때문에, 탐색할 일이 없다.

    def __len__(self):
        return self.no

    def get_insert_index(self):
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max+=1
                return self.max
            else :
                print("저장 가능한 용량을 초과하여 추가할 수 없습니다.")
                return Null
        else:
            rec=self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    def delete_index(self,idx):
        # temp = self.deleted
        # self.deleted=idx
        # self.n[idx].dnext=temp

        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext=Null
        else :
            rec=self.deleted
            self.deleted=idx
            self.n[idx].dnext=rec

    def search(self, data:Any):
        cnt = 0
        ptr = self.head

        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt +=1
            ptr=self.n[ptr].next

        return Null

    def __contains__(self,data:Any):
        return self.search(data) >=0

    def add_first(self, data:Any):
        temp=self.head
        rec=self.get_insert_index()     # 가득차면 Null을 줄 수도 있다.

        if rec != Null:
            self.head = self.current = rec
            self.n[rec] = Node(data,temp)
            self.no +=1

    def add_last(self,data:Any):
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr=self.n[ptr].next
                # 여기서 ptr은 가장 마지막 원소로 간다!  ptr!=Null로 하면 ptr은 무조건 Null(-1)이 나오니 주의할 것

            rec=self.get_insert_index()

            if rec != Null:
                self.n[rec] = Node(data)
                self.n[ptr].next = self.current = rec
                self.no +=1

    def remove_first(self):
        if self.head != Null:
            temp=self.n[self.head].next
            self.delete_index(self.head)
            self.head=self.current = temp
            self.no -=1

    def remove_last(self):
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()

            else:
                ptr=self.head    # 스캔 노드
                pre=self.head    # 스캔 노드의 앞 부분

                while self.n[ptr].next != Null:
                    pre=ptr
                    ptr=self.n[ptr].next

                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -=1

    def remove(self,p):
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return
                # while문을 나왔으면 ptr은 지워야할 값(p) "앞"에 위치한다

                self.n[ptr].next = self.n[p].next
                self.delete_index(p)
                self.current = ptr
                self.no -=1

    def remove_currentnode(self):
        self.remove(self.current)

    def clear(self):

        while self.head != Null:
            self.remove_first()
        self.current = Null

    def next(self):
        if self.current == Null or self.n[self.current].next == Null:
            print("주목 노드를 옮길 수 없습니다(Null 값)")
            return False
        else:
            self.current = self.n[self.current].next
            return True

    def print_current(self):
        if self.current == Null:
            print("주목 노드가 없습니다.")
        else:
            print(f"주목 노드의 값 : {self.n[self.current].data}")

    def print(self):
        p=self.head

        while p != Null:
            print(self.n[p].data, end=' ')
            p=self.n[p].next

        print()

    def dump(self):
        p=self.head
        for i in self.n:
            print(f"[{i.data} / {i.next} / {i.dnext}]")


    def __iter__(self):
        return ArrayLinkedListIterator(self.n, self.head)

    def __reversed__(self):
        return ArrayLinkedListIterator_Reversed(self.n, self.head, self.no)




class ArrayLinkedListIterator:
    def __init__(self, n, head):
        self.n = n
        self.head = head
        self.current=self.head

    def __iter__(self):
        return self
    # 이터레이터 클래스는 해당 항목과 next를 무조건 가지고 있어야 한다!!!

    def __next__(self):
        if self.current == Null:
            raise StopIteration
        # 이터레이터 클래스는 끝나는 지점을 이렇게 명시해 줘야 한다!!!
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data


class ArrayLinkedListIterator_Reversed:
    def __init__(self,n,head,no):
        self.n = n
        self.head = head
        self.cnt=no
        self.last=False

    def __iter__(self):
        return self

    def __next__(self):
        temp=self.cnt-1
        p=self.head
        while temp > 0 :
            p=self.n[p].next
            temp -= 1
        self.cnt -=1

        if p == self.head:
            if self.last :
                raise StopIteration
            else :
                self.last = True
                return self.n[p].data
        return self.n[p].data


test= ArrayLinkedList(5)


for k in range(5):
    test.add_last(random.randint(1,100))













