
# 백준 - 1316

# 그룹단어 : 각 문자가 연속해서 나타나는 경우만을 말함 

# def check_string(s):
#     seen = set()  # 등장한 문자를 저장할 집합
#     last_char = ""  # 마지막으로 확인한 문자
    
#     for i in s:
#         if i != last_char:
#             if i in seen: # 연속된 문자가 아니고 이미 등장했다면 
#                 return False
#             seen.add(i)
#         last_char=i
#     return True


# num=int(input())
# count=0

# for i in range(0,num):
#     word=input()
    
#     if check_string(word):
#         count +=1
        
# print(count)

# 백준 - 25206

# 학점 * 과목평점 
# GPA = (학점*과목평점) / 학점의 총합

rating=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
grade=['A+','A0','B+','B0','C+','C0','D+','D0','F']

result=0
o=0

for i in range(0,20):
    a,b,c=input().split()
    b=float(b)
    
    if c == 'P':
        continue
    
    else:
        result += b*(rating[grade.index(c)])
        o+=b
        
print(result/o)
        
    
    
    
    
    
    