
# # 백준 - 10807
# n=int(input())
# a = list(map(int, input().split()))
# find_number=int(input())

# count=0

# for num in a:
#     if num == find_number:
#         count+=1
    
# print(count)


# 백준 - 10871

# n,x=map(int,input().split())
# a = list(map(int, input().split()))

# for num in a:
#     if num < x:
#         print(num)


# 백준 - 10818
# n = int(input())

# numbers = list(map(int, input().split()))

# mi=min(numbers)
# ma=max(numbers)

# print(mi,ma)

# 백준 - 2562
# 리스트는 꼭 초기화 하기 !!
# numbers=[]

# for i in range(0,9):
#     n=int(input())
#     numbers.append(n)

# ma=max(numbers)
# print(ma)
# print(numbers.index(ma)+1)  # 특정 숫자 인덱스 찾기

# 백준 - 5597
student=[i for i in range(1,31)]

for i in range(28):
    num=int(input())
    student.remove(num)
    
for a in range(len(student)):
    print(student[a])
    
# 30명의 학생 리스트를 만들고 제출한 학생수를 제거하고 남은 2명은 제출하지 않은 것이므로 
# 2명의 인덱스를 처음부터 출력