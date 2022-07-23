from bs4 import BeautifulSoup
import datetime
import lxml
import pandas as pd
from pathlib import Path
import requests

print(datetime.datetime.now().strftime('%Y-%m-%d'))
print("Daily Treasury Par Yield Curve Rates")
print("Treasury Yield data only valid from 1990 onwards")

year = int(input("Enter year:"))
if year < 1990:
    print("No data found")
    exit()

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value={0}".format(year)

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
#Duration for 1month
yields1 = []
yields = soup("d:BC_1MONTH")
for yield1 in yields:
    yield1 =(yield1.contents[0])
    yields1.append(yield1)

#Duration for 2month
yields2 = []
yields = soup("d:BC_2MONTH")
for yield2 in yields:
    yield2 = (yield2.contents[0])
    yields2.append(yield2)

#Duration for 3month
yields3 = []
yields = soup("d:BC_3MONTH")
for yield3 in yields:
    yield3 =(yield3.contents[0])
    yields3.append(yield3)

#Duration for 6month
yields4 = []
yields = soup("d:BC_6MONTH")
for yield4 in yields:
    yield4 =(yield4.contents[0])
    yields4.append(yield4)

#Duration for 1year
yields5 = []
yields = soup("d:BC_1YEAR")
for yield5 in yields:
    yield5 =(yield5.contents[0])
    yields5.append(yield5)

#Duration for 2year
yields6 = []
yields = soup("d:BC_2YEAR")
for yield6 in yields:
    yield6 =(yield6.contents[0])
    yields6.append(yield6)

#Duration for 3year
yields7 = []
yields = soup("d:BC_3YEAR")
for yield7 in yields:
    yield7 =(yield7.contents[0])
    yields7.append(yield7)

#Duration for 5year
yields8 = []
yields = soup("d:BC_5YEAR")
for yield8 in yields:
    yield8 =(yield8.contents[0])
    yields8.append(yield8)

#Duration for 7year
yields9 = []
yields = soup("d:BC_7YEAR")
for yield9 in yields:
    yield9 =(yield9.contents[0])
    yields9.append(yield9)

#Duration for 10year
yields10 = []
yields = soup("d:BC_10YEAR")
for yield10 in yields:
    yield10 =(yield10.contents[0])
    yields10.append(yield10)

#Duration for 20year
yields11 = []
yields = soup("d:BC_20YEAR")
for yield11 in yields:
    yield11 =(yield11.contents[0])
    yields11.append(yield11)

#Duration for 30year
yields12 = []
yields = soup("d:BC_30YEAR")
for yield12 in yields:
    yield12 =(yield12.contents[0])
    yields12.append(yield12)

ser1 = pd.Series(date_list1, name = "Date",dtype = "datetime64[ns]")
ser2 = pd.Series(yields1, name = "1Mo",dtype = "float64")
ser3 = pd.Series(yields2, name = "2Mo",dtype = "float64")
ser4 = pd.Series(yields3, name = "3Mo",dtype = "float64")
ser5 = pd.Series(yields4, name = "6Mo",dtype = "float64")
ser6 = pd.Series(yields5, name = "1Yr",dtype = "float64")
ser7 = pd.Series(yields6, name = "3Yr",dtype = "float64")
ser8 = pd.Series(yields7, name = "5Yr",dtype = "float64")
ser9 = pd.Series(yields8, name = "7Yr",dtype = "float64")
ser10 = pd.Series(yields9, name = "10Yr",dtype = "float64")
ser11 = pd.Series(yields10, name = "20Yr",dtype = "float64")
ser12 = pd.Series(yields11, name = "30Yr",dtype = "float64")
results = pd.concat([ser1,ser2,ser3,ser4,ser5,ser6,ser7,ser8,ser9,ser10,ser11,ser12],axis = 1)

modified_results = results.fillna("N/A")
filepath = Path('C:/Users/Zhen Hao/Downloads/PY4E/Practice/treasury_yield_{0}.csv'.format(year))
filepath.parent.mkdir(parents=True, exist_ok=True)
modified_results.to_csv(filepath)

print("Data downloaded as CSV file.")


#newdf = pd.DataFrame(
            #{"Date":date_list1,
            #"1Month":yields1,
            #"2Month":yields2,
            #"3Month":yields3,
            #"6Month":yields4,
            #"1Year":yields5,
            #"2Year":yields6,
            #"3Year":yields7,
            #"5Year":yields8,
            #"7Year":yields9,
            #"10Year":yields10,
            #"20Year":yields11,
            #"30Year":yields12,
            #}).set_index("Date")

#print(newdf)
