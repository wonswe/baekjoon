# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

n = int(input())
num = list(map(int, input()))
print(sum(num))

# sum(list)는 리스트 내 모든 수를 더한 값을 반환한다. 
# 리스트, 튜플 등 iterable한 객체의 요소들을 더할 때 사용된다. 