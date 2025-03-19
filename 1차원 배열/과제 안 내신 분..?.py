# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

# 정리
# 학생 30명 (1 ~ 30번까지 출석번호)
# 28명이 과제 제출
# 과제 제출을 안 한 2명의 출석번호를 구하기

# my solution

# import sys
# students = []

# for i in range(1, 31):
#   students.append(i) # 학생 전원의 출석번호 리스트 생성
# submit = [] # 제출한 학생 리스트

# for student in range(1, 29): #과제를 제출한 28명의 출석 번호를 받음
#   # 입력 받은 출석 번호를 submit 리스트에 추가
#   submit.append(int(sys.stdin.readline()))

# no_submit = set(students) - set(submit)
# no_submit = list(no_submit)

# print(min(no_submit))
# print(max(no_submit))

###############################################

# another
student_num = [i for i in range(1, 31)]

for i in range(28):
  n = int(input())
  student_num.remove(n)

print(*student_num)
