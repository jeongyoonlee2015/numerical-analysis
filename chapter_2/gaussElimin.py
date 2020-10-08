# input: 정칙행렬 A, 열벡터b
# 출력: 해X

import numpy as np
import sys


def gaussElimin(A, b):
    n = len(b)
    # 상삼각행렬 만들기
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            lam = A[i, j] / A[j, j]
            # A[i, j + 1:n] = A[i, j + 1:n] - lam * A[j, j + 1:n]# 얘로 인해 [[ 1.  2.  1.],[ 2. -3. -2.], [ 4. -6.  2.]]가 됨
            A[i, :] = A[i, :] - lam * A[j, :]
            b[i] = b[i] - lam * b[j]
    # 확인
    print(A)
    print(b)

    # 해의 존재 유무 확인
    if (np.prod(np.diag(np.abs(A))) - 0.0) < sys.float_info.epsilon:  # 절대값씌우고 대각성분,곱해주기
        print('해가 존재하지 않거나 무수히 많음')
        exit()
    # 역대입법
    x = np.zeros((n, 1))
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:n], x[i + 1:n])) / A[i, i]

    return x

A = np.array([[1.0, 2.0, 1.0], [2.0, 1.0, 0.0], [4.0, 2.0, 2.0]])
b = np.array([[4.0], [3.0], [8.0]])
x = gaussElimin(A, b)
print(x)

A = np.array([[1.0, 2.0, 3.0], [2.0, 1.0, 3.0], [4.0, 2.0, 6.0]])

