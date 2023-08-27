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
    question_amount = {
        "under1":13,
        "above1":7,
        "above2":12,
        "above3":13,
        "above4":9,
        "above5":7,
        "above6":11
    }
    # Part A 處理
    if context == "background":
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data_dict[context], "None") 
        
        # 偵測 intent
        if len(waiting_question) == 5:
            resultDICT = getLokiResult(context, msgSTR, ["age"])
        elif len(waiting_question) == 4:
            resultDICT = getLokiResult(context, msgSTR, ["ten_month"])
        elif len(waiting_question) == 3:
            resultDICT = getLokiResult(context, msgSTR, ["weight"])
        elif len(waiting_question) == 2:
            resultDICT = getLokiResult(context, msgSTR, ["congenital_disease", "yes_no"])
        elif len(waiting_question) == 1:
            resultDICT = getLokiResult(context, msgSTR, ["genetic_disease", "yes_no"])
        
        # 資料寫入字典
        for key in resultDICT.keys():
            data_dict[context][key] = resultDICT[key]
        
        # 確認 Part A 資料是否收集完畢
        if len(get_key_from_value(data_dict[context], "None")) == 0:
            data_dict["a"] = True

    # Part B 處理
    elif context == "environment":
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data_dict[context], "None")

        # 偵測 intent
        if len(waiting_question) == 2:
            resultDICT = getLokiResult(context, msgSTR, ["school", "yes_no"])
        elif len(waiting_question) == 1:
            resultDICT = getLokiResult(context, msgSTR, ["3C", "yes_no"])
        
        # 資料寫入字典
        for key in resultDICT.keys():
            data_dict[context][key] = resultDICT[key][0]
            
        # 確認 Part B 資料是否收集完畢
        if len(get_key_from_value(data_dict[context], "None")) == 0:
            data_dict["b"] = True
    
    # Part C 處理
    else:
        # 檢查目前提問進展
        amount = question_amount[context]
        waiting_question = get_key_from_value(data_dict["behavior"], "None")

        # 偵測 intent
        resultDICT = getLokiResult(context, msgSTR, [waiting_question[0], "yes_no"])

        # 資料寫入字典
        for key in resultDICT.keys():
            data_dict[key] = resultDICT[key][0]
        
        if len(get_key_from_value(data_dict["behavior"], "None")) == 13-amount:
            data_dict["behavior"]["response"] = give_advice(context, data_dict["background"]["age"], data_dict)
            data_dict["c"] = True
        else:
            data_dict["response"] = resultDICT["response"]

    return data_dict


    