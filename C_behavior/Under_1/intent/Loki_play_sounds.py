#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for play_sounds

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

DEBUG_play_sounds = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_play_sounds.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_play_sounds:
        print("[play_sounds] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
            resultDICT["q9"] = True
        else:
            pass

    if utterance == "[不太]確定":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    #NOTE
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "常常" in inputSTR:
                resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
                resultDICT["q9"] = True
            elif "不常" in inputSTR:
                resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
                resultDICT["q9"] = False
        else:
            pass
    #NOTE
    if utterance == "[很多]":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
                resultDICT["q9"] = True
            elif "少" in inputSTR:
                resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
                resultDICT["q9"] = False
        else:
            pass
    
    #NOTE 如果下面這兩句都是true，那跟會就一樣了，是不是這兩個utterance可以不用
    if utterance == "[會]但[聲音][都]很像":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
            resultDICT["q9"] = True
        else:
            pass
    
    if utterance == "[會]但[聲音]沒[什麼]變化":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
            resultDICT["q9"] = True
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
    
    #NOTE 如果上面那句是繼續引導，為什麼下面這句不用
    if utterance == "不太[會]而且[聲音]很少":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...哦，對了...那當您跟孩子玩遊戲(如：手指遊戲或躲貓貓)時，孩子會不會一起玩並被逗笑呢？"
            resultDICT["q9"] = True
        else:
            pass

    if utterance == "看[心情]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT