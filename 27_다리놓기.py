import sys
import math

num = int(sys.stdin.readline().rstrip())

for i in range(0, num):
    n, m = map(int, sys.stdin.readline().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(bridge)


#   n     m     결과
#   1     2      2
#   2     4      6
#   4     9      126