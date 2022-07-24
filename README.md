# 10 Yr TIPS Bond yield vs WTI Oil price

## Motivation
The purpose of this repository is to show the relationships between 10 Yr TIPS Bond yield and WTI oil price through collection of bond yield data from U.S. Department of the Treasury and WTI price from Yahoo Finance. The relationship between these two is visualized by plotting a [line graph.](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/10Yr%20TIPS%20Yield%20vs%20WTI%20Oil%20Price-2003-2022.png)

## Background
Treasury Inflation Protection Securities or TIPS is an inflation-protected Treasury bonds, where principal amount on these bonds 
is adjusted in proportion to increases in the Consumer Price Index (CPI).
Hence, they provide a constant stream of income in real (inflation-adjusted) dollars. 
Yields on TIPS bonds should be interpreted as real interest rates.([1](https://www.amazon.com/dp/1259277178/ref=sspa_dk_detail_1?psc=1&pd_rd_i=1259277178&pd_rd_w=i30ms&content-id=amzn1.sym.837c9c40-8722-4df3-9922-02a1f44f92b9&pf_rd_p=837c9c40-8722-4df3-9922-02a1f44f92b9&pf_rd_r=PHD2690HE8DVPBSR31DG&pd_rd_wg=wovlr&pd_rd_r=e821867f-a7b1-41c9-8184-8c3e2e2f728f)) 

Crude oil, also known as the blood of industry, plays an essential role in real market and financial markets. Like other commodities, price of crude oil can be affected by many factors such as supply-demand, geopolitical events, macroeconomic policies etc. Recent articles ([2](https://www.sciencedirect.com/science/article/pii/S0140988321001109),[3](https://seekingalpha.com/article/4484793-price-of-oil-determined-real-yield)) shows that bond yield can be used as tool to predict the prices of crude oil. Generally, West Texas Intermediate(WTI) and Brent Crude serve as reference for buyers and sellers of crude oil. Therefore, WTI oil prices from Yahoo Finance were used for this project.

## To begin
1. Bond yield data for all different time maturities were gather from U.S. Department of the Treasury using this [program.](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/treasury_real_yield.py)
2. All the bond yield data were [compiled](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/join_file.py) into a [single csv file.](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/treasury_real_yield_all.csv)
3. WTI oil prices were pulled from [Yahoo Finance](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/WTI.py) as [csv](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/WTI_price.csv) file.
4. Both bond yield data and WTI price join together into one [csv](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/real_yield_vs_WTI.csv) file.
5. 10 Yrs Bond Yield was selected and [plotted](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/plot.py) together with WTI price. The graph was [shown](https://github.com/lance8831/Treasury-real-yield-vs-WTI/blob/main/10Yr%20TIPS%20Yield%20vs%20WTI%20Oil%20Price-2003-2022.png) here.
 
## Discussion
From the visualization of the graph,10 Yr TIPS yield and WTI price is negatively correlated with each other. The region highlighted lightgrey regions shows that oil price tend to goes up when bond yield started to decrease. The orange highlighted shows the opposite observation. Hence it can be seen that the bond yield lead the value of WTI price.([3](https://seekingalpha.com/article/4484793-price-of-oil-determined-real-yield))

## Reference
1. [Investment, 11th edition, Z. Bodie, A. Kane and A. J. Marcus, McGraw Hill, 2017](https://www.amazon.com/dp/1259277178/ref=sspa_dk_detail_1?psc=1&pd_rd_i=1259277178&pd_rd_w=i30ms&content-id=amzn1.sym.837c9c40-8722-4df3-9922-02a1f44f92b9&pf_rd_p=837c9c40-8722-4df3-9922-02a1f44f92b9&pf_rd_r=PHD2690HE8DVPBSR31DG&pd_rd_wg=wovlr&pd_rd_r=e821867f-a7b1-41c9-8184-8c3e2e2f728f)
2. [Z. Dai and J. Kang, Bond Yield and crude oil prices predictability, Energy Economics, 97, (2021), 105205](https://www.sciencedirect.com/science/article/pii/S0140988321001109)
3. [J. V. Erlach, How The Price Of Oil Is Determined: Real Yield Again, Seeking Alpha, 2022](https://seekingalpha.com/article/4484793-price-of-oil-determined-real-yield)
4. [Price of Oil, Last Updated at 13 July 2022](https://en.wikipedia.org/wiki/Price_of_oil)

## Reference for python program
1. [Python for Everybody Specialization, Coursera](https://www.coursera.org/specializations/python)
2. [Python for Everybody: Exploring Data in Python 3, Dr. C. Severance, S. Blumenberg, E. Hauser, A. Andrion, 2016](https://www.amazon.com/Python-Everybody-Exploring-Data/dp/1530051126)
3. [Practical Web Scraping for Data Science: Best Practices and Examples with Python, S. V. Broucke, B. Baesens, 2018](https://www.amazon.com/Practical-Web-Scraping-Data-Science-ebook/dp/B07CH3CH51/ref=sr_1_1crid=1YJCM3FCB3RHP&keywords=practical+web+scraping+for+data+science&qid=1658660421&sprefix=Practical+web+sc%2Caps%2C236&sr=8-1)
4. [mshadish,yield-curve, 2021](https://github.com/mshadish/yield-curve)
5. [limchiahooi, us-treasury-yield-spread, 2022](https://github.com/limchiahooi/us-treasury-yield-spread#us-treasury-yield-spread)

# Disclosure
I have no stock, option or similar derivative position in any of the companies mentioned, and no plans to initiate any such positions within the next 72 hours. I work on this project myself, and it expresses my own opinions. I am not receiving compensation for it. I have no business relationship with any company whose stock is mentioned in this project. Nothing in the project constitutes professional and/or financial advice, nor does any information on the project constitute a comprehensive or complete statement of the matters discussed or the law relating thereto. 
