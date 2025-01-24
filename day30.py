
# # 백준 - 5073,삼각형과 세변

# while True:
#     a, b, c = list(map(int, input().split()))
#     if a == 0 and b == 0 and c == 0:
#         break

#     elif a+b<=c or b+c<=a or a+c<=b:
#         print('Invalid')
   
#     elif a == b and b == c:
#         print('Equilateral')
        
#     elif a == b or b == c or a == c:
#         print('Isosceles')
#     else:
#         print('Scalene')


# 알고리즘 - 수행시간 
# 시간 복잡도1 - o(1)

# count =0

# n=int(input())
# count +=1

# print(count)
# print(0)

# 시간복잡도2 - o(n)

# count =0

# n=int(input())
# count +=n

# print(count)
# print(1)

# 시간 복잡도3 - o(n**2)

# count =0

# n=int(input())
# count +=(n*n)

# print(count)
# print(2)

# 시간 복잡도4

# n=int(input())
# print(int(n*(n-1) -(n-1)*n/2))

# print(2)

# 시간 복잡도5 - o(n^^3)

# count =0

# n=int(input())
# count +=(pow(n,2)*n)

# print(count)
# print(2)

# n=int(input())
# print((n-2) * (n-1) * n // 6) #  ∑(k(k + 1) / 2)이고 전체 식을 풀어서 정리하면 n(n - 1)(n - 2) / 6
# print(3)

# ================================================

# 점근적 표기 
a,b=list(map(int,input().split()))
g=int(input())
n=int(input())

if (a*n + b <= g*n and a<=g):
    #  모든 n ≥ n0에 대하여 g(n)이 f(n)보다 크거나 같아야 하는데
    # 둘다 1차함수로 생각하면 f(n)의 기울기 = a 가 g(n)의 기울기 = c 보다 크게 되면 언젠가 f(n)이 더 커질 수밖에 없기 때문에
    # 기울기 c >= a 가 되어야 합니다.
    print(1)
else:
    print(0)