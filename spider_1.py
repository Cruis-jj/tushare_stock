import urllib.request
import json
# import  pymysql
# from pyspark.sql import SparkSession
# from pyspark.sql.types import DecimalType
# from pyspark.sql.functions import *
# import pyspark.sql.functions as F
from datetime import datetime, date, timedelta

today = date.today()
today1 = datetime.now()
first = today.replace(year=2018,day=1)
last_month_day = first + timedelta(days= -1)
print(today,today1,first,last_month_day)
print(type(today),type(today1))
yesterday = (today + timedelta(days= -1)).strftime("%Y%m%d")
yesterday11 = (today + timedelta(days= -1))
print(yesterday,yesterday11)
a = type(yesterday)
b = type(yesterday11)
print(a, b)
today2 = datetime.strptime(yesterday,'%Y%m%d') + timedelta(days = 1)
print(f"today = {today2}")

last_month_first =(datetime(last_month_day.year,last_month_day.month,1)).strftime("%Y-%m-%d")
last_month_first1 = (last_month_day.replace(day= 1))
last_month_first2 = (datetime(2017,12,1))
print(last_month_first,last_month_first1,last_month_first2)


atoday = date.today()
atoday1 = datetime.now()
atowrrow = atoday1 + timedelta(days= 1)
print('--------------')
print(atoday,atoday1,atowrrow)
