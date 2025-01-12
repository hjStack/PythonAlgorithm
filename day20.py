
a = int(input())
b = int(input())
c = int(input())

# 1) 세 각의 합이 180인지?
if a + b + c != 180:
    print("Error")
else:
    # 2) 정삼각형(Equilateral) 체크
    if a == b == c:
        print("Equilateral")
    # 3) 이등변삼각형(Isosceles) 체크
    elif a == b or b == c or c == a:
        print("Isosceles")
    # 4) 나머지 경우(Scalene)
    else:
        print("Scalene")
