import random
import matplotlib.pyplot as plt
import numpy as np

#simulation of 100 times dice throwing.
data=[]

for i in range(0,10000):
	data.append(random.choice(range(1,7)))

print(data)

plt.figure(1)
plt.hist(data,bins=np.linspace(0.5,6.5,7))

#now throw 10 dices and create variable Y holding their sum each time.
data2 = []
	
for i in range(0,10000):
	count=0
	for k in range(0,10):	
		count += random.choice(range(1,7))
	data2.append(count)	

plt.figure(2)
plt.hist(data2,bins=np.linspace(9.5,60.5,51))
plt.show()
