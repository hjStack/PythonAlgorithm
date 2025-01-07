

# 행렬의 덧셈
# 행과 열의 크기가 같은 두 행렬의 같은 행 같은 열의 값을 서로 더한 결과 
# 예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 
# 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다


# n,m=map(int,input().split())
# A,B=[],[]

# for i in range(n):
#    a=list(map(int,input().split()))
#    A.append(a) # ⭐️ 그냥 리스트에 입력받은 값을 추가하면 됐음 .. 
    
# for j in range(n):
#     b=list(map(int,input().split()))
#     B.append(b)

# # append() : 리스트에 항목을 추가 => list.append()

# for i in range(n):
#     for j in range(m):
#         result=A[i][j]+B[i][j]
#         print(result,end=' ')
#     print()

# ===============================

# 백준 - 2566

# 먼저 입력받을 리스트 결정
# result=[]

# max_value = 0 
# max_row=0
# max_column=0

# for i in range(9):
#     a=list(ma₩p(int,input().split()))
#     result.append(a)

# for j in range(9):
#     for k in range(9):
#         if result[j][k] >= max_value:
#             max_value=result[j][k]
#             max_row = j+1
#             max_column=k+1 
            
# print(max_value)
# print(max_row,max_column)


# 행렬 덧셈 복습해보기
n,m=list(map(int,input().split()))
A,B=[],[]

for i in range(n):  # A 배열에 첫번째 3X3 입력리스트 넣고
    a=list(map(int,input().split()))
    A.append(a)
    
for j in range(n):  # B 배열에 첫번째 3X3 입력리스트 넣기
    b=list(map(int,input().split()))
    B.append(b)
    

for i in range(n):
    for j in range(m):
        result=A[i][j]+B[i][j]
        print(result,end=' ')
    print()