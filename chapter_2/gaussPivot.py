# input: 정칙행렬 A, 열벡터b
# 출력: 해X
#np.argmax, np.copy 이용하기
import numpy as np

def gaussPivot(A, b):
    n = len(b)
    X = np.zeros((n, 1))
    # 상삼각행렬 만들기
    for k in range(0, n - 1):
        #피벗이 0인지 체크 - 여기 고치기!!
        if np.fabs(A[k, k]) < 1.0e-12:
            for i in range(k + 1, n):
                if np.fabs(A[i, k]) > np.fabs(A[k, k]):
                    A[[k, i]] = A[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k + 1, n):
            if A[i, k] == 0:continue
            factor = A[k, k] / A[i, k]
            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j] * factor
            b[i] = b[k] - b[i] * factor

    print(A)
    print(b)
    X[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_Ax = 0
        for j in range(i + 1, n):
            sum_Ax += A[i, j] * X[j]
        X[i] = (b[i] - sum_Ax) / A[i, i]

    print('The solution of the system:')
    print(X)

# #이렇게 실행해도 됨
# A = np.array([[1.0, 2.0, 1.0], [2.0, 1.0, 0.0], [4.0, 2.0, 2.0]])
# b = np.array([[4.0], [3.0], [8.0]])
# X = gaussPivot(A, b)
# print(X)

#A = np.array([[0, 7, -1, 3, 1],[0,3,4,1,7],[6,2,0,2,-1],[2,1,2,0,2],[3,4,1,-2,1]])
#b = np.array([5],[7],[2],[3],[4])

#A = np.array([[1.0, -3.0, 3.0], [-3.0, 2.0, 3.0], [-1.0, 2.0, -1.0]])
# b = np.array([[-6.0], [-13.0], [3.0]])