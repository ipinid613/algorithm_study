c = int(input())
arr = []

for i in range(c):
    m = list(map(int,input().split()))
    total = 0
    cnt = 0
    for j in range(1,len(m)):
        total += m[j]
    average = total/(len(m)-1)
    for k in range(1,len(m)):
        if m[k] > average:
            cnt +=1
    arr.append(cnt/(len(m)-1)*100)

for answer in arr:
    print("%.3f%%"%answer)