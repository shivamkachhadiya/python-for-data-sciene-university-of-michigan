import pandas as pd
stu=['alas','jack','molly']
print(pd.Series(stu))
num=[1,2,3]
print(pd.Series(num))
stu=[1,2,None]
print(pd.Series(stu))

import numpy as np
print(np.nan==None)

student={'shivam':'computer',
         'pratik':'maths',
         'suresh':'science'
         }
print(pd.Series(student))

std=[{"shivam","kachhadiya"},{"prakash","gujarati"},{"manish","gupta"}]
print(pd.Series(std))
s=pd.Series(['physics','chemestry','maths'],index=['shivam','raj','mahesh'])
print(s)

std={'shivam':'maths',
     'mahesh':'english',
     'prkash':'computer'}
s=pd.Series(std,index=['shivam','mahesh','prkash'])
print(s)


#QUERYING STRING
std={'shivam':'maths',
     'mahesh':'english',
     'prkash':'computer'}
s=pd.Series(std)
# print(s)
print(s.iloc[2])
print(s.loc['shivam'])
print(s[1])

class_code={99:'physics',
            100:'chemestry',
            66:'english',
            78:'maths'}
s=pd.Series(class_code)
print(s)

grades=pd.Series([90,88,89,90])
total=0
for grade in grades:
    total+=grade
print(total/len(grades))

total=np.sum(grades)
print(total/len(grades))

num=pd.Series(np.random.randint(0,1000,10000))
print(num.head())
print(len(num))
num+=2
print(num.head())

# for label,value in num.iteritems():
#     num.set_value(label,value+2)
# print(num.head())

s=pd.Series([1,2,3])
s.loc['hostory']=102
print(s)

std=pd.Series({'shivam':'maths',
               'rajesh':'english',
               'msnisha':'physics',
               'paresh':'gujrati'})
print(std)

std=pd.Series(['physics','maths','english'],index=['shivam','shivam','shivam'])
print(std)

#data frame
record1=pd.Series({'name':'shivam',
                   'class':'science',
                   'score':88})
record2=pd.Series({'name':'mahesh',
                   'class':'maths',
                   'score':56})
record3=pd.Series({'name':'shruti',
                   'class':'computer',
                   'score':99})
df=pd.DataFrame([record1,record2,record3],
                index=['school1','school2','school3'])
print(df.head())
print("-----------------------------------")
print(df.loc['school2'])
print(type(df.loc['school2']))
print("-----------------------------------")
print(df.loc['school1','name'])
print("-----------------------------------")
print(df.T)
print("-----------------------------------")
print(df.T.loc['name'])
print(df['name'])
print(df['score'])
print("-----------------------------------")
print(df.loc[:,['name','score']])
print("-----------------------------------")
print(df.drop('school1'))
print("-----------------------------------")
copy_df=df.copy()
copy_df.drop("name",inplace=True,axis=1)
print(copy_df)

print("----------------------------------------------------------------------")
df=pd.read_csv("C:\\Users\\i\\Desktop\\student.csv",index_col=0, encoding="ISO-8859-1")
print(df.head())

print("-----------------------------------")


####################################################   output   #####################################################

school3  shruti     99
PS C:\Users\i\desktop> python week2.py
0     alas
1     jack
2    molly
dtype: object
0    1
1    2
2    3
dtype: int64
0    1.0
1    2.0
2    NaN
dtype: float64
False
shivam    computer
pratik       maths
suresh     science
dtype: object
0    {kachhadiya, shivam}
1     {gujarati, prakash}
2         {gupta, manish}
dtype: object
shivam      physics
raj       chemestry
mahesh        maths
dtype: object
shivam       maths
mahesh     english
prkash    computer
dtype: object
computer
maths
english
99       physics
100    chemestry
66       english
78         maths
dtype: object
89.25
89.25
0    376
1    950
2    177
3    274
4     96
dtype: int32
10000
0    378
1    952
2    179
3    276
4     98
dtype: int32
0            1
1            2
2            3
hostory    102
dtype: int64
shivam       maths
rajesh     english
msnisha    physics
paresh     gujrati
dtype: object
shivam    physics
shivam      maths
shivam    english
dtype: object
           name     class  score
school1  shivam   science     88
school2  mahesh     maths     56
school3  shruti  computer     99
-----------------------------------
name     mahesh
class     maths
score        56
Name: school2, dtype: object
<class 'pandas.core.series.Series'>
-----------------------------------
shivam
-----------------------------------
       school1 school2   school3
name    shivam  mahesh    shruti
class  science   maths  computer
score       88      56        99
-----------------------------------
school1    shivam
school2    mahesh
school3    shruti
Name: name, dtype: object
school1    shivam
school2    mahesh
school3    shruti
Name: name, dtype: object
school1    88
school2    56
school3    99
Name: score, dtype: int64
-----------------------------------
           name  score
school1  shivam     88
school2  mahesh     56
school3  shruti     99
-----------------------------------
           name     class  score
school2  mahesh     maths     56
school3  shruti  computer     99
-----------------------------------
            class  score
school1   science     88
school2     maths     56
school3  computer     99
----------------------------------------------------------------------       
    Eldon Base for stackable storage shelf, platinum  ...   0.8
1                                                     ...
2  1.7 Cubic Foot Compact "Cube" Office Refrigera...  ...  0.58
3   Cardinal Slant-D® Ring Binder, Heavy Gauge Vinyl  ...  0.39
4                                               R380  ...  0.58
5                           Holmes HEPA Air Purifier  ...  0.50
6  G.E. Longer-Life Indoor Recessed Floodlight Bulbs  ...  0.37

[5 rows x 9 columns]
-----------------------------------
PS C:\Users\i\desktop> 
