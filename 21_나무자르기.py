import sys
# 나무의 수, 원하는 나무의 길이
n, m = map(int, sys.stdin.readline().split())
# 나무의 높이
tree = list(map(int, sys.stdin.readline().split()))

# 목재절단기의 높이, 이분 탐색에 사용할 start와 end(left, right로도 많이 쓰임)
h = 0
start = 0
end = max(tree)

# 이분탐색 시작!!
# start가 더 커지면 (이분 탐색이 끝나면) 반복문을 종료한다.
while start<=end:
    # 자른 나무의 총 길이
    # 답을 구할 때, 자른 나무의 총 길이(s)가 원하는 길이(m)와 일치하는지 봐야해서 s가 필요함.
    s = 0
    # 임의로 설정한 절단기 높이
    middle = (start + end) // 2

    # 임의로 설정한 높이로 나무를 자른다.
    s = sum(i-middle if i > middle else 0 for i in tree)

    # 총 나무의 길이가 원하는 나무의 길이보다 길거나 같다면
    if s >= m:
        # 높이를 설정해주고 탐색을 반복한다. (*)
        h = middle
        start = middle + 1
    # 원하는 나무의 길이보다 짧으면 다시 높이를 탐색한다.
    else:
        end = middle - 1
print(h)