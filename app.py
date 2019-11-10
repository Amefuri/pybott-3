from flask import Flask, request, abort, send_from_directory

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from yandex.Translater import Translater
from fuzzywuzzy import process ## import fuzz

app = Flask(__name__)

line_bot_api = LineBotApi('SYR/G9r+UQ/7iN73OIrvu1875aJZ8SEj225JyEXfPpwA0CFY1q3lD4u5syGqJsXxYSDWF7i6DXBIS7/8U+zZc+mGLlRswitN28R0isFWJ2ZD8m4ychCTjVS2L1eK2IU72Z/a/8Fi4wX4M4hE4/9wMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ef20eec7733d3c6750ba2e474f617703')
user_session = {} #database for user
tr = Translater()
tr.set_key('trnsl.1.1.20191108T161057Z.789702196707e5b2.41eba9a721c3e06bd2ae57a2a1189764eb9e1b8d') # Api key found on https://translate.yandex.com/developers/keys

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from yandex.Translater import Translater


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text_from_user = event.message.text
    replyToken = event.reply_token
    userID = event.source.user_id
    user_current_session = user_session[userID]['session']

    print('--- 0 --- ', user_current_session)

    if user_current_session == None and text_from_user == 'แปลข้อความ':
        action1 = MessageAction(label='English', text="English")
        qbtn1 = QuickReplyButton(action=action1)
        action2 = MessageAction(label='France', text="France")
        qbtn2 = QuickReplyButton(action=action2)
        action3 = MessageAction(label='German', text="German")
        qbtn3 = QuickReplyButton(action=action3)
        qreply = QuickReply(items=[qbtn1, qbtn2, qbtn3])
        text = TextSendMessage(text='ต้องการแปลเป็นภาษาอะไรดีคะ? กรุณระบุ', quick_reply=qreply)
        line_bot_api.reply_message(reply_token=replyToken, messages=text)
        user_session[userID]['session'] = "Selectlang"

    elif user_current_session == 'Selectlang':
        from translator2 import check_lang
        true_lang = check_lang(text_from_user)
        if true_lang is None:
            line_bot_api.reply_message(replyToken, messages=TextSendMessage('ฉันไม่สามารถแปลมันได้ กรุณาเลือกภาษาใหม่อีกครั้ง'))
        else:
            text = TextSendMessage('ท่านต้องการให้แปลจากไทยเป็น {} ใช่ไหมคะ'.format(true_lang))
            text2 = TextSendMessage('กรุณาพิมพ์ขอความที่ต้องการแปลค่ะ')
            line_bot_api.reply_message(replyToken, messages=[text, text2])
            user_session[userID]['session'] = 'textinput'
            user_session[userID]['lang'] = true_lang

    elif user_current_session == 'textinput':
        from translator2 import tran
        output = tran(text_from_user, to_lang=user_session[userID]['lang'], tr=tr)
        from Flex import Flex_output
        flex_to_reply = Flex_output(text=output)
        flex_object = Base.get_or_new_from_json_dict(flex_to_reply, FlexSendMessage)
        line_bot_api.reply_message(reply_token=replyToken, messages=flex_object)
        user_session[userID]['session'] = 'continue'

    elif user_current_session == 'continue':
        if text_from_user == 'แปลข้อความใหม่':
            text2 = TextSendMessage('กรุณาพิมพ์ขอความที่ต้องการแปลค่ะ')
            line_bot_api.reply_message(replyToken, messages=text2)
            user_session[userID]['session'] = 'textinput'
        elif text_from_user == 'ออกจากการแปล':
            text = TextSendMessage('ขอบคุณที่มาใช้บริการแปลภาษาคะ')
            line_bot_api.reply_message(replyToken, messages=text)
            user_session[userID]['session'] = None


@handler.add(FollowEvent)
def Greeting(event):
    userid = event.source.user_id
    user= {}
    user['session'] = None
    user['lang'] = None
    #user_session.update(user)
    user_session[userid] = user 
    #user_session[userid]['session'] = None
    line_bot_api.link_rich_menu_to_user(user_id=userid, rich_menu_id='richmenu-453915def80f37374f9b7b1988fe5526')

    text = TextSendMessage(text='สวัสดีค่ะยินดีต้อนรับเข้าสู่บริการแปลข้อความ')
    reply_token = event.reply_token
    line_bot_api.reply_message(reply_token, messages=text)



import os
@app.route('/<picname>')
def getImage(picname):
    current_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_path, 'pic')
    return send_from_directory(dir_path, picname)

@app.route('/<picname>/1040')
def getImage1040(picname):
    current_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_path, 'pic')
    return send_from_directory(dir_path, picname)

if __name__ == "__main__":
    app.run()