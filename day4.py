
# 백준 - 2739

# num1=int(input())

# for n in range(1,10):
#     print(num1,'*',n,'=',num1*n)

# print()

# 백준 - 8393
# num2=int(input())
# print(sum(range(0,num2+1)))

# print()

# 백준 - 25304

# total=int(input())
# productNum=int(input())
# sum1=0

# for i in range(0,productNum):
#     num1,num2=map(int,input().split())
#     result=num1*num2
#     sum1+=result
    
# if sum1 == total:
#     print('Yes')
    
# else:
#     print('No')
    

# 백준 - 15552

# import sys

# num3=int(input())

# for i in range(1,num3+1):
#     n1,n2=map(int, sys.stdin.readline().split())
#     print(f'Case #{i}: {n1} + {n2} = {n1+n2}')
    

# 백준 - 2438

# num=int(input())
    
# for n in range(1,num+1):
#     print(' ' * (num-n) +'*' * n)
    
# = 공백을 더할땐 그냥 input값에서 초기값만 빼서 하면 됨 

# 백준 - 10952

# while 1:
#     n1,n2=map(int, input().split())
    
#     if n1 == 0 and n2 == 0:
#         break
#     else:
#         print(n1+n2)
        
        
# 백준 - 25314

a=int(input())

answer='int'

for i in range(a//4):
    print('long',end=' ')  #개행하지 않고 한 줄에 출력, 각 단어 사이에 공백 추가

print(answer)