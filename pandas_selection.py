import pandas as pd

ticker=["AAPL","AMZN","MSFT"]
#ticker=['AAPL']
column_names = ['date_time','start','end', 'p1','p2','Exchange Number','timeframe','ticker_symbol']
timeframes = ['1min','5min','30min','1hour']
cn2 = ['date_time','start','end', 'p1','p2','Exchange Number']
df = pd.DataFrame(columns= column_names)
for i in ticker:
    for j in timeframes:
        #read in the csv
        file_path = "./sp500_bundle_sample/"+i+"_"+j+"_sample.txt"
        df2 = pd.read_csv(file_path, names= cn2);
        #add j as the timeframe
        df2['timeframe']=j
        #add i as the ticker symbol
        df2['ticker_symbol']=i
        #merge to the existing dataframe
        frames=[df,df2]
        df = pd.concat(frames)

#now that I have merged all the dataframes together, pull out the ones for Microsoft
msft = df.loc[df['ticker_symbol'] == 'MSFT']
#get the sum of Pi values where exchange = 200
sum_200 = msft.loc[msft['Exchange Number'] == 200, 'p1'].sum()
sum_200b = msft.loc[(msft['Exchange Number'] == 200) & (msft['timeframe'] == '1min'), 'p1'].sum()
sum_200c = msft.loc[(msft['Exchange Number'] == 200) & (msft['timeframe'] == '1hour'), 'p1'].sum()
print(sum_200)
print(sum_200b)
print(sum_200c)
print(df)

