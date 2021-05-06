import MiraiConnnect as mirai
import serverAction as action
import json
import time
import requests
import websocket
try:
    import thread
except ImportError:
    import _thread as thread

myurl = '192.168.1.107:8080'
miraiURL = 'http://localhost:8080'
miraiKey = 'wqy123456'
miraiQQ = 1657663326
session = 'newsession'
groups =['879239861','255749834']

def sysinit():
    #获取版本
    mirai.getVersion(miraiURL=miraiURL)
    #获取session
    global session
    session = mirai.getAuth(miraiURL=miraiURL, miraiKey=miraiKey)
    #校验sesson并绑定bot
    mirai.verify(miraiURL=miraiURL, session=session, botNumber=miraiQQ)
    #开启webSocket
    mirai.startWebSocket(miraiURL=miraiURL, session=session)
    #释放sesson
    #mirai.release(miraiURL=miraiURL,session=session,botNumber=miraiQQ)


def on_message(ws, message):
    incomeJson = json.loads(message)
    if incomeJson['messageChain'][1]['type'] == 'Plain':
        incomeQQ = incomeJson['sender']['id']
        incomeMemberName = incomeJson['sender']['memberName']
        incomeGroupChatID = incomeJson['sender']['group']['id']
        incomeMessage = incomeJson['messageChain'][1]['text']
        temp = 'Get income message from GroupChat {} named {}(QQ:{}) with text: {}'.format(
            incomeGroupChatID, incomeMemberName, incomeQQ, incomeMessage)
        print(temp)
        action.judge(message=incomeMessage,
                     QQ=incomeQQ,
                     name=incomeMemberName,
                     group=incomeGroupChatID,
                     session=session)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        print('nsRobot Running!')
        time.sleep(1)

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    sysinit()
    wsURL = 'ws://' + myurl + '/message?sessionKey=' + session
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url=wsURL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
