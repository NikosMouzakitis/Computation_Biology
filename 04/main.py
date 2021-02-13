import numpy as np
import matplotlib.pyplot as plt
# uniform distribution
uni=np.random.random((5,5))
print("uniform distribution")
print(uni)

#standard normal distribution
norm=np.random.normal(0,1)#mean,std.dev
norm=np.random.normal(0,1,(3,3))#mean,std.dev
print("normal distribution")
print(norm)

#do the same
X=np.random.randint(1,7, (10000,10))
print("X is")
print(X)

print("Variable Y is now")
Y=np.sum(X,axis=1)
print(Y)
print(Y.shape)

plt.hist(Y)
plt.show()
