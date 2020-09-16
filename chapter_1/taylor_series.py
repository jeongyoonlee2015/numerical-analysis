# 테알러 전개에 따른 근삿값 구하기
# input: c = 0 에서 exp(x)의 n차 taylor unfolding
# output: s는 x0 = 1인, f(1)에서의 근삿값

from math import factorial
s = 0

for k in range(0, 10):
    s = s + (1) ** k / factorial(k)
    if(k % 2) == 0:
        print(s)

# 1.0
# 2.5
# 2.708333333333333
# 2.7180555555555554
# 2.71827876984127