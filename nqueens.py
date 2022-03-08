

# Flag를 사용한 nqueen 해결법(약간 고전적인 방법)
#
# pos=[None]*8
# flag=[False]*8
# flagx=[False]*15
# flagy=[False]*15
# cnt=0

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}',end='')
    print()

def draw():
    for i in range(8):
        for j in range(8):
            print('1' if pos[i]==j else '0', end='')
        print()
    print()

def set(i:int) -> None :
    global cnt
    for j in range(8):
        if flag[j] == False and flagx[i+j]==False and flagy[i-j+7]==False:
            pos[i]=j
            if i==7:
                draw()
                cnt+=1
            else:
                flag[j]=True
                flagx[i+j]=True
                flagy[i-j+7]=True
                set(i+1)
                flag[j] = False
                flagx[i + j] = False
                flagy[i - j + 7] = False



# set(0)
# print(f'정답의 개수는 {cnt}')







# 1차원 리스트를 활용한 방법(다소 추상적이나 효율적인 방식)

#
# num=8
# cnt2=0
# answer=[None]*(num+1)

def nqueens(arr:list, n:int) -> None:
    global cnt2
    if n==num:
        if promissing(arr, n):
            print(arr[1:])
            cnt2+=1
    elif promissing(arr, n):
        for k in range(num):
            arr[n+1]=k
            nqueens(arr,n+1)
            arr[n+1]=None


def promissing(arr:list, n:int) -> bool:
    for k in range(1,n):
        if arr[k]==arr[n]:
            return False
        if arr[k]+k == arr[n]+n:
            return False
        if arr[k]-k == arr[n]-n:
            return False
    return True

#
# nqueens(answer,0)
#
# print(f'정답의 개수는 {cnt2}')





# 최종적으로 numpy를 이용한 2차원 배열 해결법(고급 방법)

import numpy as np

num_of_queen=8
board=np.zeros((num_of_queen,num_of_queen),dtype=int)
cnt3=0


def nqueens3(arr,n):
    global cnt3

    if n==num_of_queen-1:
        if promissing(arr,n):
            print(arr)
            cnt3+=1
    elif promissing(arr,n):
        for k in range(num_of_queen):
            board[n+1][k]=1
            nqueens3(arr,n+1)
            board[n+1][k]=0

def promissing(arr,n):
    for k in range(num_of_queen):
        if sum(board[:,k]) > 1:
            return False
    for k in range(-num_of_queen, num_of_queen):
        if sum(board.diagonal(k)) > 1:
            return False
        if sum(np.fliplr(board).diagonal(k)) > 1:
            return False
    return True


def nqueens_starter(n:int) -> None:
    for k in range(n):
        board[0,k]=1
        nqueens3(board,0)
        board[0,k]=0
    print(f'정답의 개수는 {cnt3}')

nqueens_starter(num_of_queen)


