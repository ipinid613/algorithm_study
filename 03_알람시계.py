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