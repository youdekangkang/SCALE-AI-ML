import numpy as np
import matplotlib.pyplot as plt
M = np.array([[-2,-4,2],[-2,1,2],[4,2,5]])
# find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M)
# plot the eigenvalues
fig=plt.figure()
ax = fig.gca(projection='3d')
va1 = eigenvectors[0]
va2 = eigenvectors[1]
va3 = eigenvectors[2]

ax.quiver(0,0,0,va1[0],va1[1],va1[2])
ax.quiver(0,0,0,va2[0],va2[1],va2[2])
ax.quiver(0,0,0,va3[0],va3[1],va3[2])

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(0,1)

plt.show()
# save the plot into a file named "eig.npy"
np.save('eig.npy',eigenvalues)
# load the saved file into new variable called "load_eig" and print the values
load_eig = np.load('eig.npy')
print(load_eig)