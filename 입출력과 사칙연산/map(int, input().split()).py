n = input("숫자 입력: ")
print(n) # 4

nn = input("숫자 두 개를 띄어서 입력: ")
print(nn) # 4 4 

a = "This is juwon's homepage."
print(a.split()) 
# ['This', 'is', "juwon's", 'homepage.']

nn = input("숫자 여러개를 띄어서 입력: ")
print(nn.split())
# ['5', '4', '2', '1', '3', '2']
# 각각의 값을 리스트로 나누어 줌

# 입력값을 두 개 이상으로 구분하여 결과를 보자
a, b = map(int, input().split())
print(a + b) # 9
