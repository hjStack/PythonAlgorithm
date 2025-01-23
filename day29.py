
n=int(input())
k=2 # 나누는 수 # 이것을 고정시켜 놓고 소인수분해를 구현하는 것이 핵심 

while(n != 1):
    if n % k !=0:
        k+=1
    else:
        n //=k
        print(k)


