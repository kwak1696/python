import urllib.request
import urllib.parse
import json
import dateutil.parser
import _common


def use_upbit(time, box):
    target_list = box['target_list']
    fetch_result = box['fetch_result']
    work = len(target_list)
    _common.box_status(box, 'use_upbit start')
    for idx, symbol in enumerate(target_list):
        print('working upbit ' + str(idx) + ' / ' + str(work))
        #print(symbol, end=', ')
        market = symbol['market']
        coin = symbol['coin']
        try:
            # print('[market]', market)
            # print('[coin]', coin)
            # print('[step 1]')
            data = {}
            data['code'] = 'CRIX.UPBIT.' + market + '-' + coin
            data['count'] = 1
            data['to'] = time
            url_values = urllib.parse.urlencode(data, encoding='UTF-8')
            # print('[values]', url_values)  # The order may differ from below.
            #name=Somebody+Here&language=Python&location=Northampton
            url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1'
            full_url = url + '?' + url_values
            data = urllib.request.urlopen(full_url).read().decode()
            jsonObject = json.loads(data)
            #print('[result json]', jsonObject)
            tradePrice = jsonObject[0]['tradePrice']
            candleDate = dateutil.parser.parse(
                jsonObject[0]['candleDateTimeKst']).strftime(
                    '%Y-%m-%d %H:%M:%S')
            # print('[candleDate]', candleDate)
            # print('[tradePrice]', tradePrice)
            fetch_result.append(
                dict(coin=coin,
                     tradePrice=tradePrice,
                     candleDate=candleDate,
                     market=market,
                     time=time))
            print('upbit match', symbol)
            target_list.remove(symbol)
        except Exception as e:
            # print('에러남~', [market, coin], e)
            if (market == coin):
                target_list.remove(symbol)

    _common.box_status(box, 'use_upbit end')
    return box
