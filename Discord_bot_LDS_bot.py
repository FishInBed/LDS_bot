#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint

from A_background.A_background import execLoki as background_execLoki
from B_environment.B_environment import execLoki as environment_execLoki
from C_behavior.Under_1.Under_1 import execLoki as under1_execLoki
from C_behavior.Above_1.Above_1 import execLoki as above1_execLoki
from C_behavior.Above_2.Above_2 import execLoki as above2_execLoki
from C_behavior.Above_3.Above_3 import execLoki as above3_execLoki
from C_behavior.Above_4.Above_4 import execLoki as above4_execLoki
from C_behavior.Above_5.Above_5 import execLoki as above5_execLoki
from C_behavior.Above_6.Above_6 import execLoki as above6_execLoki

logging.basicConfig(level=logging.DEBUG)




punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(context, inputSTR, filterList=[]):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = filterList
    if context == "background":
        resultDICT = background_execLoki(inputLIST, filterLIST)
    elif context == "environment":
        resultDICT = environment_execLoki(inputLIST, filterLIST)
    elif context == "under1":
        resultDICT = under1_execLoki(inputLIST, filterLIST)
    elif context == "above1":
        resultDICT = above1_execLoki(inputLIST, filterLIST)
    elif context == "above2":
        resultDICT = above2_execLoki(inputLIST, filterLIST)
    elif context == "above3":
        resultDICT = above3_execLoki(inputLIST, filterLIST)
    elif context == "above4":
        resultDICT = above4_execLoki(inputLIST, filterLIST)
    elif context == "above5":
        resultDICT = above5_execLoki(inputLIST, filterLIST)
    else:
        resultDICT = above6_execLoki(inputLIST, filterLIST)

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
                             "A_background":{
                                 "age_year":"None",
                                 "age_month":"None", 
                                 "gender":"None",
                                 "ten_month":"None",
                                 "weight":"None",
                                 "congenital_disease":"None",
                                 "hospitalized":"None",
                                 "gentic_disease":"None",
                             },
                             "B_environment":{
                                 "sibling":"None",
                                 "carer":"None",
                                 "school":"None",
                                 "3c":"None"                                 
                             },
                             "C_behavior":{
                                 "q1":"None",
                                 "q2":"None",
                                 "q3":"None",
                                 "q4":"None",
                                 "q5":"None",
                                 "q6":"None",
                                 "q7":"None",
                                 "q8":"None",
                                 "q9":"None",
                                 "q10":"None",
                                 "q11":"None",
                                 "q12":"None",
                                 "q13":"None",
                                 "q14":"None"
                             },
                             "a":False,
                             "b":False,
                             "c":False
        }
        self.mscDICT = { "userid":self.templateDICT
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
                        replySTR = "嗨嗨，我們好像見過面，但其實我的記憶力跟金魚差不了多少，所以要重新開始問一次喔～" #可以自修改回應內容
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[str(message.author.id)+":"+str(message.author)]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[str(message.author.id)+":"+str(message.author)] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title() + "\n我是線上語言能力篩檢助理機器人。我可以幫助你了解孩子的語言發展狀況。在此之前須要先知道一下孩子的基本訊息，請問他現在幾歲呢？"

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                if "None" in self.mscDICT[str(message.author.id)+":"+str(message.author)]["A_background"].values():
                    resultDICT = getLokiResult()
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
