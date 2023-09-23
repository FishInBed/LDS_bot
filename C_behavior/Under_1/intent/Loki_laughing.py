#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for laughing

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

DEBUG_laughing = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_laughing.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_laughing:
        print("[laughing] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    
    #NOTE 這裡跟前幾題不一樣
    if utterance == "[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[不太]確定":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    
    #NOTE
    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外想知道的是...當您與孩子面對面時，孩子會不會注視您的臉，而且會覺得有趣好玩嗎？"
            resultDICT["q7"] = True
        else:
            pass
    #NOTE
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "常常" in inputSTR:
                resultDICT["response"] = "另外想知道的是...當您與孩子面對面時，孩子會不會注視您的臉，而且會覺得有趣好玩嗎？"
                resultDICT["q7"] = True
            elif "不常" in inputSTR:
                resultDICT["response"] = "另外想知道的是...當您與孩子面對面時，孩子會不會注視您的臉，而且會覺得有趣好玩嗎？"
                resultDICT["q7"] = False
        else:
            pass
    
    #NOTE 有些題目的很少是繼續引導，但有些是直接False，然後上面只有一兩次卻是True，有點不懂
    if utterance == "[很少]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外想知道的是...當您與孩子面對面時，孩子會不會注視您的臉，而且會覺得有趣好玩嗎？"
            resultDICT["q7"] = False
        else:
            pass

    if utterance == "不[一定]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "看[心情]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT