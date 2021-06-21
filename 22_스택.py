#https://rectanlgehihat.tistory.com/17 참조!! 정효윤님 게시글

import sys

n = int(sys.stdin.readline())

stack = []  # 정수를 저장할 빈 리스트(스택) 초기화

for _ in range(n):  # 주어지는 명령어 수만큼 반복 한다.
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])