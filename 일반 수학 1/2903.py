# 문제
# Mirko and Slavko are filming a movie adaptation of the popular SF novel "Chicks in space 13". The script requires them to present a lot of different worlds so they decided to film the entire movie in front of a green screen and add CGI backgrounds later. Mirko heard that the best way to generate artificial terrain is to use midpoint displacement algorithm.

# To start the algorithm, Mirko selects 4 points forming a perfect square. He then performs the following steps:

# On each side of the square, he adds a new point in the exact middle of the side. The height of this new point is the average height of the two points on that side.
# In the exact center of the square he adds a new point whose height is the average height of all 4 square vertices, plus a small random value.
# After those two steps are performed, he now has 4 new squares. He performs the same steps on the newly created squares again and again until he is pleased with the results. The following diagram illustrates 2 iterations of the algorithm.

		
# Start - 4 points	1 iteration - 9 points	2 iterations - 25 points
# Mirko noticed that some of the points belong to more than one square. In order to decrease memory consumption, he stores calculates and stores such points only once. He now wonders how many points in total will he need to store in memory after N iterations.

# 입력
# The first and only line of input contains one integer N (1 ≤ N ≤ 15), number of iterations

# 출력
# The first and only line of output should contain one number, the number of points stored after N iterations.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 9
# 예제 입력 2 
# 2
# 예제 출력 2 
# 25
# 예제 입력 3 
# 5
# 예제 출력 3 
# 1089

# 초기 상태 (0) - 한 변에 2개의 점, 점의 개수: 2 x 2 = 4
# 1번째 (N = 1) - 한 변에 점: 2 x 2 - 1 = 3, 점의 개수: 3 x 3 = 9
# 2번째 (N = 2) - 한 변에 점: 3 x 2 - 1 = 5, 점의 개수: 5 x 5 = 25
# 3번째 (N = 3) - 한 변에 점: 5 x 2 - 1 = 9, 점의 개수: 9 x 9 = 81
# 4번쩨 (N = 4) - 한 변에 점: 9 x 2 - 1 = 17, 점의 개수: 17 x 17 = 289
# 한 변의 점 개수 = 이전 한 변의 개수 x 2 - 1
# 점의 개수 = (한 변의 점 개수)^2

N = int(input())
S = 2

for _ in range(N):
    S = (S * 2) - 1

print(S ** 2)