
a, b = map(int, input().split())
score=list(map(int,input().split()))  # a개 입력받기 

result=sorted(score,reverse=True)  # 정렬 함수 
print(result[b-1])

