# 입력: SPD 행렬 A, 초기벡터 X, 허용오차 tol, 최대 반복횟수 kmax
# 출력: 근사해 approx
# <Gauss Seidel> GS 방법은 야코비 방법에서 최근 x로만 바꾸어 주면 된다.
import numpy as np

def jacobi(A, b, x, kmax, tol):
    r = b - np.matmul(A, b)#잔여오차 r
    rnorm = np.linalg.norm(r)
    bnorm = np.linalg.norm(b)

    n = len(A)
    xnew = np.copy(x)

    k = 1
    print('k \t\t 근사해')
    while((rnorm > (tol * bnorm)) and (k <= kmax)):
        for i in range(0, n):
            Lsum = np.dot(A[i, 0:i], xnew[0:i])
            # Lsum = np.matmul(A[i, 0:i], x[0:i]) dot 대신 matmul을 쓸 수 있다.
            Usum = np.dot(A[i, i + 1:n], x[i + 1:n])
            xnew[i] = (b[i] - Lsum - Usum) / A[i, i]
        print('k = {0} \t x = {1}'.format(k, xnew))
        x = np.copy(xnew)
        #오차가 줄어드는 부분
        r = b - np.matmul(A, x)
        rnorm = np.linalg.norm(r)
        k = k + 1
    approx = x
    return approx

A = np.array([[8.0, 2.0, -4.0], [5.0, 10.0, -3.0], [-1.0, 5.0, 20.0]])
b = np.array([6.0, 12.0, 24.0])
x = np.array([0.0, 0.0, 0.0])
kmax = 10 #반복횟수 더 줘도 상관없음
tol = 0.0001 #허용오차
approx = jacobi(A, b, x, kmax, tol)
print(approx)