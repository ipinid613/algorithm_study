import sys
import math
day_move,night_move,tree_height = map(int, sys.stdin.readline().split()) # 5 1 6

count = (tree_height - day_move)/(day_move - night_move) + 1
print(math.ceil(count))

# a = sys.stdin.readline()

# A    B    C         계산
# 5    1    6   (6-5)/(5-1)+1 = 1.25 => 2일
# 2    1    5   (5-2)/(2-1)+1 = 4.0 => 4일
# 3    1    8   (8-3)/(3-1)+1 = 3.5 => 4일
# 8    3    15  (15-8)/(8-3)+1 = 2.4 => 3일