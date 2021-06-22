import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
result = []     # 0이나 1만 가지고 있는 색종이 생기면 추가

def solution(x, y, N):
  num = paper[x][y]   # 변수에 각 정사각형 종이의 자리 할당 / paper[0][0] = 1
  for i in range(x, x+N):  # 시작점과 숫자가 같은지 반복문을 돌면서 확인
    for j in range(y, y+N):
      if num != paper[i][j]:  # 숫자가 다르면 4분할
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if num == 0:
    result.append(0)
  else: # color == 1
    result.append(1)


solution(0,0,N)
print(result.count(0))  # result의 0의 개수 -> 하얀 종이 개수
print(result.count(1))  # result의 1의 개수 -> 파란 종이 개수



# 정수를 n줄 입력받아 2차원 리스트에 저장
# paper = []
# for _ in range(N):
#     paper.append(list(map(int, sys.stdin.readline().split())))