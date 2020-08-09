from flask import Flask
import tushare as ts
import  pandas as pd
import  numpy as np

app = Flask(__name__)
@app.route('/index',methods=['post'])
def app():
    # 获取交易日历
    ts.set_token('dc0e4cf15e7726c4f46fd4a78b50ffc7c01a080322b536d42c5d55ee')
    pro = ts.pro_api()
    trade_cal_df = pro.trade_cal(exchange='', start_date='20200101', end_date='20200805', fields='exchange,cal_date,is_open,pretrade_date' )
    print(trade_cal_df)

    stock_basic_df = pro.stock_basic(is_hs='',list_status='L',exchange='',fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,is_hs')
    print(stock_basic_df)

    # hs_const_sz_df = pro.hs_const(hs_type='SZ',is_new='1',fields='ts_code,hs_type,in_date,out_date,is_new')

    # hs_const_sh_df = pro.hs_const(hs_type='SH',is_new='1',fields='ts_code,hs_type,in_date,out_date,is_new')

    stock_company_df = pro.stock_company(ts_code='600703.SH',exchange='',fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')
    print(stock_company_df)

    new_share_df = pro.new_share(start_date='20200701',end_date='20200801',fields='ts_code,sub_code,name,ipo_date,issue_date,amount,market_amount,price,pe,limit_amount,funds,ballot')
    print(new_share_df)

if __name__ == '__main__':
    app()
