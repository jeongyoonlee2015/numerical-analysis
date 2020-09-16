# 다음 알고리즘의 기계오차를 계산하라
# 기계오차 계산 방법 1
meps = 1
while (1 + meps > 1.0):
    meps = meps / 2.0

meps = 2.0 * meps

print(meps) # 기계오차: 2.220446049250313e-16


# 기계오차 계산 방법 2
import sys
print(sys.float_info.epsilon)


# 실수의 오차 처리
print(0.1 + 0.2 == 0.3) # False
print(0.1 + 0.2) # 0.30000000000000004

#어떻게하면 실수의 오차 print를 True로 만들 수 있을까
import math
#fabs: float의 절대값
print(math.fabs((0.1 + 0.2) - 0.3) <= sys.float_info.epsilon) #True
