

n,m=map(int,input().split())

# 1부터 n까지의 숫자가 담긴 리스트를 생성하는 것
basket=[i for i in range(1,n+1)]

for i in range(m):
    i,j=list(map(int,input().split()))
    
    temp=basket[i-1]
    basket[i-1]=basket[j-1]
    basket[j-1]=temp
    

for j in basket:
    print(j,end=' ')