

# 백준 - 2743

# str=input()
# print(len(str))

# 백준 - 9086

# test_n=int(input())

# result=[]

# for i in range(test_n):
#     str=input()
#     result.append((str[0],str[-1])) # 튜플로 묶어서 추가
    
# # insert는 특정 인덱스에 값을 넣을 때 사용되며, append는 리스트 끝에 값을 추가하는 데 적합합니다

# for f,l in result:
#     print(f'{f}{l}')

# 백준 - 27866

# str=input()
# n=int(input())

# print(str[n-1])

# 백준 - 11654

# str=input()
# print(ord(str))

# ord함수는 문자를 아스키코드로 변환해주는 함수
# chr함수는 아스키코드를 문자로 변환해주는 함수


# 백준 - 11720

# num1=int(input())
# m=input()

# sum1=0

# for i in range(num1):
#     sum1 += int(m[i])
    
# print(sum1)

# 백준 - 10809
# m=input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in m:
#         print(m.index(i),end = ' ')
#     else:
#         print(-1,end=' ')


# 백준 - 1152
# 문장을 공백 단위로 나누어서 단어의 개수 세기
# sentence=input()

# se=sentence.split()
# word_count=len(se)
# print(word_count)

# while True:
#     try:
#         a=input()
#         print(a)
#     except:
#         break

# 백준 - 2908

n,m=map(int,input().split())

# 정수를 역순으로 처리하려면, 먼저 정수를 문자열로 변환한 후 이를 역순으로 처리하고, 
# 필요에 따라 다시 정수로 변환하는 과정을 거쳐야 합니다.

result1=int(str(n)[::-1])
result2=int(str(m)[::-1])

# print(result1,result2)

if result1 > result2:
    print(result1)
else:
    print(result2)


    
    