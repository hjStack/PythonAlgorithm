
from collections import Counter

word=input().strip().upper()

Counter=Counter(word)

# 가장 많이 등장한 알파벳 # 튜플 
common=Counter.most_common()
# Counter.most_common()은 (키, 값) 형태의 튜플을 빈도 순으로 
# 정렬하여 리스트로 반환합니다.

# 등장 횟수가 가장 많은 알파벳을 확인
if len(common) > 1 and common[0][1] == common[1][1]:
    print('?')  # 가장 많이 사용된 알파벳이 여러 개일 경우
else:
    print(common[0][0])  # 가장 많이 사용된 알파벳 출력