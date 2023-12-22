import csv
import pandas as pd

# import both the csv files
df1 = pd.read_csv('final_grades.csv')
df2 = pd.read_csv('breadthList.csv')

print(df1.head())
print(df2.head())
print(df1.columns)
print(df2.columns)

# add new column called name next to Course column
df1['Name'] = ''

# for each element in the column Course of df1, split the string by '-' and place the first element in the Course column and the second in a new column next to it called Name
for index, row in df1.iterrows():
    course = row['course']
    course = course.split('-')
    df1.loc[index, 'course'] = course[0]
    if len(course) > 1:
        df1.loc[index, 'Name'] = course[1]

print(df1.head())

# add 7 new columns to df2 which will store the percentage of each grade
df2['EX'] = ''
df2['A'] = ''
df2['B'] = ''
df2['C'] = ''
df2['D'] = ''
df2['P'] = ''
df2['F'] = ''

def calculatePercentage(row, index):
    sum = row['EX'] + row['A'] + row['B'] + row['C'] + row['D'] + row['P']+row['F']

    ex = (row['EX'].values[0]).astype(int)
    a = (row['A'].values[0]).astype(int)
    b = (row['B'].values[0]).astype(int)
    c = (row['C'].values[0]).astype(int)
    d = (row['D'].values[0]).astype(int)
    p = (row['P'].values[0]).astype(int)
    f = (row['F'].values[0]).astype(int)
    # print(ex, a, b, c, d, p, f)
    
    df2.loc[index, 'EX'] = ex
    df2.loc[index, 'A'] = a
    df2.loc[index, 'B'] = b
    df2.loc[index, 'C'] = c
    df2.loc[index, 'D'] = d
    df2.loc[index, 'P'] = p
    df2.loc[index, 'F'] = f
    

# for each row in the breadthList.csv file, get the Course ID and search for it in the final_grades.csv file
for index, row in df2.iterrows():
    courseID = row['Course']
    # if the courseID is found in the final_grades.csv file, then get the row
    if df1[df1['course'] == courseID].empty == False:
        # get the row
        row = df1[df1['course'] == courseID]
        print(row)
        # calculate the percentage of each grade
        calculatePercentage(row, index)
    else:
        print('Course ID not found', courseID)
        # if the courseID is not found, then put 0 in all the columns
        df2.loc[index, 'EX'] = 0
        df2.loc[index, 'A'] = 0
        df2.loc[index, 'B'] = 0
        df2.loc[index, 'C'] = 0
        df2.loc[index, 'D'] = 0
        df2.loc[index, 'P'] = 0
        df2.loc[index, 'F'] = 0
        

# put the new dataframe in a new csv file
df2.to_csv('breadthListWithGrades.csv', index=False)

        
    