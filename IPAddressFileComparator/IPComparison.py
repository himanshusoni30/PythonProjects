#pip install pandas

import pandas as pd

PATH_TO_DIRECTORY = '/path/to/directory/'

df1 = pd.read_csv(PATH_TO_DIRECTORY+'data1.csv', header=None) #data1.csv fileName
df2 = pd.read_csv(PATH_TO_DIRECTORY+'data2.csv', header=None) #data2.csv fileName

# Find common records
common_records = pd.merge(df1, df2, on=list(df1.columns), how='inner')

# Find newly added records
new_records = df2[~df2.isin(df1)].dropna()

# Find deleted records
deleted_records = df1[~df1.isin(df2)].dropna()

print('------------------------------------')
print('RECORDS_IN_FILE1: ', len(df1))
print('RECORDS_IN_FILE2: ', len(df2))

print('COMMON_RECORDS:\t', len(common_records))
df_common_records = pd.DataFrame(common_records)
df_common_records.to_csv(PATH_TO_DIRECTORY+'common_records.csv', index=False, header=False)

print('NEW_RECORDS:\t', len(new_records))
df_new_records = pd.DataFrame(new_records)
df_new_records.to_csv(PATH_TO_DIRECTORY+'new_records.csv', index=False, header=False)

print ('DELETED_RECORDS:\t', len(deleted_records))
df_deleted_records = pd.DataFrame(deleted_records)
df_deleted_records.to_csv(PATH_TO_DIRECTORY+'deleted_records.csv', index=False, header=False)
print('------------------------------------')
