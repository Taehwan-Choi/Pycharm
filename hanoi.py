num_of_disk=5
cnt=0
# 내가 구현한 함수, 기본적으로 원반수 n과 a,b,c가 있다.
def hanoi(num:int, x:int, y:int, z:int) -> int:
    global cnt
    if num==1:
        print(f'원반{num}을 {x}에서 {z}로 이동합니다.')
        cnt+=1
    else :
        hanoi(num-1,x,z,y)
        print(f'원반{num}을 {x}에서 {z}로 이동합니다.')
        cnt+=1
        hanoi(num-1,y,x,z)


#원반 1 기둥에 있는 원반 3개를 3 기둥으로 옮겨보자는 함수 호출
hanoi(4,1,2,3)

print(f'총 움직인 횟수는 :{cnt}')

# 책에 나와있는 함수 구현법

count=0

def hanoi_2(no:int, x:int, y:int) -> None:
    global count
    if no>1:
        hanoi_2(no-1,x,6-x-y)

    print(f'원반{no}를 {x}에서 {y}로 이동시킵니다.')
    count+=1

    if no>1:
        hanoi_2(no-1,6-x-y,y)


hanoi_2(4,1,3)
print(f"총 움직인 횟수는 : {count}")