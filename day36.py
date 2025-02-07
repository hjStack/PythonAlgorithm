
import sys

num=int(sys.stdin.readline().rstrip())

result=[]

for i in range(num):
    n1,n2=list(map(int,input().split()))
    result.append([n1,n2])

result.sort(key=lambda x:(x[0],x[1]))
# 플로 만들어 첫 번째 원소(x[0])를 기준으로 오름차순 정렬한 뒤,
# 첫 번째 원소가 같다면 두 번째 원소(x[1])를 기준으로 다시 오름차순 정렬합니다.
    
for i in result:
    print(i[0],i[1])
    

    