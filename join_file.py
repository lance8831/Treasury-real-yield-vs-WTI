import glob
import os
import pandas as pd
from pathlib import Path

#setting path for joining multiple files
files = os.path.join("C:/Files/Treasury_real_yield_yearly", "treasury_real_yield*.csv")

#merged file returned
files = glob.glob(files)

#using pandas.concatenate the merge file into dataframe and fill out NULL values
new_csv = pd.concat(map(pd.read_csv, files), ignore_index=True)
new_csv = new_csv.fillna("N/A")

#Export the file into CSV format
filepath = Path("C:/Files/treasury_real_yield_all.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
new_csv.to_csv(filepath,index=None)

print("All files are merged")

data = pd.read_csv("treasury_real_yield_all.csv")
data["Date"] = pd.to_datetime(data["Date"])
check_data = data.info()
check_null = pd.isnull(data).sum()
print(check_data)
print(check_null)
