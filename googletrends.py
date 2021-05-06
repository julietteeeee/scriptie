from pytrends.request import TrendReq
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import csv
startTime = time.time()
pytrend = TrendReq(hl='NL', tz=360)

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("Keywords")

dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-11-30 2021-04-27',
     geo='NL')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_trends.csv')

executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))

x = []
y = []
  
with open('search_trends.csv','r') as csvfile:
    next(csvfile)
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[12]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o', markersize=1 ,label = "Google Trend data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Zoekvolume')
plt.title('Google trend data', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
