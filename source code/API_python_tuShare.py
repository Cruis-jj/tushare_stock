from flask import Flask
import tushare as ts

print(ts.__version__)

app = Flask(__name__)
@app.route('/index',methods=['post'])
def app():
    ts.set_token('dc0e4cf15e7726c4f46fd4a78b50ffc7c01a080322b536d42c5d55ee')
    pro = ts.pro_api()
    df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
    print(df)

    df1 = pro.income(ts_code='600320.SH', start_date='20180101', end_date='20180730', fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')
    print(df1)


if __name__ == '__main__':
    app.run()


    # df = pro.daily(trade_date='20200325')
    # # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
    # start_dt = '20100101'
    # time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    # end_dt = time_temp.strftime('%Y%m%d')
    # # 建立数据库连接,剔除已入库的部分
    # db = pymysql.connect(host='localhost', user='root', passwd='', db='stock', charset='utf8')
    # cursor = db.cursor()
    # # 设定需要获取数据的股票池
    # stock_pool = ['603912.SH','300666.SZ','300618.SZ','002049.SZ','300672.SZ']
    # total = len(stock_pool)
    # # 循环获取单个股票的日线行情
    # for i in range(len(stock_pool)):
    #     try:
    #         df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
    #         # 打印进度
    #         print('Seq: ' + str(i+1) + ' of ' + str(total) + '   Code: ' + str(stock_pool[i]))