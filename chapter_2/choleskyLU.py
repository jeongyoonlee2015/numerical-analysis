# input: 양의 정부호 대칭행렬A, 열벡터 b
# 출력: 해X

import numpy as np

def choleskyLU(A, b):
    n = len(b)
    L = np.zeros((n, n))


    # 하삼각행렬 만들기
    for i in range(0, n):
        for j in range(0, i):
            L[i, j] = (A[i, j] - np.dot(L[i, 0:j], L[j, 0:j])) / L[j, j]
        L[i, i] = np.sqrt(A[i, i] - np.dot(L[i, 0:i], L[i, 0:i]))

    print(L)

    # 대입법
    z = np.zeros((n, 1))
    z[0] = b[0] / L[0, 0]
    for i in range(1, n):
        z[i] = (b[i] - np.dot(L[i, 0:i], z[0:i])) / L[i, i]

    # 역대입법
    U = np.transpose(L)

    X = np.zeros((n, 1))
    X[n - 1] = z[n - 1] / U[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        X[i] = (z[i] - np.dot(U[i, i + 1:n], X[i + 1:n])) / U[i, i]

    return X
#
# import numpy as np
# from choleskyLU import *
# A = np.array([[16.0, -12.0, -12.0, -16.0], [-12.0, 25.0, 1.0, -4.0], [-12.0, 1.0, 17.0, 14.0], [-16.0, -4.0, 14.0, 57.0]])
#   ...: A
# Out[4]:
# array([[ 16., -12., -12., -16.],
#        [-12.,  25.,   1.,  -4.],
#        [-12.,   1.,  17.,  14.],
#        [-16.,  -4.,  14.,  57.]])
# b = np.array([[2.0], [3.0], [4.0], [5.0]])
#   ...: b
# Out[5]:
# array([[2.],
#        [3.],
#        [4.],
#        [5.]])
# X = choleskyLU(A, b)
# [[ 4.  0.  0.  0.]
#  [-3.  4.  0.  0.]
#  [-3. -2.  2.  0.]
#  [-4. -4. -3.  4.]]
# print(X)
# [[7.48388672]
#  [3.77929688]
#  [4.10546875]
#  [1.4453125 ]]