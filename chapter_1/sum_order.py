sum1 = 1.0
sum2 = 0.0
rpt = 1 / (10 ** 16)
for i in range(1, 10 ** 7):
    sum1 = sum1 + rpt
    sum2 = sum2 + rpt

sum2 = sum2 + 1.0

print(sum1) #1.0
print(sum2) #1.0000000009999999

# 파이썬은 인터프리터 언어