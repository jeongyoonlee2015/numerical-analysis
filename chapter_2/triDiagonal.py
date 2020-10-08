# input: 삼중대각 정칙행렬 A, 열벡터b
# 출력: 해X

import numpy as np
import sys


def triDiagonal(A, b):
    n = len(b)
    # 상삼각행렬 만들기
    for j in range(0, n - 1):
        lam = A[j + 1, j] / A[j, j]
        A[j + 1, j] = 0.0 #자동적으로 0?
        A[j + 1, j + 1] = A[j + 1, j + 1] - lam * A[j, j + 1]
        b[j + 1] = b[j + 1] - lam * b[j]
    #확인하기
    print(A)
    print(b)
        # 해의 존재 유무 확인
    if (np.prod(np.diag(np.abs(A))) - 0.0) < sys.float_info.epsilon:  # 절대값씌우고 대각성분,곱해주기
        print('해가 존재하지 않거나 무수히 많음')
        exit()

    # 역대입법
    X = np.zeros((n, 1))
    X[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        X[i] = (b[i] - (A[i, i + 1] * X[i + 1])) / A[i, i]

    return X

# #이렇게 실행해도 됨
# A = np.array([[2.0, 6.0, 0.0], [-2.0, -7.0, -3.0], [0.0, 2.0, -4.0]])
# b = np.array([[-10], [3.0], [-16.0]])
# X = triDiagonal(A, b)
# print(X)
#
# import numpy as np
# from triDiagonal import *
# A = np.array([[2.0, 6.0, 0.0], [-2.0, -7.0, -3.0], [0.0, 2.0, -4.0]])
# b = np.array([[-10], [3.0], [-16.0]])
# X = triDiagonal(A, b)
# [[  2.   6.   0.]
#  [  0.  -1.  -3.]
#  [  0.   0. -10.]]
# [[-10.]
#  [ -7.]
#  [-30.]]
# print(X)
# [[ 1.]
#  [-2.]
#  [ 3.]]