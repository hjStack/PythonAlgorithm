

# 행렬의 덧셈
# 행과 열의 크기가 같은 두 행렬의 같은 행 같은 열의 값을 서로 더한 결과 
# 예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 
# 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다


n,m=map(int,input().split())
A,B=[],[]

for i in range(n):
   a=list(map(int,input().split()))
   A.append(a) # ⭐️ 그냥 리스트에 입력받은 값을 추가하면 됐음 .. 
    
for j in range(n):
    b=list(map(int,input().split()))
    B.append(b)

# append() : 리스트에 항목을 추가 => list.append()

for i in range(n):
    for j in range(m):
        result=A[i][j]+B[i][j]
        print(result,end=' ')
    print()
