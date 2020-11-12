## numpy.linalg.eig - 고유값(Eigenvalue)과 고유벡터(Eigenvector)
## w, V = numpy.linalg.eig (A)는 정방행렬 A의 고유값 벡터(w)와 고유벡터 행렬(V)을 반환
## 고유값과 고유벡터의 관계
## 고유값 w[0]↔고유벡터 V[:, 0], 고유값 w[1]↔고유벡터 V[:, 1], …
## 각 고유벡터는 단위벡터이다.
# import numpy as np
# A = np.array([[3, 2], [4, 1]])
# A
# Out[4]:
# array([[3, 2],
#        [4, 1]])
# w, V = np.linalg.eig(A)
# w
# Out[6]: array([ 5., -1.])
# V
# Out[7]:
# array([[ 0.70710678, -0.4472136 ],
#        [ 0.70710678,  0.89442719]])
# np.linalg.norm(V[:,0])
# Out[8]: 0.9999999999999999
# np.linalg.norm(V[:,1])
# Out[9]: 0.9999999999999999