
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

# year=int(input())

# if (year%4 == 0 and year%100!=0 or year%400 == 0):
#     print('1')
# else:
#     print('0')

# print(year%4)

# num1=int(input())
# num2=int(input())

# if num1>0 and num2>0:
#     print('1')
# elif num1<0 and num2>0:
#     print('2')
# elif num1<0 and num2<0:
#     print('3')
# elif num1>0 and num2<0:
#     print('4')


# # 백준 - 2480
# num1,num2,num3=map(int,input().split())

# if num1==num2==num3:
#     result=10000+num1*1000
#     print(result)

# elif num1 == num2:
#     result1=1000+num1*100
#     print(result1)
    
# elif num2 == num3:
#     result2=1000+num2*100
#     print(result2)
    
# elif num1 == num3:
#     result3=1000+num1*100
#     print(result3)

# elif num1 != num2 and num2 != num3:
#      result4=max(num1,num2,num3)*100  
#      print(result4)
     
     
# # 백준 - 2525
# # 현재 시각과 요리시간 
# currentHour,currentMinute=map(int,input().split())
# cookingTime=int(input())

# currentHour += cookingTime//60  # 몫 
# currentMinute += cookingTime%60 # 나머지 

# if currentMinute>=60:
#     currentHour+=1
#     currentMinute-=60
    
# if currentHour>=24:
#     currentHour-=24

# print(currentHour,currentMinute)

# 백준 - 2884
hour,minute=map(int,input().split())

if minute>=45:
    minute-=45

else:
    minute+=15
    if hour==0:
        hour=23
    else:
        hour-=1
    
print(hour,minute)