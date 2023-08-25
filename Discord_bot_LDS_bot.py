#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint

from Under_1 import runLoki

logging.basicConfig(level=logging.DEBUG)




punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID): # MSC = Multi section conversation多輪對話(不斷更新說話時間)
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "age":None, 
                             "gender":None,
                             "sibling":None,
                             "3c":None
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user: #bot不會回自己
            return None
        print(message)
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            #msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            msgSTR = re.sub("<@\d+>\s?", "", message.content).strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:  #把英文字母收斂成小寫
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():  #直接去找之前是否有對話過
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[str(message.author.id)+":"+str(message.author)] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！" #可以自修改回應內容
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[str(message.author.id)+":"+str(message.author)]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[str(message.author.id)+":"+str(message.author)] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title() + "\n我是線上語言能力篩檢助理機器人。我可以幫助你了解小朋友的語言發展狀況。請問小朋友現在幾歲呢？"

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                replySTR = resultDICT["response"][0]
            pprint(self.mscDICT)
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
