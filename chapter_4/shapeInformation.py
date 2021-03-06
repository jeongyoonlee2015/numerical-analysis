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

# # numpy.ravel
# # 배열의 요소를 1차원 상에 연속적으로 나열
# # numpy.reshape
# # 배열의 요소를 바꾸지 않고, 배열의 형태만 변경
# # numpy.resize
# # 배열의 요소 수가 같지 않다면, 배열의 성분이 변경될 수 있다. 새로운 배열의 요소수가 크다면 반복 될 수 있다.
# x
# Out[9]:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
# np.ravel(x)
# Out[10]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
# # 매트랩은 열벡터우선으로, 파이썬은 행벡터우선로
# np.reshape(x, (4, 3))
# Out[12]:
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
# np.resize(x, (3, 5))
# Out[13]: #부족한부분을 반복함
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11,  0,  1,  2]])
