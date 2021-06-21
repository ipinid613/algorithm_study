# 문제
# 스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때
# 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop)
# 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는
# (LIFO, Last in First out) 특성을 가지고 있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들
# 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

# 입력값:
# 8  총 입력횟수
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# 입력값에 따른 출력값
# 1 2 3 4 + + + +  4까지 쌓임
# 1 2 (3 4) - -    4, 3 순으로 빠진다
# 1 2 5 6 + +      5, 6이 추가됨
# 1 2 5 (6) -      6이 빠짐
# 1 2 5 7 8 + +    7, 8이 추가됨
# 1 2 5 7 (8) -    8이 빠짐
# 1 2 5 (7) -      7이 빠짐
# (1 2 5) - - -    5, 2, 1 순으로 빠짐

# <문제해결>
# 스택에 넣었다가 뽑아 늘어 놓는다 == pop으로 뽑아낸 순서가 입력값 순이다.
# push 하는 순서는 오름차순으로 1=>8로 진행된다.
# 스택을 이용해 해당 수열을 만들 수 없을 경우 NO를 입력한다.

# 1. 첫번째 입력값을 받아 for 문을 통해 반복할 수 있게 만든다.
# 2. count를 담을 수 있는 변수와 +, - 를 담을 수 있는 빈 배열과 스택의 빈배열과 불린값을 받는 메세지를 만든다.
# 3. for문과 입력값을 받는 변수를 지정한다.

num = int(input())
count = 0
result = []
stack = []
no_message = True

for i in range(num):
    input_data = int(input())

    while count < input_data:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == input_data:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        break

if no_message == False:
    print("NO")
else:
    print("\n".join(result))