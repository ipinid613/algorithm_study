import sys

input = sys.stdin.readline
N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

#1 산술 평균 (소수점 첫 번째 자리에서 반올림)
print(round(sum(arr)/N))

#2 중앙값
arr.sort()
print(arr[N//2])

#3 최빈값
from collections import Counter
k=Counter(arr).most_common()
##counter의 most_common을 쓰면 arr의 숫자들과, 숫자들의 빈도수를 튜플형태로 저장해줌.


if len(arr) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0])
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else:
        print(k[0][0])
else:
    print(arr[0])

#4 범위
print(arr[-1] -  arr[0])



#  사사오입 방식의 반올림 구현하는 방법


# 파이썬에서 round 함수로 0.5를 반올림할 때, 정수 부분이 짝수면 반내림이 되고, 홀수면 반올림이 된다.
# 그 이유는 파이썬에서 사용하고 있는 round 내장 함수는 round_half_up 방식이 아니라 round_half_even 방식을 채택하고 있기 때문.



#  ex)즉 3.5의 경우에는 반올림이 되서 4가 되고, 4.5의 경우에는 반내림이 되어서 4가 되는 것.

# 이를 해결하기 위해, 반올림 오차가 없는 고정소수점을 사용하려면 decimal 모듈의 Decimal을 사용하면 된다. Decimal은 숫자를 10진수로 처리하여
#  정확한 소수점 자릿수를 표현해준다.



#  collections 모듈의 Counter 클래스

# **clear()** : 카운터 객체에서 모든 key-value 쌍을 제거

# **copy()** : 카운터 객체의 복사본을 반환

# **elements()** : 카운터 숫자만큼 요소 반환
# * 리스트를 가지고 카운터 객체를 만들었다면, 다시 리스트로 돌린다고 생각하면 쉽다. 순서는 바뀐다.

# **get()** : 인자로 key를 입력하면 해당 key와 매칭되는 value를 반환

# **items()** : key, value 쌍을 튜플 형태로 반환

# **keys()** : 카운터 객체의 key들을 반환

# **most_common()** : 가장 빈도수가 높은 key, value 쌍부터 튜플 형태로 반환. 인자로 숫자(개수)를 전달하면 가장 빈도수가 높은 것부터 해당 개수만큼의 쌍만이 반환됨

# **pop(), popitem()**
# * **pop()** : 인자로 key를 반드시 전달해야 하며, key와 매칭되는 value를 반환하고 해당 key, value 쌍을 카운터 객체에서 제거
# * **popitem()** : 전달하는 인자가 없어야 하며, 가장 뒤의 key, value 쌍을 튜플 형태로 반환하고 해당 쌍을 카운터 객체에서 제거

# **setdefault(**) : 카운터 객체에 key, value 쌍을 추가할 때 사용할 수 있음
# * key만 전달하면 카운트 수는 디폴트로 None
# * key와 함께 default=10과 같이 전달하면 key에 해당하는 카운트에 입력한 숫자가 반영됨

# **subtract()** : iterable을 전달하면 각 요소의 값을 각각 빼주고 그 결과의 카운트는 마이너스 값을 가질 수도 있음

# **update()** : iterable을 전달하여 같은 값이 있으면 카운트가 추가되게 하고 없으면 새로운 key, value 쌍을 생성

# **values()** : 카운터 객체의 value, 즉 카운트들을 반환