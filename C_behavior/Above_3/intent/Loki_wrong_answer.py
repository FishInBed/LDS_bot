#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for wrong_answer

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

DEBUG_wrong_answer = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_wrong_answer.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_wrong_answer:
        print("[wrong_answer] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直][都]是[這樣]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q12"] = False
        else:
            # write your code here
            pass

    if utterance == "[對]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q12"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
                resultDICT["q12"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "很" in inputSTR:
                resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
                resultDICT["q12"] = False
            elif "不" in inputSTR:
                resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
                resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
            resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "很少": 
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "謝謝您協助我們了解孩子目前的語言互動表現，接下來我們會根據收集到的內容提供您相關的建議哦～"
                resultDICT["q12"] = False
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT