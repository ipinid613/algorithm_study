t = int(input())    # 테스트 케이스 개수 입력 받음

for i in range(t):  # 테스트 케이스로 입력받은 수만큼 for문 반복
    h, w, n = map(int, input().split())   # h=각각 호텔의 층 수, w=각 층의 방 수, n=몇 번째 손님

    floor = n % h   # n번째 손님이 머무를 층수
    line = (n // h) + 1   # n번째 손님이 머무를 호수
    if floor == 0:  # 만약 층수가 0으로 떨어진다면 제일 꼭대기에 위치해 있는다는 뜻이므로
        floor = h   # 머무르는 곳과 층수의 값이 같아지고
        line -= 1   # 몫이 하나 늘어난걸 빼줘야 함

    print(floor * 100 + line)   # 방 번호는 YXX, YYXX형식이고 범위가 1 ≤ H,W ≤ 99 라고 주어졌으니 floor에 100을 곱해줌