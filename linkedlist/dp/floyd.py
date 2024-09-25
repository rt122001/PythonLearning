import numpy as np
def floyds(b):
    for k in range(3):
        for i in range(3):
            for j in range(3):
                if (b[i][k] * b[k][j] != 0) and (i != j):
                    if (b[i][k] + b[k][j] < b[i][j]) or (b[i][j] == 0):
                        b[i][j] = b[i][k] + b[k][j]
    for i in range(3):
        print("Minimum Cost With Respect to Node:", i)
        for j in range(3):
            print(b[i][j], end="\t")
b = np.zeros((3, 3), dtype=int)
b[0][1] = 10
b[1][2] = 15
b[2][0] = 12
#calling the method
floyds(b)