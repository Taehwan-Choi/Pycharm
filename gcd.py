#유클리드 호제법으로 두 수의 최대공약수를 구하는 함수 / 재귀함수 공부

def gcd(a:int, b:int) -> int :
    x=min(a,b)
    y=max(a,b)

    if y%x==0:
        print('최대공약수는 : ',x)

    else :
        gcd(x,y%x)

# gcd(10,25)
#
#
# 쉽게 가려면 min, max를 쓰지 않아도 된다. 그냥 바로 정의해버려도 알아서 순서 정렬이 된다(디버그 해보면),
# 큰 숫자, 작은숫자가 순서가 맞지 않으면 자동으로 바뀌기 때문

def gcd_2(a:int, b:int) -> int:
    if b==0:
        return a
    return gcd_2(b,a%b)

print(gcd_2(30,5))