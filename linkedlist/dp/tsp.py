import sys
n = 4
distan = [[0, 22, 26, 30],
          [30, 0, 45, 35],
          [25, 45, 0, 60],
          [30, 35, 40, 0]]
completed_visit = (1 << n) - 1
DP = [[-1 for _ in range(n)] for _ in range(2 ** n)]
def TSP(mark, position):
    if mark == completed_visit:
        return distan[position][0]
    if DP[mark][position] != -1:
        return DP[mark][position]
    answer = sys.maxsize
    for city in range(n):
        if (mark & (1 << city)) == 0:
            new_answer = distan[position][city] + TSP(mark | (1 << city), city)
            answer = min(answer, new_answer)
    DP[mark][position] = answer
    return answer
for i in range(1 << n):
    for j in range(n):
        DP[i][j] = -1
print("Minimum Distance Travelled ->", TSP(1, 0))