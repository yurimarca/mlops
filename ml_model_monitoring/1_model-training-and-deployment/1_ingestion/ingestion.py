import os
import pandas as pd

directories=['/data1/','/data2/','/data3/']
df_list = [] # pd.DataFrame(columns=['col1','col2','col3'])

for directory in directories:
    filenames = os.listdir(os.getcwd()+directory)

    for each_filename in filenames:
        df1 = pd.read_csv(os.getcwd()+directory+each_filename)
        # Deprecated since version 1.4.0: Use concat() instead.
        # df_list=df_list.append(df1)
        df_list.append(df1)

df_list=pd.concat(df_list)

result=df_list.drop_duplicates()
result.to_csv('result.csv', index=False)
