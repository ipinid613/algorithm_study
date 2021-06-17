# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

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

natural_list = list(range(2, 246912))  # 문제에서 제한범위 1 ≤ n ≤ 123,456
decimal_list = []

num = int(input())

for i in natural_list:
    if check(i):
        decimal_list.append(i)

while num != 0:    ## 소수 갯수 구하기
    count = 0
    for i in decimal_list:
        if num < i <= num*2:  ## 문제: n보다 크고, 2n보다 작거나 같은 소수의 개수 구하기
            count += 1
    print(count)
    num = int(input())