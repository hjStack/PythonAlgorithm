
# 조건문 

# 백준 - 1330
# num1,num2=map(int,input().split())

# if num1>num2:
#    print('>')
# elif num1<num2:
#     print('<')
# else:
#     print('==')
    

# 백준 - 9498

# score=int(input())

# if (score>=90 and score<=100):
#     print('A')

# elif (score>=80 and score<=89):
#     print('B')
    
# elif (score>=70 and score<=79):
#     print('C')

# elif (score>=60 and score<=69):
#     print('D')
# else:
#     print('F')

# 문제를 잘 읽자 ⭐️

# 백준 - 2753

# 연도가 주어졌을때 윤년이면 1, 아니면 0
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

year=int(input())

if (year%4 == 0 and year%100!=0 or year%400 == 0):
    print('1')
else:
    print('0')

# print(year%4)

