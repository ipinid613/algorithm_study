# 문제 조건
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

# 입력값 정의
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

# 출력값 정의
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

# 배열 리스트에 일치하는 조건이 있으면 먼저 삽입 후, pop을 통해 제거
# 배열이 0일 경우 YES, 0이 아닐경우 NO로 출력


while True:
    word = input()
    bracket = []

    if word[0] == ".":  # "."일때 break를 걸어 진행 방지
        break

    for i in word:
        if i == "(" or i == "[":  # "(, [" 이 있을 때, 배열에 삽입
            bracket.append(i)
        elif i == ")":
            if len(bracket) != 0 and bracket[-1] == "(":
                bracket.pop()
            else:
                bracket.append(")")
                break
        elif i == "]":
            if len(bracket) != 0 and bracket[-1] == "[":
                bracket.pop()
            else:
                bracket.append("]")
                break

    if len(bracket) == 0:
        print("yes")
    else:
        print("no")