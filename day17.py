
# 백준 - 10798
result=[]

# 숫자를 저장할 리스트를 선언해서 리스트에 붙이고 
for i in range(5):
    n=input()
    result.append(n)
    
# 새로 저장할 문자열의 변수를 만듦
output=""

maxlen = max(len(word) for word in result)
# print(maxlen)

for i in range(maxlen):
    for j in range(5):
        if i<len(result[j]):
            output+=result[j][i]
            
print(output)

 
        
        
# 백준 - 27323

# n=int(input().strip())
# m=int(input().strip())

# area=n*m
# print(area)

# 백준 - 한수의 현재위치와 오른쪽 위 꼭짓점 사이까지의 최소 거리 - 1085
# x, y, w, h = map(int,input().split())
# a=w-x
# b=h-y

# # 문제 예시로 보면 (4,1)
# print(min(x,y,a,b))

# 백준 - 3009
