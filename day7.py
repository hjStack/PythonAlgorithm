
# 백준 - 5622

# writing=input()
# count=0

# for i in writing:
#     if i in "ABC":
#         count+=3
        
#     elif i in "DEF":
#         count+=4
    
#     elif i in "GHI":
#         count +=5
    
#     elif i in "JKL":
#         count+=6
#     elif i in "MNO":
#         count +=7
    
#     elif i in "PQRS":
#         count +=8
    
#     elif i in "TUV":
#         count +=9
#     else:
#         count+=10
        
# print(count)
    
    
# 똑같은 문제 리스트 형식으로도 출력해보기 

# dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

# writing=input()
# count=0

# for i in range(len(writing)):
#     for j in dial:  # 탐색 과정 
#         if writing[i] in j:
#             count += dial.index(j)+3
            
# print(count)

# 백준 - 2675
import sys

num=int(input())

for i in range(num):
    line = input().split()  # 공백으로 나눔
    n1 = int(line[0])  # 첫 번째 값은 정수
    s = line[1]  # 두 번째 값은 문자열

    # 출력
    result = ''.join([char * n1 for char in s])  # 각 문자를 n1번 반복 # char * n1 : 현재문자를 n1번 반복
    print(result)
    