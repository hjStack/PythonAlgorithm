
# 체스는 총 16개의 피스를 사용하며, 
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

## 체스의 구성 개수를 리스트로 담아 놓고 
result=[1,1,2,2,2,8]
result1=list(map(int,input().split()))

for i in range(0,6):
    print(result[i]-result1[i],end=' ')