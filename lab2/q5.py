import numpy as np
# create matric A,B
A = np.ones((3,2))
B = np.array([[1,2],[3,4],[5,6]])
print(A)
print(B)
# multiply A and B, save to C
A = A.T
C = np.matmul(A,B)
print(C)
# print the dimension of C
print(C.shape)
