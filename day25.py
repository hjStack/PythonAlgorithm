

# 문자를 아스키코드로 변환 

# # 문자 -> 아스키코드로
# a=input()
# print(ord(a));

# # 아스키코드 -> 문자 : chr()

# 공백 단위로 문자 구분하기 

# str=input()
# count=0;

# st=len(str.split())
# print(st)

# print("======================================================");

# 소수 구하기 - prime number ⭐️
# 1과 자기 자신외에는 어떠한 수로도 나누어 떨어지지 않는 경우
# 특정수 N이 소수인지 아닌지 구하는 법은 2부터 N-1까지의 해당 수를 나눠보고 이 과정에서 
# 어떠한 수에 의해 나누어 떨어지는지 확인하는 것
# 나누어 떨어지면 해당 수는 소수이고, 다른 수에 의해 나누어 떨어진다면 그 수는 소수가 아님

# def isPrime_number(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2,n-1):
#             if n%i == 0:   # 소수가 아님
#                 return False
#     return True

# n=int(input())
# m=list(map(int,input().split()))
# count=0

# for i in range(n):
#      if isPrime_number(m[i]):
#         count+=1
        
# print(count)

# print("======================================================");

# 소수의 합과 최솟값 
# 처음만나는 값이 최솟값이다 

def isPrime_number(n):
    if n<=1:
        return False
    else:
        for i in range(2,n-1):
            if n%i == 0:   # 소수가 아님
                return False
    return True

n=int(input())
m=int(input())
count=0
sum=0
min1=0

# n=60이고 m=100인경우 

for i in range(n,m+1):
    if isPrime_number(i):
        sum = sum +i
        if min1==0: # 가장 처음 발견된 수가 가장 작은 값이므로 대입
            min1=i 
            
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min1)

 