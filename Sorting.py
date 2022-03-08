import random as rd
import FixedStack


list=[x for x in range(1,101)]
rd.shuffle(list)

print(list)
correct = [ x for x in range(1,101)]


# 버블정렬(Bubble Sorting)
# 이웃한 셀끼리 비교하면서 쭉 나가는 것
# (처음에 n-1번 비교해서 1개 고정하고, 그 다음에 n-2개 비교해서 다음 1개 고정하는 식)
def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for k in range(i):
            if arr[k]>arr[k+1]:
               arr[k], arr[k+1] = arr[k+1], arr[k]

def bubble2(arr):
    for i in range(len(arr)-1):     #0부터 원소의 개수-1 만큼의 숫자까지 for를 돌려준다. 원소의 개수 len(arr)=n
        # 단계의 step만 생각한게 아니라, 단계가 어느 인덱스에서 끝나는지에 주목한 방법이다.
        # n-1은 원소개수-1 로서 가장 끝의 idx를 의미한다. 원소개수 n과 끝인덱스 n-1 헷갈리지 말 것
        for j in range(len(arr)-1,i,-1):    # 원소의 끝에서, 위에 정의한 i 위치까지 하나씩 작아진다. 초기 0 끝값은 포함하지 않는다.
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]



def bubble3(a):
    ccnt=0
    scnt=0

    n=len(a)

    for i in range(n-1):
        exchange=0
        print(f'패스 {i+1}')
        for j in range(n-1,i,-1):
            for m in range(0,n-1):
                print(f'{a[m]:2}' + (' ' if m != j-1 else ' +' if a[j-1] > a[j] else ' -'), end='')
            print(f'{a[n-1]:2}')
            ccnt+=1

            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt+=1
                exchange+=1
        if exchange==0:
            break

    print(f'총 비교는 {ccnt} 하였고, 총 교환은 {scnt} 하였습니다.')


def bubble4(a):
    #     어려운 버블정리, last란 개념을 도입해서 스캔 범위를 직접 지정하는 방식
    # 마지막으로 교환한 인덱스를 last로 갱신해서 다음 패스를 돌릴때 범위를 한정한다

    n=len(a)
    k=0
    while k< n-1:
        last=n-1
        for j in range(n-1,k,-1):
            if a[j-1] > a[j] :
                a[j-1], a[j] = a[j], a[j-1]
                last=j
            k=last


def shaker_bubble(a):
    # 2번씩 짝지어서 큰원소를 뒤로 보내고, 작은원소를 앞에 보내는 식으로
    # 양 방향으로 섞는 느낌으로 버블을 보내는 것이다.
    left=0
    right=len(a)-1
    last=right
    while not left == right:
        # while left < right: 로 해도 된다(책의 경우에는 이렇게 했더라)
        for j in range(right,left,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last=j
            left=last

        for j in range(left,right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last=j
            right=last


def selection(a):
    # 쭉 밀고나가면서 가장 작은값의 idx를 찾아서 i인덱스와 교환한다. 앞에서부터 작은 값을 착착 쌓아나가는 방식
    # 선택정렬은 떨어져 있는 원소를 교환하므로 불안정하다. 즉 같은크기의 원소 순서가 바뀌기도 한다.
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(n-1,i,-1):
            # for j in range(i+1,n):으로 해도 된다. 그냥 i 이상의 모든 값을 가져오면 되기 때문에
            if a[min] > a[j]:
                min=j
        a[min],a[i] = a[i], a[min]



def insertion2(a):
    # 매우 비효율적이다!!!
    for end in range(1,len(a)):
        for i in range(end,0,-1):
            j=i
            temp=a[i]
            while j>0 and a[j-1] > temp:
                a[j] = a[j-1]
                j-=1
            a[j]=temp

def insertion(a):
    for i in range(1,len(a)):
        k=i
        temp=a[i]
        while k > 0 and a[k-1] > temp:
            a[k] = a[k-1]
            k-=1
        a[k]=temp



def binary_insertion2(a):

    for i in range(1,len(a)):
        key=a[i]
        pl=0
        pr=i-1

        while True:
            pc = (pl + pr)//2
            if a[pc] == key:
                break
            elif a[pc] < key :
                pl=pc+1
            elif a[pc] > key :
                pr = pc -1
            if pl > pr:
                break

        if pl <= pr:
            pd = pc+1
        #     pc가 지금 key 값이랑 정확히 일치하는 상황임. 그래서 key값을 pc_1 위치에 넣어줘야 한다(주의)
        # 따라서 하나씩 값을 밀어줘야 한다.

        else :
            pd =pr + 1
#             pr이 검색범위의 맨 끝 인덱스 이므로, 제일 끝에 삽입 한다는 뜻
        for j in range(i,pd,-1):
            a[j] = a[j-1]
        a[pd]=key



def binary_insertion(a):
    for i in range(1,len(a),1):
        pl = 0
        pr = i-1
        key=a[i]

        while True:
            pc = (pl + pr)//2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else :
                pr = pc - 1
            if pl > pr :
                break

        if pl <= pr :
            pd = pc +1
        else :
            pd = pr +1

        for k in range(i,pd,-1):
            a[k]=a[k-1]

        a[pd]=key



import bisect

def binary_insertion_best(a):
    for i in range(1,len(a)):
        bisect.insort(a,a.pop(i),0,i)
#         insort함수는 a에서  a.pop(i)값을 0부터 i 사이에 이진 삽입정렬 해준다.



def shell2(a):
    gap = len(a)//2

    while gap > 0 :
        for i in range(gap, len(a),1):
            temp=a[i]
            j=i-gap
            while j >=0 and a[j] > temp:
                a[j+gap] = a[j]
                j-=gap
            a[j+gap]=temp
        gap = gap//2




def shell3(a):
    # 좀 더 쉽고, 삽입정렬과 유사한 형태로서 이해하기 쉽게 만든 버전
    gap=len(a)//2

    while gap > 0:
        for i in range(gap,len(a),1):
            temp=a[i]
            j=i
            while j-gap >=0 and a[j-gap] > temp:
                a[j] = a[j-gap]
                j=j-gap
            a[j] = temp
        gap = gap//2




def shell(a):
    h=len(a)//2

    while h>0:
        for k in range(h,len(a),1):
            temp=a[k]
            i=k
            while i-h >= 0  and a[i-h] > temp:
                a[i]=a[i-h]
                i= i-h
            a[i] = temp
        h=h//2







#
# print(list)
#
# print(f"정렬이 정답과 일치하는 여부 : {list==correct}")
#

def partition(a):
    n=len(a)
    pl=0
    pr=n-1
    x=a[n//2]

    while pl <= pr :
        while a[pl] < x:
            pl +=1
        while a[pr] > x:
            pr -=1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1

    print(f"가운뎃 값은 {x}입니다.")

    print(f'피벗 이하인 그룹입니다. {a[:pl]}')

    if pl > pr+1:
        print(f'피벗과 일치하는 그룹입니다. {a[pr+1:pl]}')

    print(f'피벗보다 작은 그룹입니다. {a[pr+1:]}')


def quick_sort_recursion(a,start,end):
    pl=start
    pr=end
    x=a[(start+end)//2]

    # print(f'a[{start}] ~ a[{end}] : {a[start:end+1]}')

    while pl <= pr:
        while a[pl] < x:
            pl +=1
        while a[pr] > x:
            pr -=1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1

    if start < pr :
        quick_sort_recursion(a,start,pr)
    if pl < end:
        quick_sort_recursion(a, pl, end)

def quick_sort_recursion2(a):
    quick_sort_recursion(a,0,len(a)-1)



def quick_sort_unrecursion(a,start,end):
    tempostack=FixedStack.FixedStack(end-start +1)

    tempostack.push((start,end))

    while not tempostack.is_empty():
        pl, pr = start, end = tempostack.pop()
        x=a[(start+end)//2]

        while pl <= pr:
            while a[pl] < x:
                pl +=1
            while x < a[pr]:
                pr -=1
            if pl <= pr:
                a[pr], a[pl] = a[pl], a[pr]
                pr-=1
                pl+=1

        if start < pr :
            tempostack.push((start,pr))
        if pl < end:
            tempostack.push((pl,end))



def qsort(a,start,end):
    stack=FixedStack.FixedStack(len(a))
    stack.push((start,end))

    while not stack.is_empty():
        pl,pr = start, end = stack.pop()
        x = a[(start + end) // 2]


        while pl <= pr:
            while a[pl] < x : pl+=1
            while x < a[pr] : pr -=1

            if pl <= pr :
                a[pr], a[pl] = a[pl], a[pr]
                pr -= 1
                pl += 1

        if start < pr: stack.push((start,pr))
        if pl < end : stack.push((pl,end))





# 치우침을 예방하기 위해 처음 중간 끝 3개 값을 정렬하고,
# 기왕 정렬한 김에 스캔 범위에서 3개를 미리 줄여주는 고급 기법

def mid_return_and_sort(arr,a:int,b:int,c:int):
    # 무조건 b가 가운뎃값이라고 생각하고 알고리즘을 짜면 된다. b는 중간값의 인덱스인데, 반환해 준다.
    # a < b < c인 상태에서 a<b를 확정짓고, b<c를 확정짓고, b,c가 바뀌었을 경우를 대비해서 다시 a<b를 확정짓는다. 그러면 완성
    if arr[a] > arr[b] :
        arr[a], arr[b] = arr[b], arr[a]
    if arr[b] > arr[c] :
        arr[b], arr[c] = arr[c], arr[b]
    if arr[a] > arr[b] :
        arr[a], arr[b] = arr[b], arr[a]
    return b


def insertion_raw(a,start,end):
    for i in range(start+1,end+1,1):
        j=i
        temp=a[i]
        while j>0 and a[j-1]>temp:
            a[j]=a[j-1]
            j-=1
        a[j]=temp


def qsort_raw(a,start,end):

    if len(a) < 9:
        insertion_raw(a,start,end)
        return

    n=len(a)

    temp=mid_return_and_sort(a,start,(start+end)//2,end)
    x=a[temp]
    a[temp],a[end-1] = a[end-1], a[temp]
    pl=start+1
    pr=end-2


    while pl <= pr:
        while a[pl] < x :
            pl +=1
        while a[pr] > x:
            pr -=1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1

    if start < pr :
        qsort_raw(a,start,pr)
    if pl < end:
        qsort_raw(a,pl,end)



def qsort_1(a):
    qsort_raw(a,0,len(a)-1)



def merge(a):
    # 함수 안에 함수를 포함하는 방식으로 해서 깔끔하게 함수 하나로 끝내게 하였다.
    # 하지만 이 함수는 재귀를 이용하기 위해서 return에 의지하는 함수이다.
    # 즉, inplace 정렬이 아니기 때문에 a를 직접적으로 바꿔주지는 않는다.

    if len(a) == 1:
        return a

    def merge_sort(a, b):
        c = [None] * (len(a) + len(b))
        i = j = k = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c[k] = a[i]
                i += 1
                k += 1
            else:
                c[k] = b[j]
                j += 1
                k += 1

        while i < len(a):
            c[k] = a[i]
            i += 1
            k += 1

        while j < len(b):
            c[k] = b[j]
            j += 1
            k += 1

        return c

    mid = len(a) // 2

    return merge_sort(merge(a[:mid]),merge(a[mid:]))


# 정확히 이해하지 못한 병합정렬 알고리즘

def merge_complex(a):
    def _merge(a,start,end):
        if start < end:
            center = (start+end)//2

            _merge(a,start,center)
            _merge(a,center+1,end)

            p=j=0
            i=k=start

            while i<=center:
                buff[p]=a[i]
                p+=1
                i+=1

            while i<=end and j < p:
                if buff[j] <= a[i]:
                    a[k]=buff[j]
                    j+=1
                    k+=1
                else :
                    a[k]=a[i]
                    i+=1
                    k+=1

            while j < p:
                a[k]=buff[i]
                j+=1
                k+=1

    buff=[None]*(len(a))
    _merge(a,0,len(a)-1)
    del buff


# 책에 나오는 방식으로, heapify가 left~right 방식으로 이루어진다.
# right 범위까지 루트노드의 값을 적절한 위치에 내려 보내는 개념

def heap_sort1(a):
    def heapify(a,left,right):
        temp=a[left]
        parent=left

        while parent < (right+1)//2:
            cl = parent*2 + 1
            cr = cl +1

            child = cr if cr<=right and a[cr]>a[cl] else cl
            if temp >= a[child]:
                break
            a[parent]=a[child]
            parent=child
        a[parent]=temp

    for i in range((len(a)-1)//2,-1,-1):
        heapify(a,i,len(a)-1)
    for i in range(len(a)-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,0,i-1)
    print(a)



def heap_sort2(a):
    def heapify(a,left,right):

        parent=left
        temp = a[parent]

        while parent < (right+1)//2 :
            cl = parent*2 +1
            cr = cl +1

            if cr <=right and a[cr] > a[cl] :
                largechild = cr
            else:
                largechild = cl

            if a[largechild] > temp:
                a[parent]=a[largechild]
                parent=largechild
            else :
                break

        a[parent]=temp

    for k in range((len(a)-1)//2,-1,-1):
        heapify(a,k,len(a)-1)

    for k in range(len(a)-1,0,-1):
        a[0],a[k]=a[k],a[0]
        heapify(a,0,k-1)

    print(a)


# 아래 함수는 heapify가 재귀적으로 호출되는 방식이다. 바꾼 다음에 계속 부르는 것(더 쉬운 듯!)
def heap_sort3(a):
    def heapify(a,i,size):
        largest=i
        left = i*2 + 1
        right = i*2 + 2

        if left < size and a[left]>a[largest]:
            largest=left
        if right < size and a[right] > a[largest]:
            largest=right
        if largest == i:
            return
        else :
            a[largest], a[i] = a[i], a[largest]
            heapify(a,largest,size)

    for k in range((len(a)-1)//2, -1, -1):
        heapify(a,k,len(a))

    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a,0,i)

    print(a)

# heapq 모듈에서 heap에 push, pop 마음대로 해도 되는데, 항상 힙 조건이 유지된 채로 된다!! 아주 쉽게 구현 가능!!
import heapq

def heap_sort4(a):
    temp=[]
    for k in a:
        heapq.heappush(temp,k)
    for i in range(len(a)):
        a[i]=heapq.heappop(temp)
    print(a)




# 책에 나오는 방식으로, 도수분포표를 만들어서 for문을 '겁나' 돌리면서 만드는데, 이해하기도 어렵고 불편하다!
def counting_sort1(a):
    temp=[0]*(max(a)+1)
#     a배열의 가장 큰 값보다 1 더 큰 중간 버퍼를 만든다(10이면 0부터 11개의 자리가 필요하므로)
    b=[0]*len(a)

    for k in a :
        temp[k]+=1
    for k in range(1,len(temp)):
        temp[k]+=temp[k-1]
    for i in range(len(a)-1,-1,-1):
        temp[a[i]]-=1
        b[temp[a[i]]]=a[i]

    print(b)

def counting_sort2(a):
    temp=[0]*(max(a)+1)

    for k in a:
        temp[k]+=1

    i=0
    for k in range(len(temp)):
        while temp[k]>0:
            a[i]=k
            i+=1
            temp[k]-=1

    print(a)

counting_sort1(list)
