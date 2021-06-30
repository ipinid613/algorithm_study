a,b = map(int, input().split())
if 0 <= a < 24 and 0 <= b <= 59:
    to_minutes = a*60
    wake_minus = 45
    minutes_result = (to_minutes+b)
    result = minutes_result - wake_minus
    a_result = result//60
    b_result = result%60
    if a_result < 0:
        a_result = 24+a_result
    print(a_result, b_result)

a,b = map(int,input().split())
origin_time = a*60 + b
if origin_time < 60:
    origin_time += 1440
wake_time = origin_time-45
result_H = wake_time//60
if result_H == 24:
    result_H = 0
result_M = wake_time%60
print(result_H,result_M)
