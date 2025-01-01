
# 백준 - 10810
# 문제를 잘 살펴보기 !! 

# n,m=map(int,input().split())
# box = [0] * n  # 초기에는 모든 바구니에 공이 없는 상태(0) # 핵심 키워드
# # 모든 박스를 0으로 초기화한다음 넣는것이 중요

# for i in range(m):
#     a,b,c=map(int,input().split())
#     # 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻
#     # 1 2 3은 1번 바구니부터 2번바구니까지 공을 3번 넣음 
    
#     for k in range(a-1,b):
#         box[k]=c
            
# for j in box:
#     print(j,end=' ')


# 백준 - 2444

# n=int(input())

# 범위를 전체로 지정한다음 홀수개씩 출력하는 것이 중요함 

# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))
        
        
# for j in range(n-1,0,-1):
#        print(' '*(n-j)+'*'*(2*j-1))


# 백준 - 10988

str=input()

if list(str) == list(reversed(str)):
    print(1)
else:
    print(0)
    
# 리스트 각 요소로 분리해서 뒤집은 다음 같은지 check