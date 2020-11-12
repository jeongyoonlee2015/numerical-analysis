# # numpy.ndim
# # 배열의 차원, 축(axis)의 수
# # numpy.shape
# # 배열의 형태정보 출력, m×n차원
# # numpy.size
# # 배열의 요소(성분) 수
# import numpy as np
# x = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
# x
# Out[4]:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
# np.ndim(x)
# Out[5]: 2
# x.ndim
# Out[6]: 2
# np.shape(x)
# Out[7]: (3, 4)
# np.size(x)
# Out[8]: 12
