
# OX 퀴즈
# O는 문제를 맞은 것이고, X는 문제를 틀린 것

test_n=int(input())

for i in range(test_n):
    problem=input()
    # result.append(problem)  # 인덱스가 아니라 problem을 넣어야 함
    count=0
    total=0  # 누적 점수를 구할 변수 
    # 여기서 변수를 total를 선언하는 이유는 다음줄로 넘어갈때 
    # 0으로 초기화 해주기 위함

    for j in range(0,len(problem)):
        if problem[j] == 'O':
            count+=1
            total +=count
        elif problem[j] == 'X':
            count=0
            total+=0
        
    print(total)

# OOXXOXXOOO = 1+2+0+0+1+0+0+1+2+3 = 10
# OOXXOOXXOO = 1+2+0+0+1+2+0+0+1+2 = 9  

# 새로 배운 사실 ..
# input()은 str로 문자를 입력받기 때문에 문자열로 받아들여 
# 배열의 형태를 가지는것임 

