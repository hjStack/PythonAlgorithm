
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

# 시간 복잡도4 - o(n ** 2 - n)

n=int(input())
print(int(n*(n-1) -(n-1)*n/2))

print(2)