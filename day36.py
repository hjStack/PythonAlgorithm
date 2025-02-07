
# import sys

# num=int(sys.stdin.readline().rstrip())

# result=[]

# for i in range(num):
#     n1,n2=list(map(int,input().split()))
#     result.append([n1,n2])

# result.sort(key=lambda x:(x[0],x[1]))
# # 튜플로 만들어 첫 번째 원소(x[0])를 기준으로 오름차순 정렬한 뒤,
# # 첫 번째 원소가 같다면 두 번째 원소(x[1])를 기준으로 다시 오름차순 정렬합니다.
    
# for i in result:
#     print(i[0],i[1])
    

# 수 정렬하기3
# sort(),input() -> 메모리 초과를 쉽게 발생시킬 수 있음 
    
import sys
    
num=int(sys.stdin.readline())
result=[0]*10001

for i in range(num):
    n1=int(sys.stdin.readline())
    result[n1]+=1  # 등장 횟수 

for j in range(10001):
    for _ in range(result[j]):
        print(j)


# sort() 함수로 정렬하거나 for문 내에서 append로 리스트에 값을 추가하는 식의 코드는 메모리 초과를 발생시킨다.
# → 위와 같은 방식은 카운팅 정렬(계수 정렬) 알고리즘을 기반으로 하였다.
# Counting Sort는 정렬 알고리즘으로 의 시간복잡도를 갖음
