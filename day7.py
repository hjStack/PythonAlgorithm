
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

# num=int(input())

# for i in range(num):
#     line = input().split()  # 공백으로 나눔
#     n1 = int(line[0])  # 첫 번째 값은 정수
#     s = line[1]  # 두 번째 값은 문자열

#     # 출력
#     result = ''.join([char * n1 for char in s])  # 각 문자를 n1번 반복 # char * n1 : 현재문자를 n1번 반복
#     print(result)
    
# 백준 - 1546

# score=int(input())
# num1=list(map(int,input().split()))
# data_r=list(map(int,num1)) # 리스트 요소를 정수로 변환 

# # print(data_r)
# m=max(data_r)

# sum1=sum(data_r)

# result=sum1*100/m/score
# #(A / M * 100 + B / M * 100 + C / M * 100) / 3 
# # = (A + B + C) * 100 / M / 3 = 총합 * 100 / 최댓값 / 개수

# print(result)

# 백준 - 3052 -> Set() : 중복을 허용하지 않는 집합 

unique_results = set()  # 중복을 허용하지 않는 집합 생성

for i in range(10): 
    data_r = map(int, input().split()) 
    for num in data_r: 
        result=num%42
        unique_results.add(result)  # 결과를 집합에 추가
        
print(len(unique_results))  # 서로 다른 결과의 개수 출력
        
    