import urllib.request
import urllib.parse
import json
import _common


def use_cap(time, box):
    _common.box_status(box, 'use_cap start')
    target_list = box['target_list']
    for idx, item in enumerate(target_list): 
      print('target_list - ', item)
    fetch_result = box['fetch_result']
    work = len(target_list) 

    keypath = './_cap.key'
    keyfile = open(keypath, 'r', encoding="utf-8")
    key = keyfile.readline().strip()
    headers = {'X-CMC_PRO_API_KEY': key, 'Accept': 'application/json'}
    params = {'start':'1','limit':'5000','convert':'KRW'}
    # case 1
    url_values = urllib.parse.urlencode(params, encoding='UTF-8')
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    full_url = url + '?' + url_values
    req = urllib.request.Request(full_url, None, headers)
    data = urllib.request.urlopen(req).read().decode()
    # case 2
    # data = f.readline()
    # case 3
    # data = '{"status":{"timestamp":"2022-12-24T00:50:32.600Z","error_code":0,"error_message":null,"elapsed":26,"credit_count":1,"notice":null,"total_count":8963},"data":[{"id":1,"name":"Bitcoin","symbol":"BTC","slug":"bitcoin","num_market_pairs":9906,"date_added":"2013-04-28T00:00:00.000Z","tags":["mineable","pow","sha-256","store-of-value","state-channel","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","galaxy-digital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio"],"max_supply":21000000,"circulating_supply":19241806,"total_supply":19241806,"platform":null,"cmc_rank":1,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2022-12-24T00:49:00.000Z","quote":{"KRW":{"price":21530062.388250966,"volume_24h":19413727812833.043,"volume_change_24h":-7.7128,"percent_change_1h":-0.02599766,"percent_change_24h":0.10830762,"percent_change_7d":0.30503438,"percent_change_30d":1.6297992,"percent_change_60d":-12.98427925,"percent_change_90d":-11.31982618,"market_cap":414277283642621.75,"market_cap_dominance":39.8958,"fully_diluted_market_cap":452131310153273,"tvl":null,"last_updated":"2022-12-24T00:50:25.000Z"}}},{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","num_market_pairs":6317,"date_added":"2015-08-07T00:00:00.000Z","tags":["pos","smart-contracts","ethereum-ecosystem","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","hashkey-capital-portfolio","kenetic-capital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio","injective-ecosystem"],"max_supply":null,"circulating_supply":122373866.2178,"total_supply":122373866.2178,"platform":null,"cmc_rank":2,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2022-12-24T00:49:00.000Z","quote":{"KRW":{"price":1562611.2503991553,"volume_24h":6119993307191.53,"volume_change_24h":-9.508,"percent_change_1h":-0.0853786,"percent_change_24h":0.33874843,"percent_change_7d":3.67727845,"percent_change_30d":3.35127889,"percent_change_60d":-9.19920778,"percent_change_90d":-7.53673726,"market_cap":191222780106775.4,"market_cap_dominance":18.4136,"fully_diluted_market_cap":191222780106776,"tvl":null,"last_updated":"2022-12-24T00:50:25.000Z"}}},{"id":825,"name":"Tether","symbol":"USDT","slug":"tether","num_market_pairs":45497,"date_added":"2015-02-25T00:00:00.000Z","tags":["payments","stablecoin","asset-backed-stablecoin","avalanche-ecosystem","solana-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","injective-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":66247647089.7764,"total_supply":73141766321.23428,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xdac17f958d2ee523a2206206994597c13d831ec7"},"cmc_rank":3,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2022-12-24T00:49:00.000Z","quote":{"KRW":{"price":1280.279062834021,"volume_24h":23193838371979.07,"volume_change_24h":-9.9738,"percent_change_1h":-0.13827592,"percent_change_24h":0.02314844,"percent_change_7d":-0.33196694,"percent_change_30d":0.09038429,"percent_change_60d":-0.00503861,"percent_change_90d":-0.0034948,"market_cap":84815475531057.89,"market_cap_dominance":8.1678,"fully_diluted_market_cap":93641872039779.81,"tvl":null,"last_updated":"2022-12-24T00:50:25.000Z"}}},{"id":3408,"name":"USD Coin","symbol":"USDC","slug":"usd-coin","num_market_pairs":9230,"date_added":"2018-10-08T00:00:00.000Z","tags":["medium-of-exchange","stablecoin","asset-backed-stablecoin","fantom-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":44141069100.062675,"total_supply":44141069100.062675,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"},"cmc_rank":4,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2022-12-24T00:49:00.000Z","quote":{"KRW":{"price":1280.3098311038077,"volume_24h":2378106835991.807,"volume_change_24h":-0.4384,"percent_change_1h":-0.13827354,"percent_change_24h":0.02794027,"percent_change_7d":-0.31709219,"percent_change_30d":-0.01331588,"percent_change_60d":0.00335257,"percent_change_90d":0.0025376,"market_cap":56514244724242.75,"market_cap_dominance":5.4422,"fully_diluted_market_cap":56514244724248.54,"tvl":null,"last_updated":"2022-12-24T00:50:25.000Z"}}},{"id":1839,"name":"BNB","symbol":"BNB","slug":"bnb","num_market_pairs":1161,"date_added":"2017-07-25T00:00:00.000Z","tags":["marketplace","centralized-exchange","payments","smart-contracts","alameda-research-portfolio","multicoin-capital-portfolio","bnb-chain"],"max_supply":200000000,"circulating_supply":159964635.88998353,"total_supply":159979963.59042934,"platform":null,"cmc_rank":5,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2022-12-24T00:49:00.000Z","quote":{"KRW":{"price":314628.1481675433,"volume_24h":494154317530.38873,"volume_change_24h":-28.1827,"percent_change_1h":-0.28101303,"percent_change_24h":0.17776585,"percent_change_7d":5.24148817,"percent_change_30d":-17.0392773,"percent_change_60d":-10.44487133,"percent_change_90d":-10.69382088,"market_cap":50329377162360.85,"market_cap_dominance":4.8466,"fully_diluted_market_cap":62925629633509.59,"tvl":null,"last_updated":"2022-12-24T00:50:25.000Z"}}}]}'

    jsonObject = json.loads(data)
        #print('[result json]', jsonObject)
    result = jsonObject['data']
    for idx, item in enumerate(result): 
      coin = item['symbol']
      quote = item['quote']
      for idx2, market in enumerate(quote): 
        # print('cap market visual check',market)
        target = next((symbol for symbol in target_list
                                  if symbol['coin'] + symbol['market'] == coin + market),
                                  None)
        if (target):
          tradePrice = item['quote'][market]['price']
          candleDate = item['quote'][market]['last_updated']
          vo=dict(coin=coin,
          tradePrice=tradePrice,
          candleDate=candleDate,
          market=market,
          time=time)
          # print('cap vo visual check',vo)
          fetch_result.append(vo)
          target_list.remove(target)
    box['target_list'] = target_list
    box['fetch_result'] = fetch_result
    _common.box_status(box, 'use_cap end')
    return box
