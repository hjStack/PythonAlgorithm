
# # 중앙 이동 알고리즘 -> 2903

# # 상근이는 정사각형 점 4개를 고름
# # 정사각형의 각 변의 중앙에 점을 하나 추가한다.
# # 정사각형의 중심에 점을 하나 추가한다.

# # 2^2, 3^2, 5^2

# n=int(input())
# # n=1 점9개 3^2 (2^n+1) ** 2
# # n=2 25개 5^2 (2^n+1) ** 2
# # n=3 49개 7^2 (2^n+1) ** 2
    
# print((2**n+1) ** 2)

# 달팽이는 올라가고 싶다 -> 2869
# V미터인 나무 막대를 올라갈것임

# 달팽이는 낮에 A미터 올라갈 수 있다
# 밤에 잠을 자는 동안 B미터 미끄러진다. 
# 또, 정상에 올라간 후에는 미끄러지지 않는다.

# a,b,v=map(int,input().split())

# ground=0 # 초깃값
# day=0

# while True:
#     day+=1
#     ground +=a
#     if ground >=v:
#         break
#     ground -= b
    
# print(day)

# 시간 초과 ..

# import math

# a,b,v=map(int,input().split())

# day=(v-b)/(a-b)
# print(math.ceil(day)) # 올림 처리 함수 

# 브루트 포스 
# 카드의 합이 21을 넘지 않는 한도내에서 카드의 합을 최대한 크게 만듦

# 김정인 버전의 블랙젝에서 각 카드에는 양의 정수가 쓰여 있음
# 다음 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓음
# 그런후에 딜러는 숫자 M을 크게 외침 

# N장의 카드 중에서 3장의 카드를 골라야 한다
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만듦

n,m=list(map(int,input().split()))
result=list(map(int,input().split()))
sum1=0
total=0

# print(result)
    
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum1=result[i]+result[j]+result[k]
    # print(sum1)
            if sum1<=m:
               total = max(total, sum1) 
            
print(total)
            
