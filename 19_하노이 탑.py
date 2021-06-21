def hanoi(n, frm, to, otr):
    if n < 2:
        print(frm, to)       # frm에서 to로 이동
        return
    hanoi(n-1, frm, otr, to) # 맨 아래칸을 제외하고 frm에서 otr로 재귀적 이동
    print(frm, to)           # 맨아래 원반 목적지로 이동
    hanoi(n-1, otr, to, frm) # otr로 옮겼던 원반 to로 이동

n = int(input())
print((2**n)-1)
hanoi(n, 1, 3, 2)