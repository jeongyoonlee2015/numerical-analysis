# 다음 두 식의 값을 비교하여 오차의 발생 여부를 알아보자.
sum1 = 1.0
sum2 = 0.0
rpt = 1 / (10 ** 6)
for i in range(1, 10 ** 7):
    sum1 = sum1 + rpt
    sum2 = sum2 + rpt

sum2 = sum2 + 1.0

print(sum1)
print(sum2)