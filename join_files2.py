import glob
import os
import pandas as pd
from pathlib import Path

#setting path for joining multiple files
files = os.chdir("C:/Users/Zhen Hao/Downloads/PY4E/Practice")

#make a list for the same file extension to be combined
extension = "csv"
all_files = [i for i in glob.glob("*.{}".format(extension))]

#using pandas.concatenate the merge file into dataframe and fill out NULL values
new_csv = pd.concat([pd.read_csv(f) for f in all_files],axis =1)
new_csv = new_csv.fillna("N/A")

#Export the file into CSV format
filepath = Path("C:/Users/Zhen Hao/Downloads/PY4E/Practice/real_yield_vs_WTI.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
new_csv.to_csv(filepath,index=None)

print("All files are merged")

#use to check all the null value between 2 different datasets
data = pd.read_csv("real_yield_vs_WTI.csv")
data["Date"] = pd.to_datetime(data["Date"])
data["Date_WTI"] = pd.to_datetime(data["Date_WTI"])
check_data = data.info()
check_null = pd.isnull(data).sum()
print(check_data)
print(check_null)
