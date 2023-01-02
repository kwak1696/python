import sys
import datetime
from datetime import timedelta, timezone
import _ccxt
import _cap
import _google
import _swap


# python3 -m poetry install
def main():


    tz = timezone(timedelta(hours=9))
    dt_now = datetime.datetime.now(tz)
    d_today = datetime.date.today()

    print('[execute time]', dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    # 2020-09-02 11:35:16

    coinList = [
        'ETH', 'RFR', 'MANA', 'SOL', 'CRO', 'PUNDIX', 'BTC', 'TRX', 'GAS',
        'AXS', 'KRW', 'LTC', 'ADA', 'XLM', 'BORA', 'ETC', 'XRP', 'BCH', 'BTT',
        'APENFT', 'SOLO', 'MED', 'BSV', 'DOGE', 'NEO', 'XEM', 'QTUM', 'BTG',
        'BCHA', 'WAVES', 'ONT', 'XTZ', 'GRS', 'OMG', 'EOS', 'PCI', 'DKA',
        'SBD', 'EDR', 'ENJ', 'HIVE', 'AERGO', 'USD', 'USDT', 'BNB', 'CAKE'
    ]

    # krwList =[['KRW', 'EOS']]

    krwList = []
    btcList = []
    trxList = []
    usdtList = []
    bnbList = []
    failList = []

    for coin in coinList:
        krwList.append(dict(market='KRW', coin=coin))
        btcList.append(dict(market='BTC', coin=coin))
        usdtList.append(dict(market='USDT', coin=coin))
        trxList.append(dict(market='TRX', coin=coin))
        bnbList.append(dict(market='BNB', coin=coin))

    fulllist = krwList + btcList + usdtList + trxList + bnbList

    # fulllist = [btcList]

    if len(sys.argv) == 4:
        fulllist = [[sys.argv[1], sys.argv[2]]]
        time = sys.argv[3]
    elif len(sys.argv) == 3:
        fulllist = [[sys.argv[1], sys.argv[2]]]
        time = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    else:
        time = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    print('[time]', time)

    box = dict(fetch_result=[], target_list=fulllist)
    try:
        box = _ccxt.use_ccxt(time, box)
    except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
      print('예외가 발생했습니다.', e)
    box = _cap.use_cap(time, box)

    # box = _upbit.use_upbit(time, box)

    box = _swap.use_swap(time, box)

    _google.send_to_sheet(box)

    keypath = './main.key'
    keyfile = open(keypath, 'r', encoding="utf-8")
    key = keyfile.readline().strip()
    print('COMPLETE', key)

    target_list = box['target_list']
    fetch_result = box['fetch_result']
    for a in target_list:
        print(a)


if __name__ == "__main__":
    main()
