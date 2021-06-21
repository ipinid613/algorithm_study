import sys
import math

def check(num):   ## 소수인지 체크하는 함수
    if num == 1:
        return False
    else:
        ## 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있으므로 하기 공식으로 구한다.
        for i in range(2, int(math.sqrt(num)+1)):
            if num%i == 0:
                return False
        return True

a,b = map(int, sys.stdin.readline().split(' '))

for i in range(a, b+1):
    if check(i):
        print(i)