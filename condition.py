import logging
import re
from A_background.A_background import execLoki as background_execLoki
from B_environment.B_environment import execLoki as environment_execLoki
from C_behavior.Under_1.Under_1 import execLoki as under1_execLoki
from C_behavior.Above_1.Above_1 import execLoki as above1_execLoki
from C_behavior.Above_2.Above_2 import execLoki as above2_execLoki
from C_behavior.Above_3.Above_3 import execLoki as above3_execLoki
from C_behavior.Above_4.Above_4 import execLoki as above4_execLoki
from C_behavior.Above_5.Above_5 import execLoki as above5_execLoki
from C_behavior.Above_6.Above_6 import execLoki as above6_execLoki

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def operateLoki(context, inputSTR, filterList=[]):
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

def get_key_from_value(dict, val):
    resultList = []
    for key, value in dict.items():
        if val == value:
            resultList.append(key)
    return resultList 

def give_advice(context, age, final_data):
    target_age = age
    accpetance = len(get_key_from_value(final_data[context], True))
    if target_age//12 == 0:
        if accpetance >= 10:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance <= 9 and accpetance >= 6:
            result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        elif accpetance <= 5:
            if target_age >= 6 and target_age < 11:
                result = "您可以再觀察四至六個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            elif target_age > 11:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else:
            result = "目前孩子正處理語言發展的準備前期，建議您可以多跟孩子互動，並持續觀察孩子與您的互動表現，待孩子大一點，如：十個月大或近一歲時，若還不能發出一些不同的聲音時，再到醫療院所進行語言篩檢。"

    elif target_age//12 == 1:
        if accpetance >= 6:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 4 or accpetance == 5:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            if target_age >= 12 and target_age <= 18:
                if len(get_key_from_value(final_data["background"], False)) == 0:
                    result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
                else:
                    result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif target_age >= 19:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    
    elif target_age//12 == 2:
        if accpetance >= 8:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 4 and accpetance <= 7:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    
    elif target_age//12 == 3:
        if accpetance >= 8:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 4 and accpetance <= 7:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            
    elif target_age//12 == 4:
        if accpetance >= 7:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 3 and accpetance <= 6:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"

    elif target_age//12 == 5:
        if accpetance >= 6:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 4 or accpetance == 5:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"

    elif target_age//12 == 6:
        if accpetance >= 10:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 8 or accpetance == 9:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    return result

def condition_control(dicts, context, msgSTR):
    data_dict = dicts
    meta_data = {
        "under1":{
            "amount":13,
            "q1":"孩子現階段可以發出一些聽起來是有變化的組合音，如：ㄉㄚ/ㄅㄚ/ㄚ，而且達到三種(或以上)嗎？"},
        "above1":{
            "amount":7,
            "q1":"孩子會不會用手勢或動作來表達自己的喜好呢？例如：點頭表是「要」或「好」、搖頭表示「不要」、手指指物、把東西推開？"},
        "above2":{
            "amount":12,
            "q1":"孩子是不是可以正確指出至少四個身體部位呢？例如：眼睛、鼻子、嘴巴、耳朵、手、腳？"},
        "above3":{
            "amount":13,
            "q1":"孩子可不可以使用約三到四個語詞組成的短句和大人一問一答呢？"},
        "above4":{
            "amount":9,
            "q1":"孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"},
        "above5":{
            "amount":7,
            "q1":"在沒有任何協助的情況下，孩子是不是可以看懂並唸出七個非連續的阿拉伯數字呢？"},
        "above6":{
            "amount":11,
            "q1":"孩子說話時的口齒不清，需要親近家人翻譯後他人才聽得懂嗎？"}
    }
    # Part A 處理
    if context == "background":
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data_dict[context], "None") 
        
        # 偵測 intent
        if "half" in data_dict[context].keys():
            resultDICT = operateLoki(context, msgSTR, ["recheck"])
            data_dict.pop("half")
        else:
            if len(waiting_question) == 5:
                resultDICT = operateLoki(context, msgSTR, ["age"])
            elif len(waiting_question) == 4:
                resultDICT = operateLoki(context, msgSTR, ["ten_month"])
            elif len(waiting_question) == 3:
                resultDICT = operateLoki(context, msgSTR, ["weight"])
            elif len(waiting_question) == 2:
                resultDICT = operateLoki(context, msgSTR, ["congenital_disease", "yes_no"])
                if "yes_no" in resultDICT.keys() and "congenital_disease" not in resultDICT.keys():
                    resultDICT["congenital_disease"] = resultDICT["yes_no"]
                    resultDICT["response"] = ["了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"]
                    resultDICT.pop("yes_no")
            elif len(waiting_question) == 1:
                resultDICT = operateLoki(context, msgSTR, ["genetic_disease", "yes_no"])
                if "yes_no" in resultDICT.keys() and "genetic_disease" not in resultDICT.keys():
                    if resultDICT["yes_no"] == False:
                        resultDICT["gentic_disease"] = False
                        resultDICT["response"] = ["好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"]
                        resultDICT.pop("yes_no")
                    else:
                        resultDICT["response"] = ["那麼是孩子的哪位親人有什麼樣的遺傳性疾病呢？"]
                        resultDICT.pop("yes_no")
        
        # 資料寫入字典
        if "response" in data_dict[context].keys():
            data_dict[context].pop("response")
            for key in resultDICT.keys():
                data_dict[context][key] = resultDICT[key][0]
        else:
            for key in resultDICT.keys():
                data_dict[context][key] = resultDICT[key][0]
        
#TODO: 補跟yes_no交叉比對的判斷式

        # 確認 Part A 資料是否收集完畢
        if len(get_key_from_value(data_dict[context], "None")) == 0:
            data_dict["a"] = True

    # Part B 處理
    elif context == "environment":
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data_dict[context], "None")

        # 偵測 intent
        if len(waiting_question) == 2:
            resultDICT = operateLoki(context, msgSTR, ["school", "yes_no"])
            if "yes_no" in resultDICT.keys() and "school" not in resultDICT.keys():
                resultDICT["school"] = resultDICT["yes_no"]
                resultDICT["response"] = ["那麼孩子每天使用3C產品(包括：手機、平版、電腦、電視)的總時間有超過2小時嗎?"]
                resultDICT.pop("yes_no")

        elif len(waiting_question) == 1:
            resultDICT = operateLoki(context, msgSTR, ["3C", "yes_no"])
            if "yes_no" in resultDICT.keys() and "3c" not in resultDICT.keys():
                resultDICT["3c"] = resultDICT["yes_no"]
                resultDICT["response"] = ["好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對他平常的行為表現作更深入的了解囉。"]
                resultDICT.pop("yes_no")

        # 資料寫入字典
        for key in resultDICT.keys():
            data_dict[context][key] = resultDICT[key][0]
            
        # 確認 Part B 資料是否收集完畢
        if len(get_key_from_value(data_dict[context], "None")) == 0:
            data_dict["b"] = True
        if data_dict["b"] == True:
            age = data_dict["background"]["age"] // 12
            if age == 0:
                data_dict[context]["response"] =data_dict[context]["response"] + "\n" + meta_data["under1"]["q1"]
            else:
                new_context = "above" + str(age)
                data_dict[context]["response"] =data_dict[context]["response"] + "\n" + meta_data[new_context]["q1"]
    
    # Part C 處理
    else:
        # 檢查目前提問進展
        amount = meta_data[context]["amount"]
        waiting_question = get_key_from_value(data_dict["behavior"], "None")

        # 偵測 intent
        resultDICT = operateLoki(context, msgSTR, ["yes_no", waiting_question[0]])

        # 資料寫入字典
        for key in resultDICT.keys():
            data_dict[context][key] = resultDICT[key][0]
        
        if len(get_key_from_value(data_dict["behavior"], "None")) == 13-amount:
            data_dict["behavior"]["response"] = give_advice(context, data_dict["background"]["age"], data_dict)
            data_dict["c"] = True

        # 判斷對話是否結束，如果結束就給建議
        if data_dict["c"] == True:
            data_dict["behaivor"]["response"] = give_advice(data_dict["background"]["age"], data_dict)

    return data_dict

if __name__ == "__main__":
    dicts = {'a': False,
            'b': False,
            'background': {'age': 29,
                            'congenital_disease': 'None',
                            'gentic_disease': 'None',
                            'response': '2歲5個月啊。\n'
                                        '那麼孩子出生時是否足月呢？',
                            'ten_month': "None",
                            'weight': 'None'},
            'behavior': {'q1': 'None',
                        'q10': 'None',
                        'q11': 'None',
                        'q12': 'None',
                        'q13': 'None',
                        'q2': 'None',
                        'q3': 'None',
                        'q4': 'None',
                        'q5': 'None',
                        'q6': 'None',
                        'q7': 'None',
                        'q8': 'None',
                        'q9': 'None'},
            'c': False,
            'environment': {'3c': 'None',
                            'school': 'None'}} #弄個測試用的回傳字典
    context = "background"
    msgSTR = "是早產"
    resultDICT = condition_control(dicts, context, msgSTR)
    print(resultDICT)
    