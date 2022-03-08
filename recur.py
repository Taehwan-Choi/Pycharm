from FixedStack import FixedStack

def recur(n:int) -> int :
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)


stack = FixedStack(100)



# 아래는 recur 함수를 비재귀적으로 나타낸 것. 자기자신을 호출하는 방식이 아니라
# 자기 자신의 함수 처음으로 계속 돌아가는 방식으로 표현한 것이다.(값을 스택하면서 저장하는 식으로)

def recur2(n:int) -> int:

    global stack
    while True:
        if n>0:
            stack.push(n)
            n=n-1
            continue
        if not stack.is_empty():
            n=stack.pop()
            print(n)
            n=n-2
            continue
        break


recur2(4)