#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:47:15 2020

@author: lavend
"""

import os

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from guess_number import Guesser

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body)
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if event.source.user_id:
        _guesser = Guesser.all_guessers.setdefault(event.source.user_id, Guesser())
        if _guesser.state == 'from':
            message = '請輸入起始數字：'
            
        elif _guesser.state == 'to':
            message = '請輸入結束數字:'
            
        elif _guesser.state == 'guess':
            message = _guesser.feedback(event.message.text)
            
        if _guesser.state == 'end':
            del Guesser.all_guessers[event.source.user_id]
            
        message = f'{message}\n{event.source.user_id}'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print(f'listen on port: {port}')
    app.run(host='0.0.0.0', port=port)
