import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
 
df = pd.read_csv('codereddata.csv')

print(df.head())


c = df.loc[(df['Characteristic Label'] == 'Total') & (df['Format'] == 'Number') & (df['Year'] == 2015) & (df['Measure'] == 'Child fatalities') & (df['State'] != 'National')]
print(c)

plt.figure(0)
# Create first chart here.
df1 = c.iloc[0:10]
print(df1)

labels1 = df1['State'].values
print(labels1)

sizes1 = df1['Value'].values

colors1 = ['#FFC0CB', '#B0E0E6', '#DDA0DD','#DB7093', '#FF7F50','#DC143C','#FF8C00','#FFD700', '#90EE90', '#FF4500']

plt.pie(sizes1, labels=labels1, colors=colors1, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()

plt.figure(1)
# Create second chart here.


df2 = c.iloc[10:20]
print(df2)


labels2 = df2['State'].values
print(labels2)


sizes2 = df2['Value'].values

colors2 = ['#FFC0CB', '#B0E0E6', '#DDA0DD','#DB7093', '#FF7F50','#DC143C','#FF8C00','#FFD700', '#90EE90', '#FF4500']


plt.pie(sizes2, labels=labels2, colors=colors2, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()

plt.figure(2)
# Create third chart here.


df3 = c.iloc[20:30]
print(df3)


labels3 = df3['State'].values
print(labels3)


sizes3 = df3['Value'].values

colors3 = ['#FFC0CB', '#B0E0E6', '#DDA0DD','#DB7093', '#FF7F50','#DC143C','#FF8C00','#FFD700', '#90EE90', '#FF4500']


plt.pie(sizes3, labels=labels3, colors=colors3, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()

plt.figure(3)
# Create fourth chart here.

df4 = c.iloc[30:40]
print(df4)


labels4 = df4['State'].values
print(labels4)


sizes4 = df4['Value'].values

colors4 = ['#FFC0CB', '#B0E0E6', '#DDA0DD','#DB7093', '#FF7F50','#DC143C','#FF8C00','#FFD700', '#90EE90', '#FF4500']


plt.pie(sizes4, labels=labels4, colors=colors4, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()

plt.figure(4)
# Create fifth chart here.

df5 = c.iloc[40:]
print(df5)


labels5 = df5['State'].values
print(labels5)


sizes5 = df5['Value'].values

colors5 = ['#FFC0CB', '#B0E0E6', '#DDA0DD','#DB7093', '#FF7F50','#DC143C','#FF8C00','#FFD700', '#90EE90', '#FF4500']


plt.pie(sizes5, labels=labels5, colors=colors5, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()
plt.show()

