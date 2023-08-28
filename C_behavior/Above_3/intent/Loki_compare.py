#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for compare

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

DEBUG_compare = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_compare.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_compare:
        print("[compare] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不太]確定":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[偶爾]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太行":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像[可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "那關於說話的部分呢...您的孩子已經可以說出完整的短句(例如：我要喝水)了嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    return resultDICT