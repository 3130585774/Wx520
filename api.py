# -*- coding:utf-8 -*-
import requests
import datetime

together_day = "xxxx-xx-xx"
birthday = "xxxx-xx-xx"
timeappkey = ""
timesign = ""
weatherkey = ''
locationpos = "00.00,00.00"

timeapi_url = 'http://api.k780.com/?app=life.time&appkey={}&sign={}&format=json'.format(timeappkey, timesign)
now_weather_url = "https://devapi.qweather.com/v7/weather/now?key={}&location={}".format(weatherkey, locationpos)
three_day_weather_url = "https://devapi.qweather.com/v7/weather/3d?key={}&location={}".format(weatherkey, locationpos)
seven_day_weather_url = "https://devapi.qweather.com/v7/weather/7d?key={}&location={}".format(weatherkey, locationpos)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.42''80.67 Safari/537.36'
}


def get_now_weather():
    re = requests.get(now_weather_url, headers=headers).json()
    updateTime = str(datetime.datetime.strptime(re["now"]["obsTime"], "%Y-%m-%dT%H:%M+08:00").strftime(
        "%Y-%m-%d %H:%M"))  # 数据观测时间
    fxLink = re["fxLink"]  # 当前数据的响应式页面，便于嵌入网站或应用
    temp = re["now"]["temp"]  # 温度，默认单位：摄氏度
    feelsLike = re["now"]["feelsLike"]  # 体感温度，默认单位：摄氏度
    windDir = re["now"]["windDir"]  # 风向
    windScale = re["now"]["windScale"]  # 风力等级
    windSpeed = re["now"]["windSpeed"]  # 风速，公里/小时
    humidity = re["now"]["humidity"]  # 相对湿度，百分比数值
    text = re["now"]["text"]
    data = {"updateTime": updateTime,
            "fxLink": fxLink,
            "temp": temp,
            "feelsLike": feelsLike,
            "windDir": windDir,
            "windScale": windScale,
            "windSpeed": windSpeed,
            "humidity": humidity,
            "text": text,
            }
    return data


def get_day_weather(day=0):
    re = requests.get(three_day_weather_url, headers=headers).json()
    updateTime = str(
        datetime.datetime.strptime(re["now"]["obsTime"], "%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S"))
    fxLink = re["fxLink"]
    daily = re["daily"][day]
    sunrise = daily["sunrise"]  # 日出时间
    sunset = daily["sunset"]  # 日落时间
    tempMax = daily["tempMax"]  # 当天最高温度
    tempMin = daily["tempMin"]  # 当天最低温度
    textDay = daily["textDay"]  # 白天文字描述
    textNight = daily["textNight"]  # 夜晚文字描述
    return {"updateTime": updateTime,
            "fxLink": fxLink,
            "sunrise": sunrise,
            "sunset": sunset,
            "tempMax": tempMax,
            "tempMin": tempMin,
            "textDay": textDay,
            "textNight": textNight,
            }


def get_date():
    """
    {'sysTime2': '2022-08-22 08:25:05', 'sysTime1': '20220822082505'}
    """
    re = requests.get(timeapi_url, headers=headers).json()
    # print(re)
    now_date = re["result"]["datetime_1"][0:10]
    return now_date


def get_together_days():
    date1 = datetime.datetime.strptime(get_date(), "%Y-%m-%d")
    date2 = datetime.datetime.strptime(together_day, "%Y-%m-%d")
    num = date1 - date2
    return num.days


def get_birthday():
    date1 = datetime.datetime.strptime(get_date(), "%Y-%m-%d")
    date2 = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    num = date2 - date1
    return num.days