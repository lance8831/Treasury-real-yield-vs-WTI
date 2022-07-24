from bs4 import BeautifulSoup
import datetime
import lxml
import pandas as pd
from pathlib import Path
import requests

print(datetime.datetime.now().strftime('%Y-%m-%d'))
print("Daily Treasury Par Real Yield Curve Rates")
print("Treasury Real Yield data only valid from 2003 onwards")

year = int(input("Enter year:"))
if year < 2003:
    print("No data found")
    exit()

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/' + \
xml?data=daily_treasury_real_yield_curve&field_tdr_date_value={0}".format(year)

print("Retrieving data...")
html =  requests.get(url)
html_text = html.text
soup = BeautifulSoup(html_text, "xml")

#extract the date
dates = soup("d:NEW_DATE")
date_list = []
date_list1 = []
for date in dates:
    date = (date.contents[0])
    date_list.append(date)
for date in date_list:
    date_list1.append(date[0:10])

#extract the yield for each duration
#Duration for 5Yr
yields1 = []
yields = soup("d:TC_5YEAR")
for yield1 in yields:
    yield1 =(yield1.contents[0])
    yields1.append(yield1)

#Duration for 7Yr
yields2 = []
yields = soup("d:TC_7YEAR")
for yield2 in yields:
    yield2 =(yield2.contents[0])
    yields2.append(yield2)

#Duration for 10Yr
yields3 = []
yields = soup("d:TC_10YEAR")
for yield3 in yields:
    yield3 =(yield3.contents[0])
    yields3.append(yield3)

#Duration for 20Yr
yields4 = []
yields = soup("d:TC_20YEAR")
for yield4 in yields:
    yield4 =(yield4.contents[0])
    yields4.append(yield4)

#Duration for 30Yr
yields5 = []
yields = soup("d:TC_30YEAR")
for yield5 in yields:
    yield5 =(yield5.contents[0])
    yields5.append(yield5)

ser1 = pd.Series(date_list1, name = "Date",dtype = "datetime64[ns]")
ser2 = pd.Series(yields1, name = "5Yr",dtype = "float64")
ser3 = pd.Series(yields2, name = "7Yr",dtype = "float64")
ser4 = pd.Series(yields3, name = "10Yr",dtype = "float64")
ser5 = pd.Series(yields4, name = "20Yr",dtype = "float64")
ser6 = pd.Series(yields5, name = "30Yr",dtype = "float64")
results = pd.concat([ser1,ser2,ser3,ser4,ser5,ser6],axis = 1)

modified_results = results.fillna("N/A")
filepath = Path("C:/Files/treasury_real_yield_{0}.csv".format(year))
filepath.parent.mkdir(parents=True, exist_ok=True)
modified_results.to_csv(filepath,index=None)

print("Data downloaded as CSV file.")
