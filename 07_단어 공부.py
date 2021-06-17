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

import sys

words = sys.stdin.readline().upper().strip('\n')
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])




















