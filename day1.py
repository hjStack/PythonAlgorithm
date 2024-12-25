
# print('Hello World!')

# 파이썬에서 입력받기
# 파이썬에서 입력받을때는 input()사용
# 변수 여러개의 값을 입력받으려면 split()사용 

# # # # 더하기 
# num1,num2=map(int,input().split())
# print(num1+num2)

# # # # 빼기 
# num1,num2=map(int,input().split())
# print(num1-num2)

# # # 곱하기 
# num1,num2=map(int,input().split())
# print(num1*num2)

# # 나누기 
# num1,num2=map(int,input().split())
# print(num1/num2)


# 사칙 연산 총집합
# num3,num4=map(int,input().split())
# print(num3+num4)
# print(num3-num4)
# print(num3*num4)
# print('%d' %(num3/num4))
# print(num3%num4)

# 파이썬 f-string
# text=input('')
# print(f'{text}??!')

# # 백준 - 10430
# n1,n2,n3=map(int,input().split())
# print((n1+n2)%n3)
# print(((n1%n3) + (n2%n3))%n3)
# print((n1*n2)%n3)
# print(((n1%n3) * (n2%n3))%n3)

# # 18108
# # input() 함수는 항상 문자열 형태로 입력값을 반환하기 때문에, 숫자 연산을 하려면 정수(int()) 또는 실수(float())로 변환이 필요합니다.
# n1=int(input())
# print(n1-543)

# print('\\    /\\')
# print(" )  ( ')")
# print('(  /  )')
# print(' \(__)|')
      
# print('|\_/|')
# print('|q p|   /}')
# print("( 0 )\"\"\"\\")
# print(r'|"^"`    |')
# print('||_/=\\__|')

# 백준 11382
# n1,n2,n3=map(int,input().split())
# print(n1+n2+n3)

# 백준 2588
# num1=int(input())
# num2=int(input())
# print(num1 * (num2%10))
# print(num1 * int((num2%100)/10))
# print(num1 * int(num2/100))
# print(num1*num2)