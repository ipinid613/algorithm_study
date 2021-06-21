# * 괄호 문자열(Parenthesis String, PS) -> 두개의 괄호 기호"(" 와 ")" 만으로 구성되어 있는 문자열
# * 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# * 한 쌍의 괄호 기호로 된 "()" 문자열 -> 기본 VPS
# * x가 VPS라면 (괄호로 이루어져 있다면) "(x)"도 VPS
# * y도 VPS라면 xy도 VPS

N = int(input())
for i in range(N):
    vps = input()
    vps_list = list(vps)
    sum = 0
    for i in vps_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')