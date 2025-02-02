
# 666->1666->2666->3666-> ...

num=int(input())

result=666
count=0

while True:
    if '666' in str(result):
        count +=1
    if count == num:
        break
    result +=1
    
print(result)