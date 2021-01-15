from bs4 import BeautifulSoup
import requests
import re

import time
from datetime import datetime

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


import os
import sys

MAINCAPTION='@twcBPbot 에이펙 조회 /start \n지점 전체조회 /all \n 그 외 /텍스트 로 필터링(ex: /성수역)\n'
LASTTIME = '';

LASTRESULT = ''
CHANNELID = sys.argv[2]



def getMenu(filterText):


    result = ''
    url = 'https://blog.naver.com/PostList.nhn?blogId=babplus123&from=postList&categoryNo=1'
    con = requests.get(url)

    html = con.text
    soup = BeautifulSoup(con.content, 'html.parser')
    titleDIV = soup.find('div', id='title_1').find('span').getText()

    titleDAY = re.sub('밥플러스 (\d*)월 (\d*)일.*', r'\1-\2', titleDIV)

    print('titleDAY : ' + titleDAY)

    result += titleDIV + '\n'

    postDIV = soup.find('div', id='postViewArea')

    # print(postDIV)
    result += '-------------------------------' + '\n'
    cnt = 0
    for tt in postDIV.find_all('p'):
        ftext = tt.getText().strip()
        if ftext.find(':') > 0:
            if ftext.find(filterText) > 0:
                cnt = 1
            else:
                cnt = 0
        if 1 == cnt:
            result += ftext + '\n'

    result += '-------------------------------' + '\n'

    print(datetime.now())
    print(result)

    return result


# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)


    my_token = sys.argv[1]  # 아까 만든 봇의 토큰값 입력
    bot = telegram.Bot(token=my_token)  # bot 선언

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
        print('마지막응답')
        print(bot.get_updates()[0].channel_post)
        print(bot.get_updates()[0].message)
        print(bot.username)

    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
            global LASTRESULT;
            global LASTTIME;
            print(time.strftime('%H:%M', time.localtime(time.time())));
            if(LASTTIME =='' or time.strftime('%H:%M', time.localtime(time.time())) == '12:34'):
                r = getMenu('센터')
                if LASTRESULT != r:
                    LASTTIME = datetime.now()
                    LASTRESULT = r
                    bot.sendMessage(chat_id=
                    CHANNELID, text='점심시간입니다~!' + LASTRESULT + MAINCAPTION)

        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:  # your bot can receive updates without messages
            print('새요청')
            print(update.message.text)
            title=MAINCAPTION
            filter=':'
            txt=''
            inputtxt=update.message.text.split('/')
            if len(inputtxt) == 2:
                if inputtxt[1] == 'start':
                    filter = '센'
                    title += '필터조건 : ' + filter
                elif inputtxt[1] != 'all':
                    filter = inputtxt[1]
                    title += '필터조건 : ' + filter
                txt=getMenu(filter)
            update.message.reply_text(txt+'\n'+title)  # Reply to the message


if __name__ == '__main__':
    main()
