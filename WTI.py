from pandas_datareader import data as wb
from pathlib import Path
import datetime
import pandas as pd

print(datetime.datetime.now().strftime('%Y-%m-%d'))

#import data from yahoo
WTI = wb.DataReader("CL=F",data_source ="yahoo", start = "2003-1-1")["Adj Close"]
WTI = WTI.drop(["2002-12-31"])

#Convert imported data into csv
filepath = Path("C:/Users/Zhen Hao/Downloads/PY4E/Practice/WTI_price.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
WTI.to_csv(filepath)

#rename column from adj close to price
mod_WTI = pd.read_csv("C:/Users/Zhen Hao/Downloads/PY4E/Practice/WTI_price.csv")
mod_WTI = mod_WTI.rename(columns={"Date":"Date_WTI","Adj Close":"WTI_Closing_Price"})
mod_WTI.to_csv("C:/Users/Zhen Hao/Downloads/PY4E/Practice/WTI_price.csv",index=None)
check_info = mod_WTI.info()

print("Data downloaded as CSV files")
print(check_info)
