import pandas as pd

ticker=["AAPL","AMZN","MSFT"]
#ticker=['AAPL']
column_names = ['date_time','start','end', 'p1','p2','Exchange Number','ticker_symbol']
cn2 = ['date_time','start','end', 'p1','p2','Exchange Number']
df = pd.DataFrame(columns= column_names)
for i in ticker:
    #read in the csv
    file_path = "./sp500_bundle_sample/"+i+"_1min_sample.txt"
    df2 = pd.read_csv(file_path, names= cn2);
    #add i as the ticker symbol
    df2['ticker_symbol']=i
    #merge to the existing dataframe
    frames=[df,df2]
    df = pd.concat(frames)

#now that I have merged all the dataframes together, pull out the ones for Microsoft
msft = df.loc[df['ticker_symbol'] == 'MSFT']
#get the sum of Pi values where exchange = 200
sum_200 = df.loc[df['Exchange Number'] == 200, 'p1'].sum()
print(sum_200)

