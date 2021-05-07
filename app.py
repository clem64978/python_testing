import os
from services.common.math import *
from services.common.testClass import myClass
# print(makeList1())
# print(makeList3())

# print(remove_duplicates([1,1,1,1,3,3,3,3,5,5,5,5,5]))


dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])
possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}

# set built-in function union
print(dataScientist.union(dataEngineer))

# Intersection operation
print(dataScientist.intersection(dataEngineer))

# Initialize a set
graphicDesigner = {'Illustrator', 'InDesign', 'Photoshop'}

# These sets have elements in common so it would return False
dataScientist.isdisjoint(dataEngineer)

# These sets have no elements in common so it would return True
dataScientist.isdisjoint(graphicDesigner)

# Difference Operation
dataScientist.difference(dataEngineer)

# Symmetric Difference Operation
dataScientist.symmetric_difference(dataEngineer)

mySkills.issubset(possibleSkills)

#List comprehension
xr = [2*j + 10 for j in range(10)]
print(xr)

