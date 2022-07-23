#Plot: 10Yr TIPS Yield vs WTI Oil Price (2003-2022)
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv("real_yield_vs_WTI.csv")
#change the date from object to datetime
data["Date"] = pd.to_datetime(data["Date"])
data["Date_WTI"] = pd.to_datetime(data["Date_WTI"])

#plot the graph
plt.rcParams.update({'font.family':'Arial'})
x = data["Date_WTI"]
y1 = data["10Yr"]
y2 = data["WTI_Closing_Price"]

fig, ax1 = plt.subplots(figsize=(16,8),dpi = 100)
ax1.set_xlabel("Year", fontsize = 20, labelpad = 14)
ax1.set_ylabel("Percent (%)", fontsize = 20,labelpad = 20)
ax1.plot(x,y1, color = "red", label = "10Yr TIPS yield")
ax1.tick_params(axis = "x", which = "major", labelsize = 12)
ax1.tick_params(axis = "y" , which = "major", labelcolor = "red", labelsize = 12,width =1.2,length=6,colors="red")
ax1.tick_params(axis = "y" , which = "minor", labelcolor = "red",colors="red")
ax1.spines["left"].set_color("red")
ax1.spines["left"].set_linewidth(3.8)

ax2 = ax1.twinx() #instantiate a second axes that shares the same x-axis
ax2.set_ylabel("Price (USD)", fontsize = 20,rotation = 270, labelpad = 20)
ax2.plot(x, y2, color = "blue", label = "WTI Price")
ax2.tick_params(axis = "y" , which = "major", labelcolor = "blue", labelsize = 12,width =1.2,length=6,colors="blue")
ax2.tick_params(axis = "y" , which = "minor", labelcolor = "blue",colors="blue")
ax2.spines["right"].set_color("blue")
ax2.spines["right"].set_linewidth(3.8)

line1, label1 = ax1.get_legend_handles_labels()
line2, label2 = ax2.get_legend_handles_labels()
ax2.legend(line1 + line2, label1 + label2, fontsize = 18)

years = mdates.YearLocator()
dates_Format = mdates.DateFormatter("%Y")

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(dates_Format)

ax1.set_xlim([datetime.date(2002,12,31), datetime.date(2022,7,22)])
#ax1.set_ylim(-1.5, 4.0)
#ax2.set_ylim(-130, 155)

ax1.set_yticks([-0.5,0.5,1.5,2.5],minor=True)
ax2.set_yticks([-40,-20,0,20,40,60,80,100,120,140,160],minor = False)
ax2.set_yticks([-30,-10,10,30,50,70,90,110,130,150],minor = True)

ax1.hlines(y=0, xmin = [datetime.date(2002,12,31)], xmax = [datetime.date(2022,7,22)], colors="black", linestyles = "dashed",linewidth = 1)

ax1.set_title("10Yr TIPS Yield vs WTI Oil (2003-2022)", fontsize = 24)

ax1.axvspan(datetime.date(2006,3,28), datetime.date(2007,7,18), facecolor = "lightgrey")
ax1.axvspan(datetime.date(2007,7,19), datetime.date(2008,7,15), facecolor = "wheat")
ax1.axvspan(datetime.date(2008,7,15), datetime.date(2008,11,24), facecolor = "lightgrey")
ax1.axvspan(datetime.date(2008,11,25), datetime.date(2013,6,7), facecolor = "wheat")
ax1.axvspan(datetime.date(2013,6,7), datetime.date(2014,7,30), facecolor = "lightgrey")
fig.text(0.1, 0.01,"Last updated at July 22,2022",fontsize = 12,color = "black")
ax1.grid(linestyle = "dashed")
#fig.tight_layout()
fig.savefig("10Yr TIPS Yield vs WTI Oil Price-2003-2022.tiff")
#plt.show()
