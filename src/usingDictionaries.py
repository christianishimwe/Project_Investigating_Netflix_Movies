import pandas as pd
# IN THIS SECTION I PLAY AROUND WITH DICTIONARIES
#___________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________
# Suppose you have two lists, population and countries
# dictionaries will work just like a hash map in java
pop = [30.55, 2.77, 39.21]
countries = ['afganistan', 'albania', 'algeria']
# we create a dictionary named 'world'
world = {'afganistan':30.55, 'albania':2.77, 'algeria':39.21}
# now, suppose you want to retrive the population of algeria
print(world['algeria'])

## IN THIS SECTION I PLAY AROUND WITH PANDAS
#___________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________

dict = {
    "country": ['brazil', 'russia', 'india'],
    'capital': ['brazilia', 'moscow', 'new delhi'],
    'area': [8.516, 17.10, 3.286]
}

# creating the pandas
brics = pd.DataFrame(dict)
print(brics)

# dealing with comparisons
huge = brics['area'] > 4.0
print(huge)
print(brics[huge]) # this prints all the table including all those elements whose area > 4.00

