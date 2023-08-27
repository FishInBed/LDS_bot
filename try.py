def get_key_from_value(dict, val):
    resultList = []
    for key, value in dict.items():
        if val == value:
            resultList.append(key)
    return resultList 

try_dict = {"updatetime" : None,
                             "latestQuest": "",
                             "background":{
                                 "age":"None",
                                 "ten_month":"None",
                                 "weight":"None",
                                 "congenital_disease":"None",
                                 "gentic_disease":"None",
                             },
                             "environment":{
                                 "school":"None",
                                 "3c":"None"                                 
                             },
                             "behavior":{
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
                                 "q13":"None"
                             },
                             "a":False,
                             "b":False,
                             "c":False,
                             "response":[]
        }

print(get_key_from_value(try_dict["background"], "None"))