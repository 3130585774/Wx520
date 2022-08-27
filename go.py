# -*- encoding:utf-8 -*-

import requests
import json
from Wx520 import api

x_opid = 'oru0V6FVzfvObMxpA9z0pQYNbis0'
m_opid = 'oru0V6D6yWiKM7LTSy4Ha2v7nbLQ'


class SendMessage:
    def __init__(self):
        self.appID = 'wx10ea974fcab62a3f'
        self.appsecret = 'dd1510048c00b19cc0b738187fd7e099'
        self.x_opid = 'oru0V6FVzfvObMxpA9z0pQYNbis0'
        self.m_opid = 'oru0V6D6yWiKM7LTSy4Ha2v7nbLQ'
        self.access_token = self.get_access_token()
        # self.opend_ids = self.get_openid()

    def get_access_token(self):
        """
        获取微信公众号的access_token值
        """
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'. \
            format(self.appID, self.appsecret)
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
        }
        response = requests.get(url, headers=headers).json()
        access_token = response.get('access_token')
        # print(access_token)
        return access_token

    def get_openid(self):
        """
        获取所有粉丝的openid
        """
        next_openid = ''
        url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
            self.access_token, next_openid)
        ans = requests.get(url_openid)
        # print(ans.content)
        open_ids = json.loads(ans.content)['data']['openid']
        return open_ids

    def sendmsg(self, msg, open_id=''):
        """
        发送文本消息
        """
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}".format(self.access_token)
        # print(url)
        open_id = self.m_opid
        # open_id = self.x_opid
        body = {
            "touser": open_id,
            "msgtype": "text",
            "text":
                {
                    "content": msg
                }
        }
        data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
        # print(data)
        response = requests.post(url, data=data)
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        result = response.json()
        # print(result)

    def card_msg(self):
        """
        卡片信息
        """
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(self.access_token)
        # print(url)
        weather = api.get_now_weather()
        get_date = api.get_together_days()
        body = {
            # "touser": x_opid,
            "touser": m_opid,
            "template_id": "MuvxBGiPlbsIQhTkqqn46K9OkxtK7qtdrRfQmFwmkjk",
            "url": weather["fxLink"],
            "topcolor": "#FF0000",
            "data": {
                "text": {
                    "value": weather["text"],
                    "color": "#173177"
                },
                "temp": {
                    "value": weather["temp"],
                    "color": "#173177"
                },
                "feelsLike": {
                    "value": weather["feelsLike"],
                    "color": "#173177"
                },
                "humidity": {
                    "value": weather["humidity"],
                    "color": "#173177"
                },
                "windDir": {
                    "value": weather["windDir"],
                    "color": "#173177"
                },
                "windScale": {
                    "value": weather["windScale"],
                    "color": "#173177"
                },
                "updateTime": {
                    "value": weather["updateTime"],
                    "color": "#173177"
                },
                "together_day": {
                    "value": str(api.get_together_days()),
                    "color": "#173177"
                },
                "birthday": {
                    "value": str(api.get_birthday()),
                    "color": "#173177"
                },
            }
        }

        data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
        # print(data)
        response = requests.post(url, data=data)
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        result = response.json()
        # print(result)

    def custom_menu(self):
        """
        自定义菜单
        """
        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}".format(self.access_token)
        # print(url)
        body = {
            "button": [
                {
                    "name": "菜单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "官网",
                            "url": "https://www.noeye.xyz/"
                        }
                    ]
                }
            ]
        }
        data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
        response = requests.post(url, data=data)
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        result = response.json()
        # print(result)


if __name__ == "__main__":
    sends = SendMessage()
    # data = 'Hello,3Nod!'
    # sends.sendmsg("我爱你！"+api.get_date())
    # sends.custom_menu()
    sends.card_msg()
    print("Successful")
    # sends.send_media_to_user("image", './test.png')
