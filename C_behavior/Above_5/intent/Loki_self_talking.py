#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for self_talking

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_self_talking = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_self_talking.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_self_talking:
        print("[self_talking] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直][都]是":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[一直][都]是[這樣]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[會][一直]重覆":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "不[一定]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像有":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "很少見":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = True
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = True
        else:
            # write your code here
            pass

    if utterance == "火星語":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "說[一些][別人]聽不懂的":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q7"] = False
        else:
            # write your code here
            pass

    return resultDICT