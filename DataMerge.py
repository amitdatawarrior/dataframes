import pandas as pd
import numpy as np


file1 = pd.read_excel("C:/Users/Public/POC/file1.xlsx")
file2 = pd.read_excel("C:/Users/Public/POC/file2.xlsx")


df1=pd.DataFrame(file1.columns)
df2=pd.DataFrame(file2.columns)

x = df1.isin(df2)

intersected_df = pd.merge(df1, df2, how='inner')

y = intersected_df.values.tolist()


dfa=pd.DataFrame(file1)
dfb=pd.DataFrame(file2)

print("-----") 
df = pd.concat([df1, df2], axis=1)
df['result'] = np.where(df[df1] == df[df2], 'no change', 'changed')
print (df)

new=dfb.merge(dfa,on='Inner') 

dfx = dfx.file1.isin(file2)
 
file1 = pd.read_excel("C:/Users/Public/POC/file1.xlsx")
file2 = pd.read_excel("C:/Users/Public/POC/file2.xlsx")

file3 = file1.merge(file2, on=y[0], how="inner")

file4 = file3.iloc[:, 1]


file4.to_excel("merged.xlsx")



