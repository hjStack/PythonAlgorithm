
# 백준 - 3003

# 체스는 총 16개의 피스를 사용하며, 
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

## 체스의 구성 개수를 리스트로 담아 놓고 
# result=[1,1,2,2,2,8]
# result1=list(map(int,input().split()))

# for i in range(0,6):
#     print(result[i]-result1[i],end=' ')


# 백준 - 2941
# 크로아티아에서 변경된 문자를 리스트에 저장하고
# 특정 문자로 변경하고 특정문자의 개수를 세면 됨 

# a=['c=','c-','dz=','d-','lj','nj','s=','z=']

# wtr=input().strip()
# # strip() : 공백 제거 

# for i in a:
#     wtr=wtr.replace(i,'*')
    
# print(len(wtr)