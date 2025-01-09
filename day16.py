

# 정렬 알고리즘 - 2750

# n=int(input())

# result=[]

# for i in range(n):
#     m=int(input())
#     result.append(m)

# for j in range(n):
#     for k in range(n-j-1):
#         if result[k]>result[k+1]:
#             result[k],result[k+1]=result[k+1],result[k]
            
# for x in result:
#     print(x)


# 정렬 알고리즘 - 2751
# sys.stdin.readline() 이렇게 짜는게 input()보다 시간이 빠름

# import sys

# n = int(sys.stdin.readline())
# result=[]

# for i in range(n):
#     m=int(sys.stdin.readline())
#     result.append(m)

# result.sort()
# # list.sort()는 반환값이 없음 

# for a in result:
#     print(a)


# 백준 알고리즘 - 2587

# 대푯값 구하기 - 중앙값 구하는게 문제 핵심 ⭐️
# 중위값은 array에 있는 값중에서 정렬 후 순서상 중위점에 있는 숫자
# 그런데 array의 아이템수가 짝수라면 중위값이 2개가 되고, 
# 이때는 2개의 중위값의 평균이 median

# sum=0
# result=[]

# for i in range(5):
#     n=int(input())
#     sum +=n
    
#     result.sort()  # 리스트를 정렬하여 중간값 계산 준비
    
#     if len(result) % 2 == 1:
#         median=result[i//2]
#     elif len(result) % 2 == 0:
#         median=(result[i//2] + result[i//2-1])/2
        
    
# print(sum//5)
# print(median)


# 백준 - 1427 : 내림차순 정렬
n=int(input())

result=[]

while n>0:
    result.append(n%10)
    n //= 10

for j in range(len(result)):
    for k in range(len(result)-j-1):  
        if result[k]<result[k+1]:
            result[k],result[k+1]=result[k+1],result[k]
            
for x in result:
    print(x,end='')
