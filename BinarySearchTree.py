
from __future__ import annotations
# 위 기능은 forward referencing 때문에 들어간 것, 파이썬 미래 기술을 시험적으로 써보는 것이다.
import random


class Node:
    def __init__(self, key, value, left:Node=None, right:Node=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def search(self,key):
        p=self.root

        while True:
            if p is None:
                return None

            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else :
                p = p.right

    def add(self,key,value):

        def _add(node, key, value):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key,value)
                else :
                    _add(node.left,key,value)
            else :
                if node.right is None:
                    node.right = Node(key,value)
                else :
                    _add(node.right,key,value)
            return True

        if self.root is None:
            self.root=Node(key, value)
            return True
        else :
            _add(self.root, key, value)


    def remove(self, key):
        p=self.root
        parent=None
        is_left_child=True

        while True:
            if p is None:
                print("해당 값을 찾을 수 없습니다.")
                return False

            if key == p.key:
                break
            else :
                parent=p
                if key < p.key:
                    is_left_child=True
                    p=p.left
                else :
                    is_left_child=False
                    p=p.right

        if p.left is None:
            if p is self.root:
                self.root = p.right
            # 좀 번거로워도, p가 삭제하고자 하는 노드이고, parent는 그 위에 있어야 하는데,
            # 찾는 값이 하필이면 루트랑 같으면 루트의 부모는 없으므로 에러나기 쉽다
            # 그래서 좀 귀찮아도, p가 루트일 경우는 이렇게 따로 정의한다. 왼쪽이 비어 있으므로 root=root.right 와 같다.
            elif is_left_child:
                parent.left = p.right
            else :
                parent.right = p.right

        elif p.right is None:
            # 여기의 elif는 앞의 if가 false라는 것이 이미 판단된 이후 이다. 즉 여기 블록까지 왔다는 것은 p.left는 None이 아니란 것!
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else :
                parent.right = p.left
        else :
            # 자식이 둘다 있는 경우가 나머지로 남는다. 여기 코드 블럭을 이해하기가 좀 복잡하다.
            largest_one_parent=p
            seeking_largest=p.left
            is_left_child=True
            while seeking_largest.right is not None:
                largest_one_parent=seeking_largest
                seeking_largest=seeking_largest.right
                is_left_child=False


            # 아래는 찾은 가장 큰 값의 노드의 키와 값을 삭제할 p에 복사를 하는 것이고.
            # 그 아래는, 가장 큰 값의 right는 None이라는 것이 확실하므로 무시할 수 있고, 혹시나 left에 딸려 있는 것들을 살려주기 위해서
            # 그 위에 있는 가장 큰 값의 parent의 가지에 붙여 주는 것이다.
            p.key = seeking_largest.key
            p.value = seeking_largest.value

            if is_left_child:
                largest_one_parent.left = seeking_largest.left
            else:
                largest_one_parent.right = seeking_largest.left
        return True

    def dump(self, reverse = False):

        def _dump(node):
            if node is not None:
                _dump(node.left)
                print(node.value, end=' ')
                _dump(node.right)
        def __dump(node):
            if node is not None:
                __dump(node.right)
                print(node.value, end=' ')
                __dump(node.left)
        if reverse :
            __dump(self.root)
        else :
            _dump(self.root)
        print()


    def min(self):
        if self.root is None:
            print("루트 노드가 비어 있습니다.")
        else:
            p=self.root
            while p.left is not None:
                p=p.left
        print(p.value)

    def max(self):
        if self.root is None:
            print("루트 노드가 비어 있습니다.")
        else:
            p=self.root
            while p.right is not None:
                p=p.right
        print(p.value)





test = BinarySearchTree()

test.add(100,'root')

for k in range(30):
    i = random.randint(1,200)
    test.add(i,f"{i}")

