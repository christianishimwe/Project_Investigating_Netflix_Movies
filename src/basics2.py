import math
import numpy as np

# SECTION 1: IN this section, I learn how to use numpy package
# -------------------------------------------------------------------
# -------------------------------------------------------------------
print(math.pi)
height = [20, 10, 5]
width = [4.5, 2, 1]
np_height = np.array(height)
np_width = np.array(width)
# finding the result of calculation

np_result = np_height / np_width
print(np_result)
# printing the type of the np_array
print(type(np_height))

# generating randomly simulated data
np_randomHeights = np.round(np.random.normal(1.70, 0.20, 3), 2)
print(np_randomHeights)


# SECTION 1: IN this section, I learn how to use MATPLOTLIB package






