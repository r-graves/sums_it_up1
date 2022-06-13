#attempting to sum things up in pandas
import pandas as pd
import datetime as date

file_path = "./sp500_bundle_sample/AAPL_1min_sample.txt"

df1 = pd.read_csv(file_path, names=['date_time','start','end', 'p1','p2','Exchange Number'], index_col = 0);
df1.index = pd.to_datetime(df1.index,format='%Y-%m-%d %H:%M:%S')
df1['date_char'] = df1.index
def sel_date(df1b):
    #select timestamps in my timestamp range reset the index to avoid warning message from having duplicate indexes
    df2 = df1b.loc['2022-04-01 04:00:00':'2022-04-10 05:00:00'].reset_index()
    # convert datetime column to just date
    df2['date_char'] = pd.to_datetime(df2['date_char']).dt.date
    #dsa = df2.loc[]
    #sum up by date
    df3 = df2.groupby(by=['date_char'], sort=True).agg({'start':'sum','end':'sum'})
    #maximize by date
    df4 = df2.groupby(by=['date_char'], sort=True).agg({'start':'max','end':'max'})
    #pull the two together
    df5 = pd.concat([df3, df4], axis=1)
    return df5

returned_frame = sel_date(df1)

print('Returned Frame')
print(returned_frame)