import pandas as pd


Location = "datasets/smallgradesh.csv"
# df = pd.read_csv(Location, header=None)




# To add headers if not exist
df = pd.read_csv(Location, names=['Names','Grades'])

# Location = "datasets/gradedata.csv"
# df = pd.read_csv(Location)

df.head()

df.columns = ['Names','Grades']


Location = "datasets/TestData/census.csv"
df = pd.read_csv(Location)
df.head()

#create csv
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns=columns)
df.to_csv('studentgrades.csv',index=False,header=False)



Location = "datasets/gradedata.xlsx"
df = pd.read_excel(Location)
df.head()

df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head() 

# Output to excel
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names','Grades'])
df2 = pd.DataFrame(data = GradeList,columns=['Names2','Grades2'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
writer.save()

