import sys

num = int(sys.stdin.readline())  #점의 개수 입력값

array_xy = []   # 빈배열 설정

for i in range(num): #for문을 통해 x, y좌표 받기
    x, y = map(int, sys.stdin.readline().split(' '))
    array_xy.append([y, x]) #빈배열에 y, x 순으로 추가

sorted_array = sorted(array_xy)  # 추가된 배열을 순서대로 정렬

for x, y in sorted_array:  # 순서대로 출력
  print(y, x)