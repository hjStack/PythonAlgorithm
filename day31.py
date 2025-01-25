
# 브루트 포스 알고리즘
# brute : 무식한
# 일반적 방법으로 문제를 해결하기 위해서는 모든 자료를 탐색해야 하기 때문에 
# # 특정한 구조를 전체적으로 탐색할 수 있는 방법을 필요로 한다.
# 알고리즘 설계의 가장 기본적인 접근 방법은 해가 존재할 것으로 
# 예상되는 모든 영역을 전체 탐색하는 방법이다

# TypeError: int() argument must be a string, 
# a bytes-like object or a real number, not 'list'

# 그냥 int(input().split()) 하면 
# 하나씩 일일이 형변환을 해줘야 하기때문에 사용하기 불편함
# -> 해결책 : map()

# 1 3 -1 4 1 7
# 1x + 3y  = -1
# 12x + 3y = 21
# -11x = -22, x=2 y = -1
# 2 + 3y = -1 , 3y=-3 

# a,b,c,d,e,f = map(int, input("").split())

# for i in range(-999,1000):
#     for j in range(-999,1000):
#         if a*i + b*j == c and d*i+e*j==f:
#             print(i,j)

# print("===============================")

# 체스판 다시 칠하기 - 1018
# 체스판은 검은색과 흰색으로 번갈아서 칠해져 있어야 함 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서 지민이는 8*8 크기의
# 체스판으로 잘라낸 후에 몇개의 정사각형으로 다시 칠해야겠다고 생각했다
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 
# 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# num1,num2=map(int,input().split())
# result=[] # 원래의 판을 저장하기 위한 리스트 result
# title=[]  # 다시 칠한 체스판 

# for k in range(num1):
#     result.append(input())

# for i in range(num1-7):  # i ~ i+7 까지 8줄
#     for j in range(num2-7):    # j ~ j+7 까지 8칸
#         cnt1=0 # 시작이 검은색일경우
#         cnt2=0 # 시작이 흰색일경우
        
#         for a in range(i,i+8):
#             for b in range(j,j+8):
#                 if (a+b) % 2 == 0:   # 짝수줄인경우 
#                     if result[a][b] != 'W':
#                         cnt1 +=1
#                     if result[a][b] != 'B':
#                         cnt2+=1
#                 else: # 홀수줄인경우
#                     if result[a][b] != 'B':
#                         cnt1 +=1
#                     if result[a][b] != 'W':
#                         cnt2 += 1
                        
#         title.append(min(cnt1, cnt2))
    
# print(min(title))


# =========================== 

# 복습 해보깅 - 코딩은 체육과목 입니다 

n1=int(input())

for i in range(n1//4):
    print('long',end=' ')
    
print('int')