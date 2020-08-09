# -*- coding:utf-8 -*-
from flask import Flask
import tushare as ts
import  pandas as pd
import  numpy as np
import  df_write_mysql
import tushare as ts

def daily():
    write_mysql = df_write_mysql('localhost','3306','root','','stock')
    sql = 'INSERT INTO stock.daily(ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount) VALUES ();'
    write_mysql.mysql_connect.execut(sql)

if __name__ == '__main__':
    daily()






