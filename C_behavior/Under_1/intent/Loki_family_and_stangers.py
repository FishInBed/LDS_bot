#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for family_and_stangers

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

DEBUG_family_and_stangers = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_family_and_stangers.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_family_and_stangers:
        print("[family_and_stangers] {} ===> {}".format(inputSTR, utterance))

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
            pass

    if utterance == "[小孩][很]喜歡跟[人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
            resultDICT["q5"] = True
        else:
            pass
    # NOTE: 害羞跟怕生的判斷是不一樣的，這是正常的嗎？
    if utterance == "[小孩][很]害羞":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[小孩]不喜歡[別人]碰[他]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[小孩]不太理人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    
    #NOTE
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "常常" in inputSTR:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = True
            elif "不常" in inputSTR:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = False
        else:
            pass
    #NOTE
    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "這樣呀...那對於熟悉的家人與陌生的人，孩子看到不認識的人會不會有害羞或害怕的反應呢？"
                resultDICT["q4"] = True
            elif "少" in inputSTR:
                resultDICT["response"] = "這樣呀...那對於熟悉的家人與陌生的人，孩子看到不認識的人會不會有害羞或害怕的反應呢？"
                resultDICT["q4"] = False
        else:
            pass

    if utterance == "不[一定]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
            resultDICT["q5"] = False
        else:
            pass

    if utterance == "分不出來":
        if CHATBOT_MODE:
            resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
            resultDICT["q5"] = False
        else:
            pass

    if utterance == "沒[什麼]反應":
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