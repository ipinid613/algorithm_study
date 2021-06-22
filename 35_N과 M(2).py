#combinations 이용한 풀이

from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
print(arr)

answer = list(combinations(arr, M))

for element in answer:
    for element2 in element:
        print(element2, end = " ")
    print()


# dfs함수 만들어서 풀기..
# N, M = map(int, input().split(" "))
# lst = [i for i in range(1, N + 1)]
# check_list = [False] * N
#
# arr = []
#
#
# def dfs(cnt):
#     if cnt == M:
#         print(*arr)
#         return
#
#     for i in range(N):
#         if check_list[i]:
#             continue
#         check_list[i] = True
#         arr.append(lst[i])
#         dfs(cnt + 1)
#         arr.pop()
#
#         for j in range(i + 1, N):
#             check_list[j] = False
#
#
# dfs(0)