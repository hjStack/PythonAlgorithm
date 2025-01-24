
# 백준 - 5073,삼각형과 세변

while True:
    a, b, c = list(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break

    elif a+b<=c or b+c<=a or a+c<=b:
        print('Invalid')
   
    elif a == b and b == c:
        print('Equilateral')
        
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
