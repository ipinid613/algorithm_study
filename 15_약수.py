N = int(input())
A = list(map(int, input().split()))

max_num = max(A)
min_num = min(A)

print(max_num * min_num)


# ex) 12 = [2, 3, 4, 6] -> (2 * 6 = 12)

# ex) 24 = 2, 3, 4, 6, 8, 12 -> (2 * 12 = 24)

# input ->
# 2
# 4 2

# max(iterable) 괄호( ) 안에 리스트, 문자 열등 반복 가능한 자료형을 넣으면 가장 큰 값을 반환해준다.

# min(iterable) 괄호( ) 안에 리스트, 문자 열등 반복 가능한 자료형을 넣으면 가장 작은 값을 반환해준다.

# iterable(반복할 수 있는)이란 list, dict, set, str, bytes, tuple, range와 같이 반복이 가능한 데이터 타입
# 즉, member를 하나씩 반환(접근)할 수 있는 데이터 타입을 말한다.