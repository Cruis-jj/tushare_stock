# -*- coding:utf-8 -*-
from flask import Flask
import tushare as ts
import pandas as pd
import  numpy as np
import df_write_mysql
import tushare as ts

def trade_cal():
    write_mysql = df_write_mysql.MySqlUtil('localhost','3306','root','','stock','trade_cal')
    print("连接mysql")

    ts.set_token('dc0e4cf15e7726c4f46fd4a78b50ffc7c01a080322b536d42c5d55ee')
    pro = ts.pro_api()
    trade_cal_df = pro.trade_cal(exchange='', start_date='20200101', end_date='20200805',fields='exchange,cal_date,is_open,pretrade_date')
    print(trade_cal_df)
    # sql = 'INSERT INTO stock.trade_cal(exchange,cal_date,is_open,pretrade_date) VALUES ();'
    conn = write_mysql.mysql_connect
    pd.io.sql.to_sql(trade_cal_df,'trade_cal',conn,schema='stock',if_exists='append')
    print("写入sql成功")

if __name__ == '__main__':
        print("开始")
        trade_cal()
        print("结束")

