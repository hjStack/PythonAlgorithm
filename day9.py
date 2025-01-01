
# 백준 - 10810

n,m=map(int,input().split())
box = [0] * n  # 초기에는 모든 바구니에 공이 없는 상태(0)

for i in range(m):
    a,b,c=map(int,input().split())
    # 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻
    # 1 2 3은 1번 바구니부터 2번바구니까지 공을 3번 넣음 
    
    for k in range(a-1,b):
        box[k]=c
            

for j in box:
    print(j,end=' ')