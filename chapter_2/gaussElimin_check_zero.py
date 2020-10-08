# input: 정칙행렬 A, 열벡터b
# 출력: 해X

import numpy as np
import sys


def gaussElimin(A, b):
    n = len(b)
    # 상삼각행렬 만들기
    for j in range(0, n - 1):
        #피벗이 0인지 체크
        if np.abs(A[j, j] - 0.0) < sys.float_info.epsilon:
            for k in range(j + 1, n):
                if np.abs(A[k, j] - 0.0) > sys.float_info.epsilon:
                    temp = np.copy(A[k, :]); tempb = np.copy(b[k])
                    A[k, :] = A[j, :]; b[k] = b[j]
                    A[j, :] = temp; b[j] = tempb
                    break
        for i in range(j + 1, n):
            lam = A[i, j]/A[j, j]

        # 해의 존재 유무 확인
    if (np.prod(np.diag(np.abs(A))) - 0.0) < sys.float_info.epsilon:  # 절대값씌우고 대각성분,곱해주기
        print('해가 존재하지 않거나 무수히 많음')
        exit()
        # 역대입법
    X = np.zeros((n, 1))
    X[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        X[i] = (b[i] - np.dot(A[i, i + 1:n], X[i + 1:n])) / A[i, i]

    return X
# import numpy as np
# A = np.array([[0.0, 1.0, -4.0], [1.0, -3.0, 2.0], [5.0, -8.0, 7.0]])
#   ...: b = np.array([[-11.0], [5.0], [23.0]])
# from gaussElimin import *