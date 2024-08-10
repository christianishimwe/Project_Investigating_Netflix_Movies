import matplotlib.pyplot as plt

# SECTION 2: IN this section, I learn how to use MATPLOTLIB package
#_____________________________________________________________________
#_____________________________________________________________________

# let's analyze making a plot
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()
plt.clf()
# list for the size of the scatter points, for the sizes you can even change it into a numpy array and change its size
sizes = [50, 2, 1000, 10]

# making a scatter plot
plt.scatter(year, pop, sizes)
plt.show()
plt.clf()

# SECTION 3: IN this section, I deal with Data Customization
#_____________________________________________________________________
#_____________________________________________________________________
plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0, 2, 4, 6, 8, 9],
           ['O Billions', '2 Billions', '4 Billions', '6 Billions', '8 Billions', '10 Billions'])
plt.show()
