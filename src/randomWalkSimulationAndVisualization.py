import numpy as np
import matplotlib.pyplot as plt

# we are going to visuaalize random walk with flipping a coin

np.random.seed(123)
final_tails = []
for x in range(1000) :
    tails = [0]
    for x in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
#plt.hist(final_tails, 10)
#plt.show()
data = [10, 15, 20, 60, 70]
plt.hist(data)
plt.show()