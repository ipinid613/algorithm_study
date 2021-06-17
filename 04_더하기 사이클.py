#내가 푼 답안(str로 계산하기)
import sys

n = str(sys.stdin.readline().strip('\n'))
num = n
cnt = 0
while True:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))  # str '8'
    num = num[-1] + plus  # str '68' #[-1] = 제일 끝자리의 것 선택! / [-1]로 선택을 안 해두면 num이 세자리가 되는 경우 발생하여 오류남.
    cnt += 1
    if num == n:
        print(cnt)
        break

# import sys
#
# n = int(sys.stdin.readline()) # // int 68
# num = n
# cnt = 0
#
# while True:
#     a = num // 10 # // int 6
#     b = num % 10 # // int 8
#     c = (a+b) % 10 # // int 1"4" == 나머지 4
#     num = (b*10) + c # // 80 + 4
#
#     cnt += 1
#     if(num == n):
#         break
# print(cnt)