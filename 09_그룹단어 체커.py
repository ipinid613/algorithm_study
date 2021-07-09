#1안
# n = int(input())    # 단어 개수/ aaabb
#
# for _ in range(n):  # 단어의 개수만큼 반복문 돌림(각 단어 안의 알파벳 확인하는)
#     word = input()  # 단어 입력을 받고 / happy/new
#     for i in range(len(word) - 1):  # 그 단어의 길이-1만큼 반복을 할건데(-1인 이유는 단어의 다음인덱스와 비교할거니까 마지막 단어는 비교할 필요가 없어서) - happ / ne 까지만.
#         if word[i] != word[i + 1]:  # 단어의 i번째 인덱스와 그 다음 인덱스가 다르다면, i+1부터는 i번째 인덱스에 있는 알파벳이 나오면 안됨
#             if word[i] in word[i + 1:]:     # 근데 i번째 인덱스의 알파벳이 그 다음 인덱스부터 검사했을 때 나왔다면 그룹단어가 아니게 되므로
#                 n -= 1      # 첫쨋줄에서 입력받은 단어의 개수에서 하나를 빼고
#                 break       # 다음 단어 검사하러 다시 첫 for문으로 돌아감(break는 if안의 조건 성립 시, 가장 가까운 반복문을 빠져나감)
# print(n)

#2안
n = int(input())

count = n
for _ in range(n):
    word = input() # aba happy
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            count -= 1
            break
print(count)

word = 'abcbad'
print(word.find(word[1]))