
# # 분수 찾기 
# n=int(input()) 
# count=1  # 전체 분수 개수 누적

# # 분자, 분모 변수를 따로 선언 
# mole=0 # 분자
# deno=0 # 분모

# # 1라인 : 1/1
# # 2라인 : 1/2 → 2/1
# # 3라인 : 3/1 → 2/2-> 1/3

# # 이러한 결과를 통해 짝수라인은 분모가 1씩 줄어들고, 분자는 1씩 늘어남
# # 홀수라인은 분모가 1씩 늘어나고, 분자는 1씩 줄어든다

# # n이 2면 1/2

# while n > count:
#     n-=count 
#     count+=1

# if count % 2 == 0:
#     mole=n
#     deno=count-n+1
    
# else:
#     mole =count-n+1
#     deno =n
    
# print(mole, '/', deno, sep='')    

# print("======================================================")  # 구분선 

    
# 완전수 
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면 그 수를 완전수 
# 예를 들어 6=1+2+3으로 완전수 # 6의 약수는 1,2,3,6
# n이 완전수인지 아닌지 판단 

while True:
    n=int(input())
    if n == -1:
        break;
    result=[]
    for i in range(1,n):
        if n % i ==0:
            result.append(i)
        
# print("n을 제외한 약수 목록:", result)

    # while문 안에서 더하는것임
    if sum(result) == n:
        print(n, " = ", " + ".join(str(i) for i in result), sep="")

    else:  
        print(n, "is NOT perfect.")