import _common


def use_swap(time, box):
    target_list = box['target_list']
    fetch_result = box['fetch_result']

    _common.box_status(box, 'use_swap start')

    markets = ['BTC', 'KRW', 'TRX', 'BNB']
    for d0 in markets:
        for d1 in markets:
            for d2 in markets:
                for d3 in markets:
                    if (d1 != d2 and d1 != d3 and d2 != d3):
                        dp1 = next(
                            (result['tradePrice'] for result in fetch_result
                             if result['market'] == d2 and result['coin'] == d3
                             ), None)
                        dp2 = next(
                            (result['tradePrice'] for result in fetch_result
                             if result['market'] == d1 and result['coin'] == d2
                             ), None)
                        dp3 = next(
                            (result['tradePrice'] for result in fetch_result
                             if result['market'] == d1 and result['coin'] == d3
                             ), None)
                        if (dp1):
                            print(d2, '_', d3, ' market is skip ', dp1)
                        elif (dp2 and dp3):
                            tradePrice = dp3 / dp2
                            swap_result = dict(coin=d3,
                                               tradePrice=tradePrice,
                                               candleDate=time,
                                               market=d2,
                                               time=time)
                            print('market swap_result : ', swap_result)
                            fetch_result.append(swap_result)
        for symbol in target_list:
            market = symbol['market']
            coin = symbol['coin']
            try:
                for diffmarket in markets:
                    market_diffmarket = next(
                        (result['tradePrice'] for result in fetch_result
                         if diffmarket != market and result['market'] == market
                         and result['coin'] == diffmarket), None)
                    diffmarket_market = next(
                        (result['tradePrice'] for result in fetch_result
                         if diffmarket != market and result['market'] ==
                         diffmarket and result['coin'] == market), None)
                    if (market_diffmarket):
                        diffmarket_ukn = next(
                            (result['tradePrice'] for result in fetch_result
                             if result['market'] == diffmarket
                             and result['coin'] == coin), None)
                        if (diffmarket_ukn):
                            tradePrice = market_diffmarket * diffmarket_ukn
                            swap_result = dict(coin=coin,
                                               tradePrice=tradePrice,
                                               candleDate=time,
                                               market=market,
                                               time=time)
                            print('swap_result : ', swap_result)
                            fetch_result.append(swap_result)
                            target_list.remove(symbol)
                            break
                    elif (diffmarket_market):
                        market_ukn = next((result['tradePrice']
                                           for result in fetch_result
                                           if result['market'] == market
                                           and result['coin'] == coin), None)
                        if (market_ukn):
                            tradePrice = market_ukn / diffmarket_market
                            swap_result = dict(coin=coin,
                                               tradePrice=tradePrice,
                                               candleDate=time,
                                               market=market,
                                               time=time)
                            print('swap_result : ', swap_result)
                            fetch_result.append(swap_result)
                            target_list.remove(symbol)
                            break
            except:
                # print('에러남~', [market, coin])
                if (market == coin):
                    target_list.remove(symbol)
    _common.box_status(box, 'use_swap end')
    return box
