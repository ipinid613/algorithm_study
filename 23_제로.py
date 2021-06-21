import sys

n = int(sys.stdin.readline())
z = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        z.pop()
    else:
        z.append(num)

print(sum(z))


# pop()은 리스트에서 맨 마지막 요소를 출력하면서 그 요소를 리스트에서 삭제하는 함수.
# 특정 위치에 있는 요소에 대해서 사용하려면 pop(x)와 같이 x인자를 넣어주면 된다.
# 뒤에서 x번째 값을 꺼내고 싶다면 pop(-x)를 사용한다.

# 파이썬 리스트 값 삭제

# clear()   모든 요소 삭제
# pop()   지정한 위치 값을 삭제하고 삭제한 값 취득
# remove()   지정한 위치 값과 같은 값을 검색후 처음 값을 삭제
# del   위치 또는 범위를 지정 삭제
# del은 함수가 아니라 예약어이다. 그렇기 때문에 함수와 같이 사용할 수 없다.
# 사용방법은 del 뒤에 한 칸을 띄고서 'del array [인덱스]' 형태로 사용한다.