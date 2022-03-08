import random

test = [x for x in range(1,101)]

random.shuffle(test)

print(test)

def bubble(a):
    for k in range(0,len(a)):
        for i in range(len(a)-1,k,-1):
            if a[i-1]>a[i]:
                a[i-1],a[i]=a[i],a[i-1]

bubble(test)
print(test)

print("wow")

print('master work')