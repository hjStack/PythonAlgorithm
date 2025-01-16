
# 평균은 넘겠지 - 4344
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다

Test_n=int(input())

avg=0

for i in range(Test_n):
    n=list(map(int, input().split()))
    # 5 50 50 70 80 100 : 이 한줄을 리스트로 입력받음 

    avg=sum(n[1:])/n[0]  #n[0] : 학생수
    # print(avg)
    
    count=0  # 여기서 카운트를 초기화하는게 중요함
    
    for j in n[1:]:
        if j > avg:
            count+=1

    print('%.3f' %(count/n[0]*100) + '%')