import numpy as np
# IN THIS SECTION I DEAL WITH RANDOM NUMBER GENERATION

# case 1: with no seed
print(np.random.rand())
print(np.random.rand())
print(np.random.rand()) # notice how we get different numbers for all the three calls
print("end of case 1")
# case 2: starting from a seed
print("case 2")
np.random.seed(100) # seed can be any number
print(np.random.rand())
print(np.random.rand())
print(np.random.rand()) # now let's reuse the seed again

np.random.seed(100)
print(np.random.rand())
print(np.random.rand()) # notice we start getting the same numbers again in the same pattern

# case 3
print("case 3")
print(np.random.randint(0, 4)) # no seed
print(np.random.randint(0, 4)) # no seed
print(np.random.randint(0, 4)) # now, let's use seed below

np.random.seed(13)
print(np.random.randint(0, 4))
print(np.random.randint(0, 4))
print(np.random.randint(0, 4))

np.random.seed(13)
print(np.random.randint(0, 4))
print(np.random.randint(0, 4))
print(np.random.randint(0, 4))



