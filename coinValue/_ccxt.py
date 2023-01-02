import ccxt
import _common


def use_ccxt(time, box):
    _common.box_status(box, 'use_ccxt start')
    target_list = box['target_list']
    fetch_result = box['fetch_result']
    banks = [ccxt.binance(), ccxt.upbit()]
    for bank in banks:

        results = bank.fetch_tickers()
        for k in results.keys():
            x = results[k]
            target = next((symbol for symbol in target_list
                           if symbol['coin'] + '/' + symbol['market'] == k),
                          None)
            target2 = next((symbol for symbol in target_list
                            if symbol['coin'] + '_' + symbol['market'] == k),
                           None)
            if (target):
                print('ccxt match', target, k)
                symbol_receive = x['symbol'].split('/')
                fetch_result.append(
                    dict(coin=symbol_receive[0],
                         tradePrice=x['close'],
                         candleDate=x['datetime'],
                         market=symbol_receive[1],
                         time=time))
                target_list.remove(target)
            elif (target2):
                print('ccxt match', target2, k)
                symbol_receive = x['symbol'].split('_')
                fetch_result.append(
                    dict(coin=symbol_receive[0],
                         tradePrice=x['close'],
                         candleDate=x['datetime'],
                         market=symbol_receive[1],
                         time=time))
                target_list.remove(target2)

    box['target_list'] = target_list
    box['fetch_result'] = fetch_result
    _common.box_status(box, 'use_ccxt end')
    return box
