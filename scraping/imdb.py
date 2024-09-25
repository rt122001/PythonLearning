import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name','Age','Address','Qualification'}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(columns=('Name','Age','Address','Qualification'))

for i in range(5):
   df.loc[i] = [i,i,i,i]
# select two column
print(df)
df.to_csv('sample.csv',index=False)