# 팩토리얼 구현하기 
# 사물의 순서를 정할때 얼마나 많은 방법이 있는지, 
# 어떤 것들을 조합할때 얼마나 다양한 방법이 있는지 구할때 유용하다

# def factorial_n(n):
#     result=1 # 맨 처음 초깃값을 1로 초기화하는게 중요하다
#     if n<=1:
#         n=0
#     for i in range(1,n+1):
#         result = result * i
#     return result
            
# n1=int(input())
# value = factorial_n(n1)
# print(value)

# # 10 ! = 3628800 = 10 X 9 X 8 X 7 X 6 X 5 X 4 X 3 X 2 X 1 
# # 5!=120 -> 5 4 3 2 1
# # 3!=6 

# # print("==========================")

# # print(type(None))  # <class 'NoneType'>
# # print(type(False)) # <class 'bool'>
# # print(None == False) # False

# print("================================")

# 하노이 탑 
# 첫번째 장대에서 세번째 장대로 옮기려 함 
 
# 한번에 한개의 원판만을 다른 탑으로 옮길 수 있음
# 쌓아 놓은 원핀은 항상 위의 것이 아래것봅다 작아야 함
# 원반의 이동횟수를 최소화하고자 할떄, 각 원반을 옮기는 모든 순서 출력

def hanoi(n,start,middle,target):
    # 그냥 막대의 개수를 파라미터로 주면 된다 ... !
   if n == 1:
       print(start,target) 
       # target은 옮기는 기둥이 a,b,c가 있다고 가정할때 a-c까지 가는 
       # 방법의 개수
   elif n>1 and n<=20:
       hanoi(n-1,start,target,middle)
       print(start,target)
       hanoi(n-1,middle,start,target)
                
# 첫번째 장대에 놓인 원판의 개수
n=int(input())

# n=3이면 첫번째 장대에 3개가 있음
# n개의 원판이 있을때 
# n=1이면 p(1)=1, p(2)=3, p(3)=7, p(4)=15
# 일반적으로  P(n)은  P(n-1)로 부터 유도할 수 있다.

result=2**n-1  
print(result)

hanoi(n,1,2,3)

# 재귀 함수 -> 같은 형태의 보다 작은 입력을 지닌 자기 자신을 호출하는것잉고
# 이렇게 재귀적인 호출을 사용하는 함수를 재귀함수라고 한다

