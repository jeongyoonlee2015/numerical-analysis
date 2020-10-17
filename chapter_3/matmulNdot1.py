import numpy as np
A = np.arange(6).reshape([2, 3])
B = np.arange(12).reshape([3, 4])
C = np.arange(2 * 2 * 4).reshape((2, 2, 4))
D = np.arange(2 * 2 * 4).reshape((2, 4, 2))

i = np.dot(A, 2)
j = np.dot(B, 10)
# k = np.matmul(A, 3)
# l = np.matmul(B, 5)
x = np.matmul(C, D).shape
y = np.dot(C, D).shape

print("<<<dot>>>")
print(i,"\n\n", j)
# print("\n<<<matmul>>>")
# print(k,"\n", l)

print("<<<tensor multiplication - dot>>>")
print(x)
print("<<<tensor multiplication - matmul>>>")
print(y)