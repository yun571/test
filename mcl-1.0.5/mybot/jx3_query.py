import requests
import json
import time

url = "https://jx3api.com/app/"
serverName = '青梅煮酒'


def getHong(msg):
    data = {"name": msg, "token": "153166341"}
    r = requests.post(url + 'getMacro', data)
    print(r.text)
    return r.text


def getSaohua():
    data = {"token": "153166341"}
    r = requests.post(url + 'getRandom', data)
    r_data = json.loads(r.text)
    return r_data


def getDaily():
    data = {"server": serverName, "token": "153166341"}
    r = requests.post(url + 'getDaily', data)
    r_data = json.loads(r.text)
    return r_data['data']


def getGold():
    data = {"server": serverName, "token": "153166341"}
    r = requests.post(url + 'getGold', data)
    r_data = json.loads(r.text)
    return r_data['data']


def getServer(server = serverName):
    data = {"server": server, "token": "153166341"}
    r = requests.post(url + 'getServer', data)
    r_data = json.loads(r.text)
    return r_data['data']

def  getSand():
    data = {"server": serverName,"token": "153166341"}
    r = requests.post(url + 'getSand', data)
    r_data = json.loads(r.text)
    return r_data['data']


def getHeighten(name):
     data = {"name": name,"token": "153166341"}
     r = requests.post(url + 'getHeighten', data)
     r_data = json.loads(r.text)
     return r_data['data']


# def getSand():
#     data = {"server": serverName, "token": "153166341"}
#     r = requests.post(url + 'getSand', data)
#     r_data = json.loads(r.text)
#     img_url = r_data['data']['url']
#     img = requests.get(img_url).content

#     Time = time.strftime("%y-%m-%d-%H-%M-%S", time.localtime(time.time()))
#     with open(init.IMAGE_PATH + Time + '.jpg', 'wb') as i:
#         i.write(img)
#     return {'path': init.IMAGE_PATH + Time + '.jpg'}


def getFlower(name: str):
    data = {"server": serverName, "flower": name, "token": "153166341"}
    r = requests.post(url + 'getFlower', data)
    r_data = json.loads(r.text)
    return r_data['data']


def getExam(subject: str):
    data = {"question": subject, "token": "153166341"}
    r = requests.post(url + 'exam', data)
    r_data = json.loads(r.text)
    if r_data['code'] == 0:
        return ''
    return r_data['data']


if __name__ == '__main__':
    print(getExam("古琴"))