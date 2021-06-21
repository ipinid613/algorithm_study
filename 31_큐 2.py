import sys
from collections import deque

n = int(sys.stdin.readline())

que = deque()   # 빈 큐 만들기

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        que.append(command[-1])     # print(que) -> deque(['1'])

    elif command[0] == 'pop':   # 큐는 선입선출이므로 popleft() 메소드사용
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif command[0] == 'size':
        print(len(que))

    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':  # 큐의 가장 앞 인덱스는 0
        if not que:
            print(-1)
        else:
            print(que[0])

    elif command[0] == 'back':  # 큐의 가장 마지막 인덱스는 -1
        if not que:
            print(-1)
        else:
            print(que[-1])