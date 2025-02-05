
# 좌표 정렬

import sys

n=int(sys.stdin.readline())
result=[]

for i in range(n):
    n1,n2=list(map(int,input().split()))
    result.append([n1,n2])
    
result.sort()

for i in result:
    print(i[0],i[1])


# 나이순정렬

import sys

n=int(sys.stdin.readline())
member=[]

for i in range(n):
    n1, name = sys.stdin.readline().split()
    n1=int(n1)
    member.append([n1,name])
    
member.sort(key=lambda x:x[0])
# sort 함수의 인자로 key = function을 넣어주면 되고 function이 곧 기준이 된다.
# 람다식에서 두번째 값을 기준으로 정렬을 하는데 두번째 값이 같을때에는 첫번째 값을 기준으로 오름차순 정렬을 하는 것임

for i in member:
    print(i[0],i[1])