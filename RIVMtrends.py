from pytrends.request import TrendReq
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
  
with open('2ggdmeldingen.csv','r') as csvfile:
    next(csvfile)
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',markersize=1, label = "GGD Trend data")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('besmettingen')
plt.title('GGD trend data', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
