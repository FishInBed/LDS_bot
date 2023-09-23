#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for play_with_adults

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

DEBUG_play_with_adults = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_play_with_adults.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_play_with_adults:
        print("[play_with_adults] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    #NOTE
    if utterance == "[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
            resultDICT["q10"] = False
        else:
            pass

    if utterance == "[不太]看人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[不太]確定":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    
    # NOTE 只看過一兩次是True，為什麼不常跟很少就是False？然後會但不多跟會但不常又是True
    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
            resultDICT["q10"] = True
        else:
            pass

    if utterance == "[小孩]沒[興趣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    #NOTE
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "常常" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
                resultDICT["q10"] = True
            elif "不常" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
                resultDICT["q10"] = False
        else:
            pass
    #NOTE
    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
                resultDICT["q10"] = True
            elif "少" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
                resultDICT["q10"] = False
        else:
            pass
    #NOTE
    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
            resultDICT["q10"] = True
        else:
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
            resultDICT["q10"] = True
        else:
            pass

    if utterance == "不[一定]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不喜歡跟[大人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不太理人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不跟[大人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "並不[會]每次":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，就算是您或其他家人在跟孩子玩的時候，孩子多半是安靜無聲的嗎？"
            resultDICT["q10"] = True
        else:
            pass

    if utterance == "看[心情]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT