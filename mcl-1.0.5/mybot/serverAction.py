#动作指令判断函数，在此函数内判断需要采取的动作并起调相关子处理函数
#输入-message: 收到的全文本信息
#输入-QQ: 发信息的QQ号，通过主程序传递即可
#输入-name: 发来信息的昵称，用于后续相关确认通知，虽然大概率新版本不需要这样了
#输入-group: 接收到信息的群聊ID，用于后续相关确认通知，虽然大概率新版本不需要这样了
import jx3_query as query
import MiraiConnnect as mirai
import serverAction as action
import json
import time
import requests
import websocket
import testMirai


def judge(message, QQ, name, group, session):
    if str(group) in testMirai.groups:
        requestData = ""
        res = ""
        data = ""
        if message[:2] == '骚话':
            data = query.getSaohua()
            print(data)
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": data['data']['text']
                }]
            }

        if message[:1] == '宏':
            command = message[1:]
            commandPart = command.split()
            data = query.getHong(commandPart[0])
            print(data)
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": data
                }]
            }

        if message[:2] == '日常':
            data = query.getDaily()
            # data = data[1:-1]
            dataStr = u"日期："+data['Date']+"\n"\
            u"星期："+data['Week']+"\n"\
            u"大战："+data['DayWar']+"\n"\
            u"战场："+data['DayBattle']+"\n"\
            # u"矿车："+data['DayCommon']+"\n"\
            # u"DayDraw："+data['DayDraw']+"\n"\
            u"公共任务："+data['WeekCommon']+"\n"\
            u"小周长："+data['WeekFive']+"\n"\
            u"大周长："+data['WeekTeam']+"\n"
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": dataStr
                }]
            }

        if message[:2] == '金价':
            data = query.getGold()
            datastr = '服务器：  '+data['server'] + '\n' + '万宝楼：   '+data['wanbaolou'] + '\n' + '游募：      '+data[
                'youmu'] + '\n' + 'uu898：   '+data['uu898'] + '\n' + 'dd373：   '+data[
                    'dd373'] + '\n' + '5173：     '+data['5173'] + '\n' + '7881：     '+data['7881']+''
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": datastr
                }]
            }

        if message[:2] == '开服':
            data = query.getServer()
            print (data)
            if str(data['status']) == '1':
                datastr = '已开服'
            else:
                datastr = '未开服'
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": query.serverName+': '+datastr
                }]
            }
        
        if message[:2] == '沙盘':
            data = query.getSand()
            requestData = {
                'sessionKey': session,
                "target": group,
               "urls": [
                    data['url']
                    ]
            }
        
        if  message[:2] == '小药':
            command = message[2:]
            commandPart = command.split()
            data = query.getHeighten(commandPart[0])
            datastr = '心法： '+data['Name']+'\n'+'增强食品:  '+data['HeightenFood']+'\n'+'辅助食品： '+data['AuxiliaryFood']+'\n'+'增强药品： '+data['HeightenDrug']+'\n'+'辅助药品:  '+data['AuxiliaryDrug']
            requestData = {
                'sessionKey': session,
                "target": group,
                "messageChain": [{
                    "type": "Plain",
                    "text": datastr
                }]
            }

        print(requestData)

        if message[:2] == '沙盘':
            res = requests.post('http://' + testMirai.myurl + '/sendImageMessage',
                            json=requestData)
        else:
            res = requests.post('http://' + testMirai.myurl + '/sendGroupMessage',
                            json=requestData)

        jsonData = res.json()
        print(jsonData)
        if jsonData['code'] == 0:
            print('Sent')
        else:
            print('Send failed')

        # if message[:2] == 'ns':  #如果开头不是ns那么一切免谈，无事发生
        #     command = message[2:]  #把ns去掉后面开始分割这个指令
        #     commandPart = command.split()  #按照空格进行分割，但是后续要看看是不是加入更多的防傻判断
        #     if commandPart[0] == '开团':
        #         date = commandPart[1]
        #         time = commandPart[2]
        #         dungeon = commandPart[3]
        #         comment = commandPart[4]
        #         if commandPart[5] == '1':  #这TM判断不了直接报索引溢出就尼玛离谱，垃圾python毁我青春
        #             useBlackList = 1
        #         else:
        #             useBlackList = 0
        #         temp = '收到开团指令 日期：{} 时间：{} 副本名称：{} 注释：{} 是否启用黑名单：{}'.format(
        #             date, time, dungeon, comment, useBlackList)
        #         print(temp)