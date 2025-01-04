

# 복습 

# n=int(input())

# for i in range(1,n+1):
#     print(' '* (n-i)+ i * '*')
    
    
# 복습 - 10807

# num1=int(input())
# n=list(map(int,input().split()))
# findNumber=int(input())

# count=0

# for i in n:
#     if i == findNumber:
#     # 리스트의 find() 함수는 문자열에서만 사용 가능
#        count = n.count(findNumber)

# print(count)        
    
# 백준 - 10871

# a,b=map(int,input().split())
# n=list(map(int,input().split()))

# for i in n:
#     if i < b:
#         print(i)

# 백준 - 10818 
# max(),min()구현 

# def max_num(result):
#     num=result[0]  # ⭐️
#     for i in result:
#         if i>num:
#             num=i
#     return num

# def min_num(result):
#     num1=result[0]
#     for i in result:
#         if i<num1:
#             num1=i
#     return num1

# n=int(input())
# m=list(map(int,input().split()))

# print(min_num(m))
# print(max_num(m))

# 백준 - 10818

# 바구니룰 총 N개 가지고 있음
# 1-N번까지 번호가 매개져 있다
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다

# 가장 처음 바구니에는 공이 들어있지 않고 
# 바구니에는 공을 1개만 넣을 수 있음

# 앞으로 M번 공을 넣음 
# 공을 넣을 바구니의 범위를 정하고 
# 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣음 

# 백준 10810
# n,m=map(int,input().split())

# box=[0]*n

# for a in range(1,m+1):
#     i,j,k=list(map(int,input().split()))
#     for b in range(i-1,j):
#     # i=1 j=2 k=3 : 1번 바구니부터 2번 바구니까지 공을 3번 넣음 
#         box[b]=k
        
# for c in box:
#     print(c,end=' ')


# 백준 - 10811 : 바구니 뒤집기

n,m=map(int,input().split())
tmp=0
box = [i for i in range(1, n + 1)]

for a in range(1,m+1):
    i,j=list(map(int,input().split()))
    for b in range((j - i + 1) // 2):  # 범위의 절반만 반복
        tmp=box[i-1+b]
        box[i-1+b]=box[j-1-b]
        box[j-1-b]=tmp
        
for c in box:
    print(c,end=' ')