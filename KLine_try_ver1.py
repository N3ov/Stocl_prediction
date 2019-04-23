import sys
import json

import requests
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import plotly

plotly.tools.set_credentials_file(username='N3ov', api_key='dC1ZcLLdu0xgNzwjguyI')

def getData(code, date):
    response = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%d&stockNo=%d' % (date, code))
    return json.loads(response.text)

def drawPlot(data):
    df = pd.DataFrame(data)
    df.columns = [
        'date',
        'shares',
        'amount',   # 交易量
        'open',     # 開盤價
        'high',     # 最高價
        'low',      # 最低價
        'close',    # 收盤價
        'change',
        'turnover'
    ]
    trace = go.Ohlc(x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])
    data = [trace]
    py.plot(data, filename='simple_candlestick')


def main():
    code = sys.argv[1]
    date = sys.argv[2]
    print('股票編號: %s' %(code))
    print('日期: %s' %(date))

    code = int(code)
    date = int(date)
    data = getData(code, date)

    drawPlot(data)

if __name__ == "__main__":
    main()
