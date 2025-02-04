import sys

num=int(sys.stdin.readline())
result=[]

for i in range(num):
    result.append(sys.stdin.readline().strip()) # input()은 느림
sorted_list=set(result) # 중복 제거후 리스트로 전환해서 sort()
lst=list(sorted_list)
lst.sort() # sort() : 리스트 내에서만 정의될 수 있다, 
# list.sort() 함수는 기본적으로 리스트를 오름차순으로 정렬해주는 기능을 합니다.
lst.sort(key=len)

for i in lst:
    print(i)
    
# 새로운 정렬된 리스트를 반환하는 함수는 sorted 함수이고, 
# 리스트 자체를 정렬시켜버리는 것은 sort 함수입니다.
