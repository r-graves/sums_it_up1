#attempting to sum things up in pandas
import pandas as pd

file_path = "./sp500_bundle_sample/AAPL_1min_sample.txt"

df1 = pd.read_csv(file_path);

print(df1)