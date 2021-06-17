N = int(input())

result = 0

while N >= 0:
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break

    N -= 3
    result += 1

else:
    print(-1)

#     N   3kg  5kg    번
#     3   1           1
#     4              -1
#     5        1      1
#     6   2           2
#     7              -1
#     8   1    1      2
#    18   1    3      4

#  ex)
#     N이 18인 경우:
#    18 - 3 = 15 ->> result + 1
#    15 % 5 == 0 ->> result + 3 (result += (15 // 5))

#    result = 4번


#    N이 7인 경우:
#     7 - 3 = 4  ->> result + 1
#     4 - 3 = 1  ->> result + 1
#     1 < 3 ->> print(-1)

#    -1 출력


# point)
#     while에 조건식 대신 True를 지정하면 무한히 반복하는 무한 루프가 만들어진다
#     조건식이 항상 참이니 끝없이 실행되는것
#     콘솔에서 Ctrl + C 누르면 루프가 끝남
#     True 대신에 다른 값을 넣을 수 있음 ex) 내용이 있는 문자열이나 0이 아닌 숫자는 True로 취급