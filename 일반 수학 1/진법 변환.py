# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# 예제 입력 1 
# ZZZZZ 36
# 예제 출력 1 
# 60466175

# 두 수 A와 B가 주어졌을 때 
# A를 B로 나눈 나머지값들을 B진법 규칙에 맞게 변환시킨 것이다.
# ex) 60,466,175와 36로 예를 들면, 60,466,175 % 36 = 35이다.
# 그리고 60,466,175 / 36 = 1,679,615(소수점제외)이고, 
# 다시 1,679,615을 36으로 나눈 나머지 값을 구하면 35가 나온다.
# 반복하면 마지막 숫자는 35가 나와 
# 총 나머지값은 35,35,35,35,35이고, 이를 B진법으로 변환하면 ZZZZZ이 되는 것이다.

# Z Z Z Z Z
# (Z x 36^4) + (Z x 36^3) + (Z x 36^2) + (Z x 36^1) + (Z x 36^0)
 
# A:10, B:11, C:12,..., F:15,...,Y:34, Z:35

N, B = input().split()
B = int(B)

# 방법 1: using int()
result = int(N,B)
print(result)

# 방법 2: convert each digit
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result1 = 0

for i in range(len(N)):
  value = digits.index(N[i])
  result1 = result1 * B + value
print(result)