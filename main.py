# 구현 실전문제 왕실의 나이트

# 열(a,b,c...)과 행(1,2,3...)으로 구성된 나이트 현재 위치 받자

# 너무 노가다같은디..
first = str(input())
x = first[0]
if x == 'a':
  x = 1
if x == 'b':
  x = 2
if x == 'c':
  x = 3
if x == 'd':
  x = 4
if x == 'e':
  x = 5
if x == 'f':
  x = 6
if x == 'g':
  x = 7
if x == 'h':
  x = 8

y = first[1]
y = int(first[1])

#현재 위치
x, y
count = 0

# 이동해보자
if (x + 2) < 9 and (y + 1) < 9:
  count += 1
if (x + 2) < 9 and (y - 1) > 0:
  count += 1
if (x - 2) > 0 and (y + 1) < 9:
  count += 1
if (x - 2) > 0 and (y - 1) > 0:
  count += 1
if (y + 2) < 9 and (x + 1) < 9:
  count += 1
if (y + 2) < 9 and (x - 1) > 0:
  count += 1
if (y - 2) > 0 and (x + 1) < 9:
  count += 1
if (y - 2) > 0 and (x - 1) > 0:
  count += 1
print(count)
