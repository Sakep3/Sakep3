import csv
import pprint

import pandas as pd

mylist=[]



mylist.append([1, "StockNum"])
mylist.append([1, "StockName"])
mylist.append([1, "StockInc"])
mylist.append([1, "StockPbr"])


print(mylist)


df1 = pd.DataFrame(
    data={'Code': [10]},
    index=["6758"]
)
print(df1)


#with open('data/inc.txt', encoding="utf-8") as f:
# reader = csv.reader(f)
# for row in reader:
#   print(row[0])
