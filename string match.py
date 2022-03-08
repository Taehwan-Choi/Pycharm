
# 브루트포스 문자열 검색, 포인터텍스트, 포인터패턴을 0, 0 으로 두고
# 포인터패턴이 끝까지 가면 검색 성공이므로 while 벗어나고, 찾은 문자열의 시작값 pt-pp를 반환한다
# pp가 끝까지 가지 못한 상황에서 pt가 끝나버리면 실패한 것이므로 while문 나와서 -1을 반환한다.

def bf_match(text:str, pat:str) -> int:
    pt=0
    pp=0

    while pt != len(text) and pp != len(pat):

        if text[pt] == pat[pp]:
            pt+=1
            pp+=1
        else :
            pt = pt - pp + 1
            pp = 0

    return pt-pp if pp == len(pat) else -1


print(bf_match('ddddwasdekvljpoelaslojvpaaaaaaddaspokasdfvpod','asdf'))



print('alkfjlkjalsjdfaaadlfjkkasldfjaaa'.find('aaa'))
print('alkfjlkjalsjdfaaadlfjkkasldfjaaa'.rfind('aaa'))
print('alkfjlkjalsjdfaaadlfjkkasldfjaaa'.index('aaa'))
print('alkfjlkjalsjdfaaadlfjkkasldfjaaa'.rindex('aaa'))

# find 함수는 그 값을 찾고, 첫 인덱스를 주는데, rfind는 오른쪽 인덱스를 반환 한다.(즉 찾은것 중에 제일 큰 인덱스를!)
# index 함수는 같은 기능을 하는데, 값이 없으면 -1을 주는게 아니라, 에러 값을 반환한다.

print('sassdfsf'.startswith('ass',1))

def kmp_match(txt:str, pat:str) -> int :
    pt=1
    pp=0

    skip=[0] * (len(pat)+1)

    skip[pt]=0

    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt +=1
            pp +=1
            skip[pt]=pp
        elif pp==0:
            pt+=1
            skip[pt]=pp
        else :
            pp=skip[pp]

    pp=0
    pt=0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt +=1
            pp +=1
        elif pp == 0:
            pt+=1
        else :
            pp=skip[pp]

    return pt-pp if pp==len(pat) else -1

print(kmp_match('ddddwasdekvljpoelaslojvpaaaaaaddaspokasdfvpod','asdf'))



def bm_match(txt:str, pat:str) -> int:

    skip=[None] * 256

    for pt in range(256):
        skip[pt]=len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) -pt -1


    while pt < len(txt):
        pp=len(pat) -1
        while txt[pt] == pat[pp]:
            if pp==0:
                return pt
            pt -= 1
            pp -= 1

        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1


print(bm_match('ddddwassssssdekvljpoelaslojvpaaaaaaddaspokasdfvpod','asadsxxxsdf'))


