# 1. 내 답안

import sys
import math

n,k = map(int, sys.stdin.readline().split()) # 5 2

answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(answer)

# 2. 재귀함수 사용
# import sys
# def make_fac(num): #5*4*3*2*1
#     return num * make_fac(num-1) if num != 1 else 1
# n,k = map(int, sys.stdin.readline().split())
#
# answer = make_fac(n) // (make_fac(k)*make_fac(n-k))
# print(answer)