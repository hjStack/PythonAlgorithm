
a, b = map(int, input().split())
score=list(map(int,input().split()))  # a개 입력받기 

result=sorted(score,reverse=True)  
# 정렬 함수 : 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.
print(result[b-1])

