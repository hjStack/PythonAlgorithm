
# 상근이는 숫자 카드 N개를 가지고 있음 
# 정수 M개가 주어졌을때 이 수가 적혀있는 숫자 카드를 상근이가 가지고
# 있는지 아닌지 구하는 프로그램

# 리스트에 담으면 O(N)의 시간이 걸림
# set을 사용하면 평균 O(1)시간에 가능하므로 O(N+M)의 시간복잡도 

# set()
import sys

N=int(sys.stdin.readline().strip()) # 숫자 카드 개수 
cards=set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())  # 확인할 숫자 개수
queries = map(int, sys.stdin.readline().split())  # 확인할 숫자들

print(" ".join("1" if num in cards else "0" for num in queries))
# # 문자열 합치기 

import sys

n1 = int(sys.stdin.readline().strip())  # 출입 기록 수
# strip() : 문자열내에서 공백 제거 

company=set()

for _ in range(n1):
    name,action=sys.stdin.readline().split()
    
    if action == "enter":
        company.add(name)
    elif action == "leave":
         company.discard(name)

for person in sorted(company,reverse=True):
    print(person)


