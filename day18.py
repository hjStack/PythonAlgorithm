
# # 2차원 배열 백준 문제 복습해보기 

# n,m=map(int,input().split())
# A,B=[],[]

# # 첫번째 3x3을 담을 숫자의 배열을 정하고 입력받음 
# for i in range(n):
#    a=list(map(int,input().split()))
#    A.append(a)

# for j in range(n):
#     b=list(map(int,input().split()))
#     B.append(b)

# # 첫번째 행렬과 두번째 행렬을 더할 리스트 선언 
# result=[]

# for i in range(n):
#     for j in range(m):
#         result=A[i][j]+B[i][j]
#         print(result,end=' ')
#     print()

# print("===================================================")

# 백준 - 2563
# 가로 세로 크기가 각각 100인 정사각형인 도화지 위에 
# 가로 세로 크기가 10인 정사각형 모양의 색종이를 붙임

# # 색종이의 수 
# n=int(input())
# A,B=[],[]
# result=0

# # 색종이의 좌표 입력 for문 
# for i in range(n):
#     # 색종이를 붙인 위치의 좌표 
#     a,b=list(map(int,input().split()))
#     A.append(a)
#     B.append(b)
# # a : 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
# # b : 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리

# # print(result)

# background=[[0]*100 for a in range(100)]  #100X100로 도화지의 크기 초기화

# # 거리를 구하는 for문
# for i in range(n):
#     for j in range(A[i],A[i]+10):
#         for k in range(B[i],B[i]+10):
#             background[j][k]=1 # 색종이가 있는 부분을 1로 표시
            
# result=sum(sum(row) for row in background)
# print(result)


# print("=================================================")

# 백준 - 2720

# 심지어 $0.5달러를 줘야하는 경우에 거스름돈으로 $5달러를 주는것이다!
# 거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 
# 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
# 거스름돈은 5달러 이하

# price_list={
#     "Q":0.25,
#     "D":0.10,
#     "N":0.05,
#     "P":0.01    
# }

# # 테스트 케이스의 개수
# n=int(input())
# result=[]

# for i in range(3):
#     m=float(input())
#     result.append(m)
    
# print(price_list.items())

# price_list["Q"]=int(m[i]//price_list["Q"])
# print(price_list["Q"])