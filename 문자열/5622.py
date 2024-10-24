# 오래된 다이얼 전화기

# 1: 2초
# 2: (A, B, C) 3초
# 3: (D, E, F) 4초
# 4: (G, H, I) 5초
# 5: (J, K, L) 6초
# 6: (M, N, O) 7초
# 7: (P, Q, R, S) 8초
# 8: (T, U, V) 9초
# 9: (W, X, Y, Z) 10초
# 0: (Operator) 11초

# # my solution

# s = input()
# seconds = 0
# for l in s:
#   if l in ("A", "B", "C"):
#     seconds += 3
#   elif l in ("D", "E", "F"):
#     seconds += 4
#   elif l in ("G", "H", "I"):
#     seconds += 5
#   elif l in ("J", "K", "L"):
#     seconds += 6
#   elif l in ("M", "N", "O"):
#     seconds += 7
#   elif l in ("P", "Q", "R", "S"):
#     seconds += 8
#   elif l in ("T", "U", "V"):
#     seconds += 9
#   elif l in ("W", "X", "Y", "Z"):
#     seconds += 10
#   elif l == "0":
#     seconds += 11

# print(seconds)

#################################

# another
dic = {
  1: '',
  2: 'ABC',
  3: 'DEF',
  4: 'GHI',
  5: 'JKL',
  6: 'MNO',
  7: 'PQRS',
  8: 'TUV',
  9: 'WXYZ'
}

str = input()
t = 0

for s in str:
  for key in dic:
    if (s in dic[key]) : t += (key + 1)

print(t)