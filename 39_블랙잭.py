#브루트포스 방식으로 문제를 해결한다. == 모든 경우의 수를 탐색한다!
n, m = map(int, input().split())
numlist = list(map(int, input().split()))

answer = 0
for i in range(len(numlist)):
    for j in range(i + 1, len(numlist)):
        for k in range(j + 1, len(numlist)):
            sum = numlist[i] + numlist[j] + numlist[k]

            if sum <= m:
                answer = max(answer, sum)

print(answer)