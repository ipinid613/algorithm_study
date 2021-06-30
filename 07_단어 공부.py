# def find(string):
#     alphabet_array = [0]*26
#
#     for phrase in string:
#         if not phrase.isalpha():
#             continue
#         occurrency = ord(phrase.lower()) - ord("a") # == 0
#         alphabet_array[occurrency] += 1
#
#     max_alphabet = alphabet_array[0]
#     for a in alphabet_array:
#         if a > max_alphabet:
#             max_alphabet = a
#         b = alphabet_array.index(max_alphabet) #1
#         c = chr(b+97).upper()
#     return c
#
# result = find('aasdasd')
# print(result)

# import sys
#
# words = sys.stdin.readline().upper().strip('\n')
# unique_words = list(set(words))
#
# cnt_list = []
# for x in unique_words:
#     cnt = words.count(x)
#     cnt_list.append(cnt)
#
# if cnt_list.count(max(cnt_list)) > 1:
#     print('?')
# else:
#     max_index = cnt_list.index(max(cnt_list))
#     print(unique_words[max_index])


#시간초과 = word를 반복하여 꺼내서 cnt하면, sszzz의 경우 22333이 cnt_list에 입력됨.
#만약 1,000,000의 길이를 가진 단어가 입력된다면 cnt_list는 1,000,000의 length를 가지게 되므로 연산이 늦어짐.
# import sys
# word = list(sys.stdin.readline().rstrip().upper())
# cnt_list = []
#
# for i in word:
#     cnt = word.count(i)
#     cnt_list.append(cnt)
#
# if cnt_list.count(max(cnt_list)) == cnt_list.count(min(cnt_list)):
#     print('?')
# else:
#     max_word = cnt_list.index(max(cnt_list))
#     print(word[max_word])

import sys
word = sys.stdin.readline().rstrip().upper()
cnt_list = []
unique_word = list(set(word))

for i in unique_word:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_word = cnt_list.index(max(cnt_list))
    print(unique_word[max_word])




















