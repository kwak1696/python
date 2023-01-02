import dateutil.parser
import _common


def send_to_sheet(box):
    fetch_result = box['fetch_result']
    _common.box_status(box, 'send_to_sheet start')
    print('------------')
    for item in fetch_result:
        queryTime = dateutil.parser.parse(item['time'])
        data = {
            '타임스탬프': queryTime,
            '일시': queryTime,
            '마켓': item['market'],
            '코인': item['coin'],
            '금액': item['tradePrice'],
            '비고': item['candleDate']
        }
        print(*data.values(), sep=',')
    print('------------')
    _common.box_status(box, 'send_to_sheet end')
