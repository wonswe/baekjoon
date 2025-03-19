# 입력
# 첫 번째 줄에는 문제의 정수 N이 주어진다. 
# (4 <= N <= 1000; N은 4의 배수)

# 출력
# 혜아가 
# N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

# 예제 입력 1 
# 4
# 예제 출력 1 
# long int
# 예제 입력 2 
# 20
# 예제 출력 2 
# long long long long long int

# my solution

n = int(input())
long = "long "
str = ""

for i in range(n//4):
  str += long
  
print(f"{str}int")

# another
n = int(input())
print("long " * (n // 4) + "int")