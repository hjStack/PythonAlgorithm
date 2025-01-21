
# 1/21

x_result=[]
y_result=[]

for i in range(3):
    x,y=list(map(int,input().split()))
    x_result.append(x)
    y_result.append(y)
   
# print(x_result)
# print(y_result)

# 여기까지 결과  
[5, 5, 7, 7]
[5, 7, 5, 7]

# 출력은 7,7이 나와야 함

for i in range(3):
    if x_result.count(x_result[i]) == 1:
        x1=x_result[i]
    
    if y_result.count(y_result[i]) == 1:  # y 값이 리스트에서 한 번만 나타나는 경우
        y1 = y_result[i]
        
print(x1,y1)  
# count() : x_result라는 배열에서 x의 특정 글자가 몇개있는지 찾는 함수