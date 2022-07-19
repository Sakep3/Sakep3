import csv
import pprint

with open('data/inc.txt', encoding="utf-8") as f:
 reader = csv.reader(f)
 for row in reader:
   print(row[0])
 #print(f.read())