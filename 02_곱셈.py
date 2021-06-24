#세자리수 곱하기
# a, b = map(str, input().split())
# a = int(input())
# b = input()
# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))

#2회차
a = int(input())
b = input()
a_result = a*(int(b[2]))
b_result = a*(int(b[1]))
c_result = a*(int(b[0]))
d_result = a*int(b)
print(a_result)
print(b_result)
print(c_result)
print(d_result)

#2회차 - 나머지 이용
num1 = int(input())
num2 = int(input()) #385

print(num1 * (num2%10)) #5
print(num1 * ((num2%100)//10)) #8
print(num1 * (num2//100)) #3
print(num1 * num2)