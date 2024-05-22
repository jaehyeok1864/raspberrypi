# 1초에 1씩 증가하는 값을 출력하는 프로그램(반복문 while)을 작성하시오.

#time모듈의 sleep 함수
from time import sleep 

print(1)
sleep(10)
print(2)

count = 1

#try except

try :
    while True:
        print(count)
        sleep(1)
        count = count + 1 # count += 1
except KeyboardInterrupt :
    print("반복을 종료합니다 !!!")