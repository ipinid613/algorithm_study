N = int(input())


def gcd_r(a, b):
    return gcd_r(b, a % b) if b else a


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b

#     return a

def lcm(a, b):
    return a * b // gcd_r(a, b)


for i in range(N):
    a, b = map(int, input().split())

    print(lcm(a, b))

#   // 파이썬 문법 중에서 False로 취급하는 것들

#   1. None

#   2. False

#   3. 0인 숫자들: 0, 0.0, 0j(j는 복소수에서 허수부분을 표현함)

#   4. 비어 있는 문자열, 리스트, 튜플, 세트: '', "", [], (), set()

#   5. 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때

#   6. 앞에서 나열한 것들을 제외한 모든 요소들은 True로 취급