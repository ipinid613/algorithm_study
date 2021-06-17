# not_self = []
#
for i in range(1,10001):
    i_num = 0
    for j in list(str(i)):
        i_num = i_num + int(j)
        num = int(i) + i_num
    not_self.append(num)

for k in range(1,10001):
    if k not in not_self:
        print(k)

total_number = set(range(1,10001))
target_number = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    target_number.add(i)

self_number = sorted(total_number -target_number)

for k in self_number:
    print(k)