import sys
import json

import requests
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import plotly

plotly.tools.set_credentials_file(username='', api_key='')

def main():
    num = sys.argv[1]
    date = sys.argv[2]
    print('股票編號: %s' %(num))
    print('日期: %s' %(date))

    num = int(num)
    date = int(date)
    response = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%d' %(date) + '&stockNo=%d' %(num))
    # print(response.text)

    res_json = json.loads(response.text)
    # print(type(res_json))

    # topic = pd.DataFrame(res_json['fields'])
    df = pd.DataFrame(res_json['data'])
    df.columns = ['date', 'shares', 'amount', 'open', 'high', 'low', 'close', 'change', 'turnover']
    # print(topic)
    print((df))

    # datelist = []
    
    # for i in range(len(df)):
    #     datelist.append(df['date'][i])
    # df.index = datelist  #索引值改成日期
    # df = df.drop(['date'],axis = 1)
    # print(df)
    # print(type(df['shares']))


    trace = go.Ohlc(x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])
    data = [trace]
    py.plot(data, filename='simple_candlestick')


if __name__ == "__main__":
    main()
