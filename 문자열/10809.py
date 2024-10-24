# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# # my solution

alphabet = {}
for i in range(97, 123):
  alphabet[chr(i)] = -1

s = input()
for i in range(len(s)):
  alphabet[s[i]] = s.find(s[i])

print(*alphabet.values())
# print(*alphabet.items())  # 그냥 해봄

#############################

# # another
import sys
s = sys.stdin.readline()
ans = []
for c in range(ord("a"), ord("z") + 1):
# 딱 봤을 때 range(97, 123)으로 되어있는 것 보다 
# a - z의 아스키를 사용한다는 걸 한눈에 볼 수 있는 이 코드가 더 좋은 것 같다. 
  ans.append(s.find(chr(c))) # find() method returns -1 if the value is not found
# 그리고 출력값에는 알파벳이 아닌 해당 문자의 위치만 필요하기 때문에 딕셔너리를 만들 
# 필요는 굳이 없는 것 같다. 문제가 어떤 출력값을 필요로 하는지 먼저 잘 파악하고 접근하자.
print(*ans)