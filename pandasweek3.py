import pandas as pd
staff_df=pd.DataFrame([{'name':'shivam','role':'student'},
                       {'name':'prkash','role':'bussness'},
                       {'name':'chandrika','role':'house wife'}])
staff_df=staff_df.set_index('name')
student=pd.DataFrame([{'name':'haresh','school':'computer'},
                      {'name':'harsh','school':'low'},
                      {'name':'mahesh','school':'civil engg'}])
student=student.set_index('name')
print(staff_df.head())
print(student.head())
print(pd.merge(staff_df,student,how='outer',left_index=True,right_index=True))
t1=pd.merge(staff_df,student,how='inner',left_index=True,right_index=True)
print(t1)
print("-------------------------------------------------------------------")
t2=pd.merge(staff_df,student,how='right',left_index=True,right_index=True)
print(t2)
print("-------------------------------------------------------------------")
staff=pd.DataFrame([{'name':'shivam','role':'Director of HR','location':'rajkot'},
                    {'name':'haresh','role':'registrar','location':'surat'},
                    {'name':'viraj','role':'proffesor','location':'junagadh'}])

student=pd.DataFrame([{'name':'manish','school':'Low','location':'ananad'},
                    {'name':'rajesh','school':'bussiness','location':'patan'},
                    {'name':'dilip','school':'Film','location':'chennai'}])
a=pd.merge(staff,student,how='left',on='name')
print(a)
print("-------------------------------------------------------------------")


staff=pd.DataFrame([{'first name':'shivam','last name':'kachhadiya'},
                    {'first name':'manish','last name':'gupta'},
                    {'first name':'ramesh','last name':'shrma'}])

student=pd.DataFrame([{'first name':'jeet','last name':'mishra'},
                    {'first name':'anand','last name':'gajera'},
                    {'first name':'mahesh','last name':'joshi'}])

print(pd.merge(staff,student,how='inner',on=['first name','last name']))

#pandas idioms

import numpy as np
import timeit
df=pd.read_csv('C:\\Users\\i\\Desktop\\adanistock.csv')
print(df.head())
print(df.where(df['Close']==2284.199951).dropna())




# #spiltting
# for state in df['Open'].unique():
#     avg=np.average(df.where(df['Open']==state).dropna()['test'])
#     print('test'+state+'test 2'+str(avg))

print(pd.Timestamp(2023,10,5,0,0))

from scipy import stats
df=pd.read_csv('C:\\Users\\i\\Desktop\\adanistock.csv')
print(df.head())
print("there are {} rows and {} coloumns".format(df.shape[0],df.shape[1]))
late_finishers=df[~df.index.isin(Volume.index)]
print(late_finishers.head())


###############################################################   output   #################################################

school3  shruti     99
PS C:\Users\i\desktop> python week3.py
                 role
name
shivam        student
prkash       bussness
chandrika  house wife
            school
name
haresh    computer
harsh          low
mahesh  civil engg
                 role      school
name
chandrika  house wife         NaN
haresh            NaN    computer
harsh             NaN         low
mahesh            NaN  civil engg
prkash       bussness         NaN
shivam        student         NaN
Empty DataFrame
Columns: [role, school]
Index: []
-------------------------------------------------------------------
       role      school
name
haresh  NaN    computer
harsh   NaN         low
mahesh  NaN  civil engg
-------------------------------------------------------------------
     name            role location_x school location_y
0  shivam  Director of HR     rajkot    NaN        NaN
1  haresh       registrar      surat    NaN        NaN
2   viraj       proffesor   junagadh    NaN        NaN
-------------------------------------------------------------------
Empty DataFrame
Columns: [first name, last name]
Index: []
         Date         Open         High  ...        Close    Adj Close     Volume
0  25-04-2022  2259.949951  2295.000000  ...  2284.199951  2283.229248  1683622.0
1  26-04-2022  2297.000000  2413.899902  ...  2395.300049  2394.282227  3199358.0
2  27-04-2022  2404.949951  2420.949951  ...  2334.100098  2333.108398  2559876.0
3  28-04-2022  2359.850098  2389.899902  ...  2378.550049  2377.539307  1679893.0
4  29-04-2022  2389.000000  2394.149902  ...  2332.000000  2331.009033  1916180.0

[5 rows x 7 columns]
         Date         Open    High  ...        Close    Adj Close     Volume
0  25-04-2022  2259.949951  2295.0  ...  2284.199951  2283.229248  1683622.0 

[1 rows x 7 columns]
2023-10-05 00:00:00
         Date         Open         High  ...        Close    Adj Close     Volume
0  25-04-2022  2259.949951  2295.000000  ...  2284.199951  2283.229248  1683622.0
1  26-04-2022  2297.000000  2413.899902  ...  2395.300049  2394.282227  3199358.0
2  27-04-2022  2404.949951  2420.949951  ...  2334.100098  2333.108398  2559876.0
3  28-04-2022  2359.850098  2389.899902  ...  2378.550049  2377.539307  1679893.0
4  29-04-2022  2389.000000  2394.149902  ...  2332.000000  2331.009033  1916180.0

[5 rows x 7 columns]
there are 247 rows and 7 coloumns

PS C:\Users\i\desktop> 
