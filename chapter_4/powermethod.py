# 입력: 행렬 A, 초기벡터 x, 최대 반복횟수 kmax
# 출력: 우세 고유값, 우세 고유벡터

import numpy as np
def power(A, x, kmax):
    #A가 정방행렬이어야 하므로 정방행렬인지 확인
    m, n = A.shape
    if m != n:
        print('정방행렬이 아님')

    for k in range(0, kmax):
        y = np.matmul(A, x)
        #파워법 구성방법은 두 가지가 있다.
        # 1차 방법: y값에 절대값을 취하고 그 중 가장 큰 값
        index = np.argmax(np.abs(y)) # 절대값이 최대값인 인덱스
        value = y[index] # value: 우세고유값
        vector = y / value #y값을 value로 나눈다. #vector: 우세 고유 벡터
        print('k = {0} \t 고유값 = {1} \t 고유벡터 = {2}'.format(k, value, vector))#k, value, vector값이 변하는 것이 들어가게 됨.
        x  = np.copy(vector)
    return value, vector

#power 함수 정의 완료

