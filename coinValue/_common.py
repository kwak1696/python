def box_status(box, caption):
    target_list = box['target_list']
    fetch_result = box['fetch_result']
    print('[' + caption + ']', len(fetch_result), len(target_list))
